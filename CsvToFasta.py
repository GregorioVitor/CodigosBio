#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:15:54 2020

@author: gregorio
"""


import sys
import csv

csv.field_size_limit(sys.maxsize)
arquivo = open('/home/gregorio/Desktop/maize_DB.fasta', 'a+') # Abra o arquivo (leitura)
conteudo = arquivo.readlines()


with open('/home/gregorio/Desktop/maize_DB.csv', 'r') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv, delimiter=',')
    for coluna in leitor:
        print('>'+coluna['circName'])
        print(coluna['seq'])
        conteudo.append('\n>'+coluna['circName'])
        conteudo.append("\n"+ coluna['seq'])
        
        
        
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

arquivo.close()
