#This script merges the outputs of the preprocessed datasets 
#Specifically for QCD
import os
import argparse

current_dir = os.getcwd()

os.makedirs(f"{current_dir}/outputs/combined", exist_ok=True)

parser = argparse.ArgumentParser(description='Merge preprocessor outputs')
parser.add_argument('--isData', '-i', action="store_true", help='Is it data?')

args = parser.parse_args()


#Dataset dictionary (MC)
dataset_dict = None

if not args.isData:
    print("Merging MC datasets")
    dataset_dict = {
        "QCD_15to30":{
            "input_directory": f"{current_dir}/outputs/QCD_15to30",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd15to30"
        },
        "QCD_30to50":{
            "input_directory": f"{current_dir}/outputs/QCD_30to50",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd30to50"
        },
        "QCD_50to80":{
            "input_directory": f"{current_dir}/outputs/QCD_50to80",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd50to80"
        },
        "QCD_80to120":{
            "input_directory": f"{current_dir}/outputs/QCD_80to120",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd80to120"
        },
        "QCD_120to170":{
            "input_directory": f"{current_dir}/outputs/QCD_120to170",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd120to170"
        },
        "QCD_170to300":{
            "input_directory": f"{current_dir}/outputs/QCD_170to300",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd170to300"
        },
        "QCD_300to470":{
            "input_directory": f"{current_dir}/outputs/QCD_300to470",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd300to470"
        },
        "QCD_470to600":{
            "input_directory": f"{current_dir}/outputs/QCD_470to600",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd470to600"
        },
        "QCD_600to800":{
            "input_directory": f"{current_dir}/outputs/QCD_600to800",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd600to800"
        },
        "QCD_800to1000":{
            "input_directory": f"{current_dir}/outputs/QCD_800to1000",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd800to1000"
        },
        "QCD_1000to1400":{
            "input_directory": f"{current_dir}/outputs/QCD_1000to1400",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_qcd1000to1400"
        }
    }

else:
    print("Merging Data")
    dataset_dict = {
        "Data":{
            "input_directory": f"{current_dir}/outputs/Data",
            "output_directory": f"{current_dir}/outputs/combined",
            "input_name": "processed_output",
            "output_name": "processed_output_data"
        }
    }


#Combine the files
for key in dataset_dict.keys():
    print("Combining files for dataset: {}".format(key))
    dataset = dataset_dict[key]
    
    #Commands
    command_events = f"hadd -f {dataset['output_directory']}/{dataset['output_name']}.root $(ls {dataset['input_directory']}/{dataset['input_name']}_*.root | grep -v 'hist.root')"
    command_hist = f"hadd -f {dataset['output_directory']}/{dataset['output_name']}_hist.root {dataset['input_directory']}/{dataset['input_name']}_*hist.root"

    #Execute the commands
    os.system(command_hist)
    #os.system(command_events)