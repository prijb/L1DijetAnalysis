#This script runs preprocess_dataset.py over a bunch of datasets
import os

current_dir = os.getcwd()

#Dataset dictionary
dataset_dict = {
    "QCD_15to30":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/QCD_PT-15to30_regressed_leading/240909_124252/0000",
        "output": f"{current_dir}/outputs/QCD_15to30",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
    "QCD_30to50":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/QCD_PT-30to50_regressed_leading/240821_124954/0000",
        "output": f"{current_dir}/outputs/QCD_30to50",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
    "QCD_50to80":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/QCD_PT-50to80_regressed_leading/240821_125003/0000",
        "output": f"{current_dir}/outputs/QCD_50to80",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
    "QCD_80to120":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/QCD_PT-80to120_regressed_leading/240821_125013/0000",
        "output": f"{current_dir}/outputs/QCD_80to120",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
    "QCD_120to170":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/QCD_PT-120to170_regressed_leading/240821_125021/0000",
        "output": f"{current_dir}/outputs/QCD_120to170",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
    "QCD_170to300":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/QCD_PT-170to300_regressed_leading/240821_125029/0000",
        "output": f"{current_dir}/outputs/QCD_170to300",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
    "QCD_300to470":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/QCD_PT-300to470_regressed_leading/240822_154142/0000",
        "output": f"{current_dir}/outputs/QCD_300to470",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
    "QCD_470to600":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/QCD_PT-470to600_regressed_leading/240821_125045/0000",
        "output": f"{current_dir}/outputs/QCD_470to600",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
    "QCD_600to800":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/QCD_PT-600to800_regressed_leading/240821_125054/0000",
        "output": f"{current_dir}/outputs/QCD_600to800",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
    "QCD_800to1000":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/QCD_PT-800to1000_regressed_leading/240821_125104/0000",
        "output": f"{current_dir}/outputs/QCD_800to1000",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
    "QCD_1000to1400":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/QCD_PT-1000to1400_regressed_leading/240821_125113/0000",
        "output": f"{current_dir}/outputs/QCD_1000to1400",
        "use_grid": True,
        "nfiles": -1,
        "start": 0
    },
}

"""
dataset_dict = {
    "QCD_15to30":{
        "input": "store/user/ppradeep/L1Scouting/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/QCD_PT-15to30_regressed_leading/240909_124252/0000",
        "output": f"{current_dir}/outputs/QCD_15to30",
        "use_grid": True,
        "nfiles": 1,
        "start": 0
    }
}
"""

#Submit for each dataset
for key in dataset_dict.keys():
    print("Submitting for dataset: {}".format(key))
    dataset = dataset_dict[key]

    #Make the output directory if it doesn't exist
    os.makedirs(dataset["output"], exist_ok=True)
    
    command = ""
    if dataset["use_grid"]:
        command = "python3 {}/Preprocess/preprocess_dataset.py -i {} -o {} --grid -n {} -s {}".format(current_dir, dataset["input"], dataset["output"], dataset["nfiles"], dataset["start"])
    else:
        command = "python3 {}/Preprocess/preprocess_dataset.py -i {} -o {} -n {} -s {}".format(current_dir, dataset["input"], dataset["output"], dataset["nfiles"], dataset["start"])
    
    #command = "python3 {}/Preprocess/preprocess_dataset.py -i {} -o {} -g {} -n {} -s {}".format(current_dir, dataset["input"], dataset["output"], dataset["use_grid"], dataset["nfiles"], dataset["start"])

    os.system(command)

print("All datasets submitted!")
