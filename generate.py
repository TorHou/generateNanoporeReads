import argparse
from Bio import SeqIO
from random import random, choice


parser = argparse.ArgumentParser()

parser.add_argument("input")
parser.add_argument("--error_rate", type = float, default = 0.18)
args = parser.parse_args()

def otherNt(nucleotide):
    other = ["A","C","G","T"]
    other.remove(nucleotide)
    return choice(other)

def generateNPRead(read):
    nts = ["A","C","G","T"]
    fuzzy_read = ""
    for letter in read:
        if random() > args.error_rate:
            fuzzy_read += letter
        else:
            mistake = random()
            if mistake > 0.667:
                fuzzy_read += otherNt(letter)
            elif mistake > 0.333:
                # add insert
                fuzzy_read += choice(nts)
                while random() < 0.333 * args.error_rate:
                    fuzzy_read += choice(nts)
                fuzzy_read += letter
    return fuzzy_read
            

for read in SeqIO.parse(args.input,"fasta"):
    #print(read.seq)
    print(">"+read.id)
    print(generateNPRead(read.seq))




