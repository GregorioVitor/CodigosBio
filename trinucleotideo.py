#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:39:29 2020

@author: gregorio
"""

from Bio import SeqIO
import matplotlib.pyplot as plt

class Trinucle:
    def __init__(self, arq, arq_f):
        trinucleotides = ['ATC','ATG','ACC','AAC',
                         'AAT','AGA','CAT','CAC',
                         'CCA','CCG','CGG','CTT',
                         'GAT','GTA','GGT','GAA',
                         'GCC','GCA','TCA','TAG',
                         'TGA','TGG','TGC','TAT']
        
        con_trinuc=[] #quantidade total de dinucleotideo
        B= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for rec in SeqIO.parse(arq,"fasta"):
            seq_din = rec.seq    
            all_counts = [] #quantidade de dinucleotideo de cada sequencia
        
            for trinucleotide in trinucleotides:
                count = seq_din.count(trinucleotide)
                #print("count is " + str(count) + " for " + trinucleotide)
                all_counts.append(count)
            #print(all_counts)
            #print(con_trinuc)
            con_trinuc = list(map(sum, zip( all_counts, B)))
            B = con_trinuc
            #print(B)
            
        box=[]
        fig = plt.figure()
        ax1 =fig.add_subplot(1,1,1)
        
        ax1.set_xlabel("Trinucleotides")
        ax1.set_ylabel("Quantity")
        ax1.set_title("Trinucleotides of " + str(arq_f))
        
        
        for j in range(0, 23):
            box.append(ax1.bar(trinucleotides, con_trinuc, color = 'rgb' )) ##plot do boxplot
            
        
        fig.set_size_inches(18.5, 10.5)
        plt.show()