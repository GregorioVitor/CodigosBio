#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:53:18 2020

@author: gregorio
"""


#python3 TCC.py -N 6 Arabidopsis_thaliana_GreeNC.fasta Arabidopsis_thaliana_CANTATA.fasta Oryza_sativa_Japonica_Group_GreeNC.fasta Oryza_sativa_Japonica_Group_CANTATA.fasta Zea_mays_GreeNC.fasta Zea_mays_CANTATA.fasta



from Bio import SeqIO
from Bio.SeqUtils import GC
import matplotlib.pyplot as plt
import sys
import argparse

####################Leitura do Arquivo########################
parser = argparse.ArgumentParser()

parser.add_argument('-N', metavar='N', nargs='+', help='an integer for the accumulator')
#parser.add_argument('-i', metavar='i', nargs='+', help='input file')


args=parser.parse_args()
args.N[0] = int(args.N[0]) ##numero de database para int    
print (args.N[0])

arq=[]
arq_f=[]
for i in range(3, (3 + args.N[0]) ):
    arq.append(sys.argv[i]) ##colocando o nome dos database em vetor
    arq_f.append(sys.argv[i].rstrip('.fasta').replace('_', " ")) ##colocando o nome dos database em vetor sem o .fasta

arquivo =[]
for aux in range(0, args.N[0]):
    arquivo.append([len(rec) for rec in SeqIO.parse(arq[aux],"fasta")]) ##salvando o comprimento de cada sequencia de cada database em vetor


fig = plt.figure()
    
###########################################################################    
###################### width ##############################################
###########################################################################    

ax1 =fig.add_subplot(2,1,1)
ax1.set_xlabel("Database")
ax1.set_ylabel("Tamanho")

box =[]
for j in range(0, args.N[0]):
    box.append(ax1.boxplot(arquivo[j], patch_artist= True, positions = [j], widths = 0.5)) ##plot do boxplot
    if j%2 == 0:
        plt.setp(box[j]["boxes"], facecolor="green") ##cor verde do boxplot 
    else:
        plt.setp(box[j]["boxes"], facecolor="yellow") ##cor amarela do boxplot
    
ax1.set_title("Width")

##nomeando cada boxplot##
rotate = 0      #valor do rotation no nome
plt.xticks([])
if args.N[0]==1:
    plt.xticks([0], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==2:
    plt.xticks([0,1], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==3:
    plt.xticks([0,1,2], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==4:
    plt.xticks([0,1,2,3], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==5:
    plt.xticks([0,1,2,3,4], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==6:
    plt.xticks([0,1,2,3,4,5], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==7:
    plt.xticks([0,1,2,3,4,5,6], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==8:
    plt.xticks([0,1,2,3,4,5,6,7], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==9:
    plt.xticks([0,1,2,3,4,5,6,7,8], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==10:
    plt.xticks([0,1,2,3,4,5,6,7,8,9], arq_f, rotation=rotate, fontsize= 'xx-small')


###########################################################################    
##################### GC Cont #############################################
###########################################################################  


ax2 =fig.add_subplot(2,1,2)
    
ax2.set_xlabel("Database")
ax2.set_ylabel("GC%")
ax2.set_title("GC Content")

gc_cont = []
for aux in range(0, args.N[0]):
    gc_cont.append([GC(rec.seq) for rec in SeqIO.parse(arq[aux],"fasta")])          

box =[]
for j in range(0, args.N[0]):
    box.append(ax2.boxplot(gc_cont[j], patch_artist= True, positions = [j], widths = 0.5)) ##plot do boxplot
    if j%2 == 0:
        plt.setp(box[j]["boxes"], facecolor="green") ##cor verde do boxplot 
    else:
        plt.setp(box[j]["boxes"], facecolor="yellow") ##cor amarela do boxplot
        
##nomeando cada boxplot##
plt.xticks([])
if args.N[0]==1:
    plt.xticks([0], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==2:
    plt.xticks([0,1], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==3:
    plt.xticks([0,1,2], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==4:
    plt.xticks([0,1,2,3], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==5:
    plt.xticks([0,1,2,3,4], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==6:
    plt.xticks([0,1,2,3,4,5], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==7:
    plt.xticks([0,1,2,3,4,5,6], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==8:
    plt.xticks([0,1,2,3,4,5,6,7], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==9:
    plt.xticks([0,1,2,3,4,5,6,7,8], arq_f, rotation=rotate, fontsize= 'xx-small')
elif args.N[0]==10:
    plt.xticks([0,1,2,3,4,5,6,7,8,9], arq_f, rotation=rotate, fontsize= 'xx-small')
    
plt.subplots_adjust(hspace= 0.45, wspace= 0.4)
fig.set_size_inches(18.5, 10.5)
plt.savefig("BoxPlot.png") ##salvando o boxplot    
plt.show()
    
###########################################################################    
################## dinucleotideo ##########################################
###########################################################################  

from dinucleotideo import Dinucle

for j in range(0, args.N[0]):
    arq_seq = str(arq[j])
    arq_nome= str(arq_f[j])
    p1 = Dinucle(arq_seq, arq_nome)



    


