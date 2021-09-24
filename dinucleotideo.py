#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 01:29:11 2020

@author: gregorio
"""
from Bio import SeqIO
import matplotlib.pyplot as plt

class Dinucle:
    def __init__(self, arq, arq_f):
        dinucleotides = ['AA','AT','AG','AC',
                         'TA','TT','TG','TC',
                         'GA','GT','GG','GC',
                         'CA','CT','CG','CC']
        
        con_dinuc=[] #quantidade total de dinucleotideo
        B= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for rec in SeqIO.parse(arq,"fasta"):
            seq_din = rec.seq    
            all_counts = [] #quantidade de dinucleotideo de cada sequencia
        
            for dinucleotide in dinucleotides:
                count = seq_din.count(dinucleotide)
                #print("count is " + str(count) + " for " + dinucleotide)
                all_counts.append(count)
            #print(all_counts)
            #print(con_dinuc)
            con_dinuc = list(map(sum, zip( all_counts, B)))
            B = con_dinuc
            #print(B)
            
        box=[]
        fig = plt.figure()
        ax1 =fig.add_subplot(1,1,1)
        
        ax1.set_xlabel("Dinucleotides")
        ax1.set_ylabel("Quantity")
        ax1.set_title("Dinucleotides of " + str(arq_f))
        
        
        for j in range(0, 15):
            box.append(ax1.bar(dinucleotides, con_dinuc, color = 'rgb' )) ##plot do boxplot
            
        
        fig.set_size_inches(18.5, 10.5)
        plt.show()
        
        
    