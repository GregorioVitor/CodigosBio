#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:38:33 2021

@author: gregorio
"""


#python3 GTF_filter.py -g CA_mrg_ftr.gtf -r CA_transc_rnaplonc_result_FILTER.txt -o result.gtf
#python3 GTF_filter.py -g CC_mrg_ftr.gtf -r stavCC_transc_rnaplonc_result_FILTER.txt -o stavCC_transc_rnaplonc_result_FILTER.gtf
#python3 GTF_filter.py -g CC_mrg_ftr.gtf -r stavCC_transc_rnaplonc_result_FILTER_90.txt -o stavCC_transc_rnaplonc_result_FILTER_90.gtf
#python3 GTF_filter.py -g CE_mrg_ftr2.gtf -r transcripts_CE2_rnaplonc_result_FILTER.txt -o transcripts_CE2_rnaplonc_result_FILTER.gtf
#python3 GTF_filter.py -g CE_mrg_ftr2.gtf -r transcripts_CE2_rnaplonc_result_FILTER_90.txt -o transcripts_CE2_rnaplonc_result_FILTER_90.gtf


import pandas as pd
import argparse

#pd.options.display.max_rows=900000
pd.options.display.max_columns=12


ap = argparse.ArgumentParser()
ap.add_argument("-g", "--gtfFile", required=True, help= "Path of the gtf file")
ap.add_argument("-r", "--resultFile", required=True, help= "Path of the result file, or the RNAplonc.model output")
ap.add_argument("-o", "--outputFile", required=True, help= "Path of the output file")
args = vars(ap.parse_args())


gtf_df = pd.read_csv(args["gtfFile"], sep='\t', header=None, comment='#' )
arq2 = pd.read_csv(args["resultFile"], sep= '\s+')
arq3 = open(args["outputFile"],"w")

gtf_df = gtf_df.rename(columns={0:'# SeqId', 1:'Source', 2:'type', 3:'start', 4:'end', 5:'score', 6:'strand', 7:'phase', 8:'attributes'})
gtf_df['transcript_id'] = gtf_df['attributes'].str.extract(r'transcript_id "(.*)"')

df_aux = arq2
df_aux.columns = ['transcript_id', 'predicted' , 'prediction']


#df_Final = pd.merge(arq2, gtf_df[['start', 'end', 'transcript_id']],on='transcript_id', how='left')
df_Final = pd.merge(gtf_df, df_aux[['transcript_id', 'prediction']], on='transcript_id', how='right')


#df_Final['attributes']= df_Final.agg('{0[attributes]}prediction "{0[prediction]}";'.format, axis=1)
df_Final['attributes'] = [''.join([x,'prediction "',str(round(y,4)),'";']) for x,y in zip(df_Final['attributes'], df_Final['prediction'])] 
df_Final = df_Final.drop(columns=['transcript_id', 'prediction'])

print(df_Final)

final = df_Final.to_csv(index=False, sep="\t")
arq3.write(final)
