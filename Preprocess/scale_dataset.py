#This script takes a preprocessed file and weights the histograms by a given cross section and luminosity
import ROOT
import os
import argparse

#Argument parser
parser = argparse.ArgumentParser(description='Scale histograms of preprocessed L1 Scouting files')
parser.add_argument('--input', '-i', type=str, help='Input file path')
parser.add_argument('--output', '-o', type=str, help='Output file path')
parser.add_argument('--lumi', '-l', default=100, type=float, help='Integrated luminosity to scale')
parser.add_argument('--xs', '-x', default=1, type=float, help='Process xs')

args = parser.parse_args()

#File input
fname = args.input
oname = args.output
lumi = args.lumi
xs = args.xs

#Load the histogram file
f = ROOT.TFile(fname, "READ")
f_keys = f.GetListOfKeys()
f_keynames = [key.GetName() for key in f_keys]
histos_to_scale = [f.Get(keyname) for keyname in f_keynames if "h_" in keyname]

#Get the number of events
n_entries = f.Get("n_entries").GetVal()

#Open the output file
fout = ROOT.TFile(oname, "RECREATE")

for histo in histos_to_scale:
    histo.Sumw2()
    #MC case
    if ((lumi > 0)&(xs > 0)):
        histo.Scale((lumi*xs)/n_entries)

    histo.Write()

fout.Close()