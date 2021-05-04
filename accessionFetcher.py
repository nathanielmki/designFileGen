import argparse
import sys
import os
import csv
import re
import string
from Bio import Entrez

# This program takes in an BioProject string ID, and downloads the appropriate SraRunTable metadata file

# Maybe use snakemake???

def main():
    # Definitions for argparse arguments
    parser = argparse.ArgumentParser(
        description='Provide BioProject ID to acquire SRA metadata file')
    
    parser.add_argument("-i", "--id", required=True, dest="id",
                    help="Bioproject ID, acquired from an SRA query or publication reference")

if __name__ == '__main__':
    main()