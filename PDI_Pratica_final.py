import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn
import os
import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


epochs = 1
batch = 32
train_model = 'outro'
index =0

#carrega o modelo da inception_v3 com os pesos aprendidos no treino da ImageNet sem a camada densa (include_top=False)

base_model = tf.keras.applications.VGG19(weights='imagenet', include_top=False, input_shape = (224,224,3) )


#O restante do modelo e suas camadas são discutidos a seguir
#x recebe o final da inception_v3

x=base_model.output

#Nova configuração para o modelo

#adiciona apos x uma camada AveragePooling2D e atribui este no a x novamente (logo x e o topo novamente)
#x=tf.keras.layers.GlobalAveragePooling2D()(x)

#adiciona apos x duas camada conv com 64 neuronios com funcao de ativacao relu. Atribui este no a x novamente
#x=tf.keras.layers.Conv2D(64, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(64, 3, activation='relu')(x)
#x=tf.keras.layers.MaxPooling2D((2,2), strides = (2,2))(x)

#adiciona apos x duas camada conv com 128 neuronios com funcao de ativacao relu. Atribui este no a x novamente
#x=tf.keras.layers.Conv2D(128, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(128, 3, activation='relu')(x)
#x=tf.keras.layers.MaxPooling2D((2,2), strides = (2,2))(x)

#adiciona apos x quatro camada conv com 256 neuronios com funcao de ativacao relu. Atribui este no a x novamente
#x=tf.keras.layers.Conv2D(256, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(256, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(256, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(256, 3, activation='relu')(x)
#x=tf.keras.layers.MaxPooling2D((2,2), strides = (2,2))(x)

#adiciona apos x quatro camada conv com 512 neuronios com funcao de ativacao relu. Atribui este no a x novamente
#x=tf.keras.layers.Conv2D(512, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(512, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(512, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(512, 3, activation='relu')(x)
#x=tf.keras.layers.MaxPooling2D((2,2), strides = (2,2))(x)

#adiciona apos x quatro camada conv com 512 neuronios com funcao de ativacao relu. Atribui este no a x novamente
#x=tf.keras.layers.Conv2D(512, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(512, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(512, 3, activation='relu')(x)
#x=tf.keras.layers.Conv2D(512, 3, activation='relu')(x)
#x=tf.keras.layers.MaxPooling2D((2,2), strides = (2,2))(x)

x=tf.keras.layers.Flatten()(x)

#adiciona apos x duas camada densa com 4096 neuronios com funcao de ativacao relu. Atribui este no a x novamente
x=tf.keras.layers.Dense(4096,activation='relu')(x)
x=tf.keras.layers.Dense(4096,activation='relu')(x)

#adiciona apos x uma camada densa com 7 neuronios (duas classes) com funcao de ativacao softmax (distribuicao de probabilidade). Atribui este no a preds
preds=tf.keras.layers.Dense(7,activation='softmax', name='predictions')(x)

#definindo modelo final
model=tf.keras.models.Model(inputs=base_model.input,outputs=preds)

#mostrando modelo final e sua estrutura
model.summary()

#congelando os neuronios já treinados na ImageNet, queremos retreinar somente a ultima camada
for l in model.layers:
  if l.name.split('_')[0] != 'dense':
    l.trainable=False
  else:
    l.trainable=True


#iniciando objeto que apanhara todas as imagens de treino, processando as imagens com o metodo da InceptionV3
train_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(preprocessing_function=tf.keras.applications.inception_v3.preprocess_input) #included in our dependencies

#iniciando objeto que apanhara todas as imagens de teste, processando as imagens com o metodo da InceptionV3
test_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(preprocessing_function=tf.keras.applications.inception_v3.preprocess_input)

#CARREGANDO PRÓPRIO DATASET PARA USO

#definindo gerador de imagens de treino
train_generator = train_data_gen.flow_from_directory('train', target_size=(224,224),color_mode='rgb',batch_size=batch,class_mode='categorical',shuffle=True)

#definindo gerador de imagens de teste
test_generator = train_data_gen.flow_from_directory('test', target_size=(224,224),color_mode='rgb', batch_size=batch,class_mode='categorical',shuffle=True)

lr = tf.keras.optimizers.Adam(learning_rate=0.0001)#estabelecendo taxa de otimização

model.compile(optimizer=lr, loss='categorical_crossentropy', metrics=['accuracy'])

#definicao dos steps
step_size_train= train_generator.n//train_generator.batch_size
step_size_test = test_generator.n//test_generator.batch_size



#treinando e testando o modelo
history = model.fit_generator(generator=train_generator, steps_per_epoch=step_size_train, epochs=epochs, validation_data=test_generator, validation_steps=step_size_test)





#Avaliando o modelo
loss_train, train_acc = model.evaluate_generator(train_generator, steps=step_size_train)
loss_test, test_acc = model.evaluate_generator(test_generator, steps=step_size_test)
print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))
#Apresentando resultados em graficos
plt.title('Loss')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()


# Criando graficos para visualização dos resultados
print()
print()
plt.title('Accuracy')
plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='test')
plt.legend()
plt.show()

print('Criando classificações..')
labels = os.listdir('train')
print('Rótulos', labels)


#criando estruturas para métricas de avaliação, processo um pouco mais demorado
Y_pred = model.predict_generator(test_generator)
print('Preds Created')
y_pred = np.argmax(Y_pred, axis=1)
print('Preds 1D created')

classification = classification_report(test_generator.classes, y_pred, target_names=labels)
print('----------------CLASSIFICATION--------------')
print(classification)
matrix = confusion_matrix(test_generator.classes, y_pred)
df_cm = pd.DataFrame(matrix, index = [i for i in range(7)],
                  columns = [i for i in range(7)])
plt.figure(figsize = (10,7))
sn.heatmap(df_cm, annot=True, linewidths=2.5)

