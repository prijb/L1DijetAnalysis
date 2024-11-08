#This script runs scale_datasets.py over a bunch of datasets and then merges them
import os

current_dir = os.getcwd()

script = f"{current_dir}/Preprocess/scale_dataset.py"
output_dir = f"{current_dir}/outputs/scaled"

os.makedirs(output_dir, exist_ok=True)

#Dictionary of MC pT bins
pt_bins_dict = {
    #Using XSecAnalyzer (13.6 TeV xs and 2023 conditions)
    #"QCD_15to30":{
    #    "input": f"{current_dir}/outputs/combined/processed_output_qcd15to30_hist.root",
    #    "output": f"{output_dir}/scaled_qcd15to30.root",
    #    "lumi": 45.0,
    #    "xs": 1.306e9
    #},
    #The rest use 13.6 TeV xs and 2024 conditions
    "QCD_30to50":{
        "input": f"{current_dir}/outputs/combined/processed_output_qcd30to50_hist.root",
        "output": f"{output_dir}/scaled_qcd30to50.root",
        "lumi": 45.0,
        "xs": 1.126e8
    },
    "QCD_50to80":{
        "input": f"{current_dir}/outputs/combined/processed_output_qcd50to80_hist.root",
        "output": f"{output_dir}/scaled_qcd50to80.root",
        "lumi": 45.0,
        "xs": 1.669e7
    },
    "QCD_80to120":{
        "input": f"{current_dir}/outputs/combined/processed_output_qcd80to120_hist.root",
        "output": f"{output_dir}/scaled_qcd80to120.root",
        "lumi": 45.0,
        "xs": 2.506e6
    },
    "QCD_120to170":{
        "input": f"{current_dir}/outputs/combined/processed_output_qcd120to170_hist.root",
        "output": f"{output_dir}/scaled_qcd120to170.root",
        "lumi": 45.0,
        "xs": 4.404e5
    },
    "QCD_170to300":{
        "input": f"{current_dir}/outputs/combined/processed_output_qcd170to300_hist.root",
        "output": f"{output_dir}/scaled_qcd170to300.root",
        "lumi": 45.0,
        "xs": 1.13e5
    },
    "QCD_300to470":{
        "input": f"{current_dir}/outputs/combined/processed_output_qcd300to470_hist.root",
        "output": f"{output_dir}/scaled_qcd300to470.root",
        "lumi": 45.0,
        "xs": 7.572e3
    },
    "QCD_470to600":{
        "input": f"{current_dir}/outputs/combined/processed_output_qcd470to600_hist.root",
        "output": f"{output_dir}/scaled_qcd470to600.root",
        "lumi": 45.0,
        "xs": 6.224e2
    },
    "QCD_600to800":{
        "input": f"{current_dir}/outputs/combined/processed_output_qcd600to800_hist.root",
        "output": f"{output_dir}/scaled_qcd600to800.root",
        "lumi": 45.0,
        "xs": 1.788e2
    },
    "QCD_800to1000":{
        "input": f"{current_dir}/outputs/combined/processed_output_qcd800to1000_hist.root",
        "output": f"{output_dir}/scaled_qcd800to1000.root",
        "lumi": 45.0,
        "xs": 3.054e1
    },
    "QCD_1000to1400":{
        "input": f"{current_dir}/outputs/combined/processed_output_qcd1000to1400_hist.root",
        "output": f"{output_dir}/scaled_qcd1000to1400.root",
        "lumi": 45.0,
        "xs": 8.899
    }
}

#Run scale_histograms.py over each MC pT bin
for pt_bin in pt_bins_dict.keys():
    print("Scaling histograms for", pt_bin)
    os.system(f"python3 {script} --input {pt_bins_dict[pt_bin]['input']} --output {pt_bins_dict[pt_bin]['output']} --lumi {pt_bins_dict[pt_bin]['lumi']} --xs {pt_bins_dict[pt_bin]['xs']}")

#Then hadd the scaled histos
scaled_histos = ""
for pt_bin in pt_bins_dict.keys():
    scaled_histos += f"{pt_bins_dict[pt_bin]['output']} "
    
os.system("hadd -f {}/scaled_qcd.root {}".format(output_dir, scaled_histos))