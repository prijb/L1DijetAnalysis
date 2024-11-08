#This script compares the data and MC for the distributions produced in the Preprocess module
import os
import uproot
import hist
from hist.intervals import ratio_uncertainty
import numpy as np
import scipy as sp
#Plotting (with mplhep)
import matplotlib.pyplot as plt
import mplhep as hep
plt.style.use(hep.style.CMS)
plt.rcParams["figure.figsize"] = (12.5, 10)

current_dir = os.getcwd()

#Open files
f_data = uproot.open(f"{current_dir}/outputs/combined/processed_output_data_hist.root")
#f_qcd_15to30 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd15to30.root")
f_qcd_30to50 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd30to50.root")
f_qcd_50to80 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd50to80.root")
f_qcd_80to120 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd80to120.root")
f_qcd_120to170 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd120to170.root")
f_qcd_170to300 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd170to300.root")
f_qcd_300to470 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd300to470.root")
f_qcd_470to600 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd470to600.root")
f_qcd_600to800 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd600to800.root")
f_qcd_800to1000 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd800to1000.root")
f_qcd_1000to1400 = uproot.open(f"{current_dir}/outputs/scaled/scaled_qcd1000to1400.root")

#Define a plotting function for the data-MC comparison
def plot_hist(dict_data, dict_mc, title=None):
    tot_data = sum(dict_data['hists'])
    tot_mc = sum(dict_mc['hists'])

    fig, axs = plt.subplots(2, 1, gridspec_kw=dict(height_ratios=[3, 1], hspace=0.1), sharex=True)
    hep.histplot(dict_mc['hists'], ax=axs[0], stack=True, histtype='fill', color=dict_mc['col_list'], label=dict_mc['label_list'], flow=None, density=False)
    hep.histplot(dict_data['hists'], ax=axs[0], histtype='errorbar', color='black', label='Data', flow=None, density=False)
    axs[0].legend(fontsize=14, ncol=2)
    if dict_data["yscale_log"]:
        axs[0].set_yscale('log')
    axs[0].set_xlabel('')
    axs[0].set_ylabel(dict_data['ylabel'])

    #Plot the ratio
    errps = {'hatch':'////', 'facecolor':'none', 'lw': 0, 'edgecolor': 'k', 'alpha': 0.5}
    mc_rel_err = np.sqrt(tot_mc.variances())/(tot_mc.values())
    hep.histplot(tot_data.values()/tot_mc.values(), tot_data.axes[0].edges, yerr=np.sqrt(tot_data.variances())/tot_data.values(), ax=axs[1], histtype='errorbar', color='black', label='Data/MC')
    axs[1].stairs(1+mc_rel_err, baseline=1-mc_rel_err, edges=tot_mc.axes[0].edges, **errps)
    axs[1].axhline(1, color='black', linestyle='--')
    axs[1].set_ylim(0.0, 2.0)
    axs[1].set_ylabel('Data/MC')
    axs[1].set_xlabel(dict_data['xlabel'])
    '$m_{jj}$ [GeV]'
    hep.cms.label(data=True, llabel="Private Work", rlabel=r"Level-1 Scouting 2024, 45 $\mathrm{pb^{-1}}$", ax=axs[0])
    plt.savefig(f"{current_dir}/plots/{title}.png")


#Common plotting params
label_list_data = ['Data']
#label_list_mc = ['15-30 GeV', '30-50 GeV', '50-80 GeV', '80-120 GeV', '120-170 GeV', '170-300 GeV', '300-470 GeV', '470-600 GeV', '600-800 GeV', '800-1000 GeV', '1000-1400 GeV']
label_list_mc = ['30-50 GeV', '50-80 GeV', '80-120 GeV', '120-170 GeV', '170-300 GeV', '300-470 GeV', '470-600 GeV', '600-800 GeV', '800-1000 GeV', '1000-1400 GeV']

col_list_data = ['black']
col_list_mc = ["#3f90da", "#ffa90e", "#bd1f01", "#94a4a2", "#832db6", "#a96b59", "#e76300", "#b9ac70", "#717581", "#92dadd"]

