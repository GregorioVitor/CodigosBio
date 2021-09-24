#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:25:40 2020

@author: gregorio
"""

import pandas as pd
import numpy as np

data = pd.DataFrame([['Portugal', 'Lisboa', 10000000, 2],
                ['Peru', 'Lima', 32000000, 1],
                ['Chile', 'Santiago', 18000000, 4],
                ['Brasil', 'Brasília', 209000000, 5]])

print(data)
cols = list(data.columns.values)

novo =[]


print(cols)


i =0
while i < len(cols):
    
    par = data[i]
    impar = data[i+1]

    
    i=i+2

    
    novo.append(impar)
    novo.append(par)

a = np.array(novo)

df = pd.DataFrame(a.T)
    
print(df)
