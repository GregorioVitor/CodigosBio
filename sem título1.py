#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 19:00:11 2020

@author: gregorio
"""


import numpy as np
import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio.SeqUtils import GC

        

arq =["/home/gregorio/Desktop/PlantasTCC/Oryza_sativa_Japonica_Group_CANTATA.fasta", 
      "/home/gregorio/Desktop/PlantasTCC/Oryza_sativa_Japonica_Group_GreeNC.fasta",
      "/home/gregorio/Desktop/PlantasTCC/Zea_mays_CANTATA.fasta",
      "/home/gregorio/Desktop/PlantasTCC/Zea_mays_GreeNC.fasta"]
arquivo= []
for aux in range(0, len(arq)):
    arquivo.append([len(rec) for rec in SeqIO.parse(arq[aux],"fasta")]) ##salvando o comprimento de cada sequencia de cada database em vetor

plt.style.use("seaborn-whitegrid")
labels = list("ABCD")
colors = ["crimson", "purple", "limegreen", "gold"]
width=0.4


fig, ax = plt.subplots()
for i, l in enumerate(labels):
    data = np.array(arquivo[i])
    x = np.ones(data.shape[0])*i + (np.random.rand(data.shape[0])*width-width/2.)
    mean = data[:].mean()
    plt.scatter(x, data[:], s=25, c=x, cmap = "Pastel2" ,plotnonfinite=True)
    plt.plot([i-width/2., i+width/2.],[mean,mean], color="k")


plt.xticks(range(len(labels)),labels)


plt.show()