#SR
#hists_data_sr = [f_data["h_mjj_sig"].to_hist()]
#hists_mc_sr = [f_qcd_30to50["h_mjj_sig"].to_hist(), f_qcd_50to80["h_mjj_sig"].to_hist(), f_qcd_80to120["h_mjj_sig"].to_hist(), f_qcd_120to170["h_mjj_sig"].to_hist(), f_qcd_170to300["h_mjj_sig"].to_hist(), f_qcd_300to470["h_mjj_sig"].to_hist(), f_qcd_470to600["h_mjj_sig"].to_hist(), f_qcd_600to800["h_mjj_sig"].to_hist(), f_qcd_800to1000["h_mjj_sig"].to_hist(), f_qcd_1000to1400["h_mjj_sig"].to_hist()]
#dict_data_sr = {'hists':hists_data_sr, 'label_list':label_list_data, 'col_list':col_list_data,'yscale_log':True, 'ylabel':'Events/5 GeV', 'xlabel':'$m_{jj}$ [GeV]', 'title':'data_mc_comparison_sr'}
#dict_mc_sr = {'hists':hists_mc_sr, 'label_list':label_list_mc, 'col_list':col_list_mc, 'yscale_log':True, 'ylabel':'Events/5 GeV', 'xlabel':'$m_{jj}$ [GeV]', 'title':'data_mc_comparison_sr'}

#SR bins divided by 2
hists_data_sr = [(f_data["h_mjj_sig"].to_hist())[::2j]]
hists_mc_sr = [(f_qcd_30to50["h_mjj_sig"].to_hist())[::2j], (f_qcd_50to80["h_mjj_sig"].to_hist())[::2j], (f_qcd_80to120["h_mjj_sig"].to_hist())[::2j], (f_qcd_120to170["h_mjj_sig"].to_hist())[::2j], (f_qcd_170to300["h_mjj_sig"].to_hist())[::2j], (f_qcd_300to470["h_mjj_sig"].to_hist())[::2j], (f_qcd_470to600["h_mjj_sig"].to_hist())[::2j], (f_qcd_600to800["h_mjj_sig"].to_hist())[::2j], (f_qcd_800to1000["h_mjj_sig"].to_hist())[::2j], (f_qcd_1000to1400["h_mjj_sig"].to_hist())[::2j]]
dict_data_sr = {'hists':hists_data_sr, 'label_list':label_list_data, 'col_list':col_list_data,'yscale_log':True, 'ylabel':'Events/10 GeV', 'xlabel':'$m_{jj}$ [GeV]', 'title':'data_mc_comparison_sr'}
dict_mc_sr = {'hists':hists_mc_sr, 'label_list':label_list_mc, 'col_list':col_list_mc, 'yscale_log':True, 'ylabel':'Events/10 GeV', 'xlabel':'$m_{jj}$ [GeV]', 'title':'data_mc_comparison_sr'}


#dEta 
hists_data_deta = [(f_data["h_deta"].to_hist())[::3j]]
hists_mc_deta = [(f_qcd_30to50["h_deta"].to_hist())[::3j], (f_qcd_50to80["h_deta"].to_hist())[::3j], (f_qcd_80to120["h_deta"].to_hist())[::3j], (f_qcd_120to170["h_deta"].to_hist())[::3j], (f_qcd_170to300["h_deta"].to_hist())[::3j], (f_qcd_300to470["h_deta"].to_hist())[::3j], (f_qcd_470to600["h_deta"].to_hist())[::3j], (f_qcd_600to800["h_deta"].to_hist())[::3j], (f_qcd_800to1000["h_deta"].to_hist())[::3j], (f_qcd_1000to1400["h_deta"].to_hist())[::3j]]
dict_data_deta = {'hists':hists_data_deta, 'label_list':label_list_data, 'col_list':col_list_data, 'yscale_log':True, 'ylabel':'Events/0.3', 'xlabel':'$\Delta\eta_{jj}$', 'title':'data_mc_comparison_deta'}
dict_mc_deta = {'hists':hists_mc_deta, 'label_list':label_list_mc, 'col_list':col_list_mc, 'yscale_log':True, 'ylabel':'Events/0.3', 'xlabel':'$\Delta\eta_{jj}$', 'title':'data_mc_comparison_deta'}


#Plot 
plot_hist(dict_data_sr, dict_mc_sr, "data_mc_comparison_sr")
plot_hist(dict_data_deta, dict_mc_deta, "data_mc_comparison_deta")
