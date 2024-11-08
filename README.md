# L1 Dijet Analysis Framework

## Overview
Contains code for preprocessing, merging, weighting, plotting and fitting NTuples produced by the L1ScoutingAnalyzer

Analyse in the following steps
1. Preprocess dataset
2. Merge dataset
3. Weight dataset
4. Plot dataset

Requires CMSSW_14_1_0_pre4 and to run setup script

## Preprocessing
The `Preprocess` folder contains scripts which apply selections and weights to NTuples
* `preprocess_file.py`: Applies selections using RDataframes to a given NTuple. `preprocess_dataset` and `preprocess_datasets.py` are wrapper scripts for running on one and multiple datasets respectively
* `merge_outputs.py`: Merges preprocessed histograms into a single histogram for a given dataset defined in the script
* `scale_dataset.py`: Scales all the histograms in the file by a given cross seciton and luminosity. `scale_datasets` performs this for multiple datasets and merges into one file with weighted histograms

## WIP
Plotting and fitting code
