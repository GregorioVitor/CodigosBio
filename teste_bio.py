#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:53:18 2020

@author: gregorio
"""


#python3 TCC.py -N 6 Arabidopsis_thaliana_GreeNC.fasta Arabidopsis_thaliana_CANTATA.fasta Oryza_sativa_Japonica_Group_GreeNC.fasta Oryza_sativa_Japonica_Group_CANTATA.fasta Zea_mays_GreeNC.fasta Zea_mays_CANTATA.fasta
#python3 teste_bio.py -N 7 FANTOM_Humanlv3_lncRNA_antisense_sem_N.fasta FANTOM_Humanlv3_lncRNA_divergent.fasta FANTOM_Humanlv3_lncRNA_intergenic.fasta FANTOM_Humanlv3_lncRNA_sense_intronic.fasta FANTOM_Humanlv3_pseudogene.fasta FANTOM_Humanlv3_sense_overlap_RNA.fasta FANTOM_Humanlv3_uncertain_coding.fasta 



from Bio import SeqIO
from Bio.SeqUtils import GC
import seaborn as sns
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



    
###########################################################################    
###################### width ##############################################
###########################################################################  

plt.style.use(['ggplot'])    
fig1 = plt.figure()
ax1 =fig1.add_subplot(1,1,1)
ax1.set_xlabel("Database")
ax1.set_ylabel("Width")
ax1.set_title("Width")


box =[]
red_diamond = dict(markerfacecolor='r', marker='D')

for j in range(0, args.N[0]):
    box.append(ax1.boxplot(arquivo[j], patch_artist= True, positions = [j], widths = 0.4,showmeans = True, meanprops = red_diamond)) ##plot do boxplot
    if j==0:
        plt.setp(box[0]["boxes"], color= "blue") ##cor verde do boxplot 
    elif j==1:
        plt.setp(box[1]["boxes"], color='orange') ##cor verde do boxplot
    elif j==2:
        plt.setp(box[2]["boxes"], color='green') ##cor verde do boxplot
    elif j==3:
        plt.setp(box[3]["boxes"], color='cyan') ##cor verde do boxplot
    elif j==4:
        plt.setp(box[4]["boxes"], color='purple') ##cor verde do boxplot
    elif j==5:
        plt.setp(box[5]["boxes"], color='brown') ##cor verde do boxplot
    elif j==6:
        plt.setp(box[6]["boxes"], color='pink') ##cor verde do boxplot
    elif j==7:
        plt.setp(box[7]["boxes"], color='grey') ##cor verde do boxplot
    elif j==8:
        plt.setp(box[8]["boxes"], color='yellow') ##cor verde do boxplot
    elif j==9:
        plt.setp(box[9]["boxes"], color='violet') ##cor verde do boxplot
   


##nomeando cada boxplot##
plt.xticks([])
if args.N[0]==1:
    plt.xticks([0], arq_f, fontsize= 'xx-small')
elif args.N[0]==2:
    plt.xticks([0,1], arq_f, fontsize= 'xx-small')
elif args.N[0]==3:
    plt.xticks([0,1,2], arq_f, fontsize= 'xx-small')
elif args.N[0]==4:
    plt.xticks([0,1,2,3], arq_f, fontsize= 'xx-small')
elif args.N[0]==5:
    plt.xticks([0,1,2,3,4], arq_f, fontsize= 'xx-small')
elif args.N[0]==6:
    plt.xticks([0,1,2,3,4,5], arq_f, fontsize= 'xx-small')
elif args.N[0]==7:
    plt.xticks([0,1,2,3,4,5,6], arq_f, fontsize= 'xx-small')
elif args.N[0]==8:
    plt.xticks([0,1,2,3,4,5,6,7], arq_f, fontsize= 'xx-small')
elif args.N[0]==9:
    plt.xticks([0,1,2,3,4,5,6,7,8], arq_f, fontsize= 'xx-small')
elif args.N[0]==10:
    plt.xticks([0,1,2,3,4,5,6,7,8,9], arq_f, fontsize= 'xx-small')

plt.subplots_adjust(hspace= 0.45, wspace= 0.4, left = 0.045, right = 0.99)
fig1.set_size_inches(18.5, 10.5)
plt.savefig("BoxPlotWidth.png") ##salvando o boxplot    
plt.show()


###########################################################################    
################ width without outliers####################################
########################################################################### 

fig2 = plt.figure()
ax2 =fig2.add_subplot(1,1,1)
ax2.set_xlabel("Database")
ax2.set_ylabel("Width")
ax2.set_title("Width without Outliers")


box=[]
for j in range(0, args.N[0]):
    box.append(ax2.boxplot(arquivo[j], patch_artist= True, positions = [j], widths = 0.4,showmeans = True, meanprops = red_diamond, showfliers= False)) ##plot do boxplot
    plt.setp(box[j]["boxes"], facecolor=(0,0.49,1)) ##cor verde do boxplot 


##nomeando cada boxplot##
plt.xticks([])
if args.N[0]==1:
    plt.xticks([0], arq_f, fontsize= 'xx-small')
elif args.N[0]==2:
    plt.xticks([0,1], arq_f, fontsize= 'xx-small')
elif args.N[0]==3:
    plt.xticks([0,1,2], arq_f, fontsize= 'xx-small')
elif args.N[0]==4:
    plt.xticks([0,1,2,3], arq_f, fontsize= 'xx-small')
elif args.N[0]==5:
    plt.xticks([0,1,2,3,4], arq_f, fontsize= 'xx-small')
elif args.N[0]==6:
    plt.xticks([0,1,2,3,4,5], arq_f, fontsize= 'xx-small')
elif args.N[0]==7:
    plt.xticks([0,1,2,3,4,5,6], arq_f, fontsize= 'xx-small')
elif args.N[0]==8:
    plt.xticks([0,1,2,3,4,5,6,7], arq_f, fontsize= 'xx-small')
elif args.N[0]==9:
    plt.xticks([0,1,2,3,4,5,6,7,8], arq_f, fontsize= 'xx-small')
elif args.N[0]==10:
    plt.xticks([0,1,2,3,4,5,6,7,8,9], arq_f, fontsize= 'xx-small')

plt.subplots_adjust(hspace= 0.45, wspace= 0.4, left = 0.045, right = 0.99)
fig2.set_size_inches(18.5, 10.5)
plt.savefig("BoxPlotWidthOutliers.png") ##salvando o boxplot    
plt.show()


###########################################################################    
##################### GC Cont #############################################
###########################################################################  

fig3 = plt.figure()
ax3 =fig3.add_subplot(1,1,1) 
ax3.set_xlabel("Database")
ax3.set_ylabel("GC%")
ax3.set_title("GC Content")

gc_cont = []
for aux in range(0, args.N[0]):
    gc_cont.append([GC(rec.seq) for rec in SeqIO.parse(arq[aux],"fasta")])           
    
box =[]
for j in range(0, args.N[0]):
    box.append(ax3.boxplot(gc_cont[j], patch_artist= True, positions = [j], widths = 0.4, showmeans = True, meanprops = red_diamond)) ##plot do boxplot
    plt.setp(box[j]["boxes"], facecolor="blue") ##cor verde do boxplot 

        
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
    
plt.subplots_adjust(hspace= 0.45, wspace= 0.4, left = 0.045, right = 0.99)
fig3.set_size_inches(18.5, 10.5)
plt.savefig("BoxPlotCont.png") ##salvando o boxplot    
plt.show()
    

###########################################################################    
################ GC Cont without Outliers##################################
###########################################################################  

fig4 = plt.figure()
ax4 =fig4.add_subplot(1,1,1)
ax4.set_xlabel("Database")
ax4.set_ylabel("GC%")
ax4.set_title("GC Content without Outliers")

box =[]
for j in range(0, args.N[0]):
    box.append(ax4.boxplot(gc_cont[j], patch_artist= True, positions = [j], widths = 0.4, showmeans = True, meanprops = red_diamond, showfliers = False)) ##plot do boxplot
    plt.setp(box[j]["boxes"], facecolor="blue") ##cor verde do boxplot 

        
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
    
plt.subplots_adjust(hspace= 0.45, wspace= 0.4, left = 0.045, right = 0.99)
fig4.set_size_inches(18.5, 10.5)
plt.savefig("BoxPlotCont.png") ##salvando o boxplot    
plt.show()



###########################################################################    
##################### GC Ratio ############################################
###########################################################################    
   
fig5 = plt.figure()    
ax5 = fig5.add_subplot(1,1,1)   
ax5.set_xlabel("Database")
ax5.set_ylabel("GC Ratio")
ax5.set_title("GC Ratio")

nucleotideos =['A','C','G','T']


box =[]
GC_ratio_list = []
con_nuc=[] #quantidade total de nucleotideo
for aux in range(0, args.N[0]):
    for rec in SeqIO.parse(arq[aux],"fasta"):
        seq_nuc = rec.seq    
        all_counts = [] #quantidade de nucleotideo de cada sequencia
        for nucleotide in nucleotideos:
            count = seq_nuc.count(nucleotide)
            all_counts.append(count)            
        GC_ratio_list.append((all_counts[0]+all_counts[3])/(all_counts[1]+all_counts[2]))
    con_nuc.append(GC_ratio_list)
    GC_ratio_list = []
        

box =[]
for j in range(0, args.N[0]):
    box.append(ax5.boxplot(con_nuc[j], patch_artist= True, positions = [j], widths = 0.4,showmeans = True, meanprops = red_diamond)) ##plot do boxplot
    plt.setp(box[j]["boxes"], facecolor="cyan") ##cor verde do boxplot 


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
    

    
plt.subplots_adjust(hspace= 0.45, wspace= 0.4, left = 0.045, right = 0.99)
fig5.set_size_inches(18.5, 10.5)
plt.savefig("BoxPlotRatio.png") ##salvando o boxplot    
plt.show()


###########################################################################    
################### GC Ratio without outliers##############################
########################################################################### 

fig6 = plt.figure()    
ax6 = fig6.add_subplot(1,1,1)  
ax6.set_xlabel("Database")
ax6.set_ylabel("GC Ratio")
ax6.set_title("GC Ratio without Outliers")

box =[]
for j in range(0, args.N[0]):
    box.append(ax6.boxplot(con_nuc[j], patch_artist= True, positions = [j], widths = 0.4,showmeans = True, meanprops = red_diamond, showfliers = False)) ##plot do boxplot
    plt.setp(box[j]["boxes"], facecolor="cyan") ##cor verde do boxplot 


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
    

    
plt.subplots_adjust(hspace= 0.45, wspace= 0.4, left = 0.045, right = 0.99)
fig6.set_size_inches(18.5, 10.5)
plt.savefig("BoxPlotRatio.png") ##salvando o boxplot    
plt.show()



    
###########################################################################    
################## dinucleotideo ##########################################
###########################################################################  

#from dinucleotideo import Dinucle

#for j in range(0, args.N[0]):
#    arq_seq = str(arq[j])
#    arq_nome= str(arq_f[j])
#    p1 = Dinucle(arq_seq, arq_nome)

###########################################################################    
################## trinucleotideo ##########################################
###########################################################################  

#from trinucleotideo import Trinucle

#for j in range(0, args.N[0]):
#    arq_seq2 = str(arq[j])
#    arq_nome2= str(arq_f[j])
#    p2 = Trinucle(arq_seq2, arq_nome2)




    


