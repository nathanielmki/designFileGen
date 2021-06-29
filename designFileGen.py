import pandas as pd
import numpy as np
import argparse
import sys
import os
import csv
import re
import string

# This program takes an unfiltered metadata file downloaded from NCBI as input, and converts it to a usable design file

def pandasConversion(infile, outfile, delim=','):
    # Use pandas to convert CSV file from NCBI to reduced and formatted TSV file

    #parser = argparse.ArgumentParser(description='Load file for modification.')
    #parser.add_argument('csvfile', type=argparse.FileType('r'), help='input file')
    #args = parser.parse_args()
    df = pd.read_csv(infile, sep=",")
    if 'Replicate' not in df:
        df['Replicate'] = 'R'
    if 'Time' not in df:
        df['Time'] = np.nan
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = map(str.lower, df.columns)
    df = df.rename(columns={'run': 'sample'})
    df = df.rename(columns={'time': 'time_dpa'})
    df2 = df.replace(r' ', '_', regex=True)
    df_final=df2[['sample', 'replicate', 'time_dpa', 'dev_stage']]
    df_final.to_csv(outfile, sep='\t', encoding='utf-8')


def inputVerification(parsed_args):
    # Check if input file exists, throw warning if it does not
    infile = parsed_args.infile
    if not os.path.isfile(parsed_args.infile):
        print("The input file %s does not exist, quitting." %
              parsed_args.infile)
        sys.exit()

    # Auto-generate an output file name based upon checked input
    if parsed_args.outfile == '':
        outfile = infile.split('.')[-2] + '.design.txt'
    else:
        outfile = parsed_args.outfile

    return infile, outfile


def main():
    # Definitions for input and output files
    parser = argparse.ArgumentParser(
        description='Load SRA metadata table for conversion.')

    parser.add_argument("-i", "--infile", required=True, dest="infile",
                        help="Input SraRunTable, downloaded from NCBI SRA Run Selector")

    parser.add_argument("-o", "--outfile", dest="outfile",
                        help="Output filename, should end in '.design.txt'.")

    infile, outfile = inputVerification(parser.parse_args())

    pandasConversion(infile, outfile)


if __name__ == '__main__':
    main()
