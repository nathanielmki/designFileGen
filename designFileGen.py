import pandas as pd
import argparse
import sys, os
import csv
import re
import string
import numpy as np
import openpyxl

# Primarily meant to convert SRA metadata records into a workable design file

def designFileGen():
    parser = argparse.ArgumentParser(description='Load file for modification.')
    parser.add_argument('csvfile', type=argparse.FileType('r'), help='input file')
    args = parser.parse_args()

    df = pd.read_csv(args.csvfile, sep=",")
    #df.drop(columns=df.columns[0],axis=1, inplace=True)
    df.columns = df.columns.str.replace(' ','_')
    df.columns = map(str.lower, df.columns)
    df = df.rename(columns={'run': 'sample'})
    df = df.rename(columns={'time': 'time_dpa'})
    df2 = df.replace(r' ','_', regex=True)
    df2.to_csv('bowdoin.gryllus_PRJNA647692.design.txt', sep='\t', encoding='utf-8')
#TODO: Build in editing of filename output

if __name__ == '__main__':
    designFileGen()
