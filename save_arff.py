#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 02:28:35 2020

@author: gregorio
"""


from Bio import SeqIO
import pandas as pd
import numpy as np
import arff
from Bio.SeqUtils import GC

class save_arff:
    def __init__(self, lista, arq_f):
        width = []
        gc_cont = []
        name =[]
        
        nucleotideos =['A','C','G','T']
        GC_ratio = []
        con_nuc=[]
        #tam = len(arq[aux])
        
        for rec in SeqIO.parse(lista,"fasta"):
            seq_nuc = rec.seq    
            all_counts = [] #quantidade de nucleotideo de cada sequencia
            for nucleotide in nucleotideos:
                count = seq_nuc.count(nucleotide)
                all_counts.append(count)            
            GC_ratio.append(round((all_counts[0]+all_counts[3])/(all_counts[1]+all_counts[2]),4))
        
            width.append(len(rec))
            width_seq = np.array(width)
            name.append(rec.id)
            gc_cont.append(round(GC(rec.seq),4))
            gc_cont_seq = np.array(gc_cont)
            GC_ratio_seq = np.array(GC_ratio)
            
        data = np.array([name, width_seq, gc_cont_seq, GC_ratio_seq]).T
        
        df = pd.DataFrame(data, columns = ['Seq Name','Width', 'GC Content', 'GC Ratio'])
        
        print(df)
        
        arff.dump('result '+ arq_f +'.arff', df.values, relation = 'relation name', names = ['Seq Name','Width', 'GC Content', 'GC Ratio'])    
            
        con_nuc.append(GC_ratio)
        GC_ratio_list = [] 