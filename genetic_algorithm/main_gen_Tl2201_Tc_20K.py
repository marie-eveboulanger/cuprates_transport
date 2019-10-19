import numpy as np
import random
from copy import deepcopy
import genetic_utils as utils
from genetic import genetic_search
import os
##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

init_member = {
    "bandname": "HolePocket",
    "a": 5.46,
    "b": 5.46,
    "c": 23.2,
    "t": 200,
    "tp": 0.22,
    "tpp": -0.11,
    "tz": 0.07,
    "tz2": 0.00,
    "mu": -0.406,
    "fixdoping": -2,
    "numberOfKz": 7,
    "mesh_ds": 1 / 20,
    "T": 0,
    "Bamp": 45,
    "Btheta_min": 0,
    "Btheta_max": 90,
    "Btheta_step": 5,
    "Bphi_array": [0, 20, 28, 36, 44],
    "gamma_0": 15,
    "gamma_k": 0,
    "gamma_dos_max": 0,
    "power": 12,
    "factor_arcs": 1,
    "seed": 72,
    "data_T": 4.2,
    "data_p": 0.25,
}


ranges_dict = {
    "t": [100.0,500.0],
    "tp": [0.20,0.24],
    "tpp": [-0.13,-0.09],
    "tz": [0.01,0.12],
    "mu": [-0.85,-0.3],
    "gamma_0": [5,30],
    "gamma_k": [10,100],
    "power":[1, 20],
    # "gamma_dos_max": [10.0,300.0],
    # "factor_arcs" : [1, 300],
}

# ## Data Nd-LSCO 0.24  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# data_dict = {}  # keys (T, phi), content [filename, theta, rzz, theta_cut]
# data_dict[25, 0] = ["../data_NdLSCO_0p25/0p25_0degr_45T_25K.dat", 0, 1, 90]
# data_dict[25, 15] = ["../data_NdLSCO_0p25/0p25_15degr_45T_25K.dat", 0, 1, 90]
# data_dict[25, 30] = ["../data_NdLSCO_0p25/0p25_30degr_45T_25K.dat", 0, 1, 90]
# data_dict[25, 45] = ["../data_NdLSCO_0p25/0p25_45degr_45T_25K.dat", 0, 1, 90]

# data_dict[20, 0] = ["../data_NdLSCO_0p25/0p25_0degr_45T_20K.dat", 0, 1, 90]
# data_dict[20, 15] = ["../data_NdLSCO_0p25/0p25_15degr_45T_20K.dat", 0, 1, 90]
# data_dict[20, 30] = ["../data_NdLSCO_0p25/0p25_30degr_45T_20K.dat", 0, 1, 90]
# data_dict[20, 45] = ["../data_NdLSCO_0p25/0p25_45degr_45T_20K.dat", 0, 1, 90]

# data_dict[12, 0] = ["../data_NdLSCO_0p25/0p25_0degr_45T_12K.dat", 0, 1, 83.5]
# data_dict[12, 15] = ["../data_NdLSCO_0p25/0p25_15degr_45T_12K.dat", 0, 1, 83.5]
# data_dict[12, 45] = ["../data_NdLSCO_0p25/0p25_45degr_45T_12K.dat", 0, 1, 83.5]

# data_dict[6, 0] = ["../data_NdLSCO_0p25/0p25_0degr_45T_6K.dat", 0, 1, 73.5]
# data_dict[6, 15] = ["../data_NdLSCO_0p25/0p25_15degr_45T_6K.dat", 0, 1, 73.5]
# data_dict[6, 45] = ["../data_NdLSCO_0p25/0p25_45degr_45T_6K.dat", 0, 1, 73.5]


## Data Nd-LSCO 0.21  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
data_dict = {}  # keys (T, phi), content [filename, theta, rzz, theta_cut]
data_dict[4.2, 0] = ["../data/Tl2201_Tc_20K_Hussey_2003/rhozz_vs_theta_Tl2201_Tc_20K_B45_T4.2K_phi_0.dat", 0, 1, 80]
data_dict[4.2, 20] = ["../data/Tl2201_Tc_20K_Hussey_2003/rhozz_vs_theta_Tl2201_Tc_20K_B45_T4.2K_phi_20.dat", 0, 1, 80]
data_dict[4.2, 28] = ["../data/Tl2201_Tc_20K_Hussey_2003/rhozz_vs_theta_Tl2201_Tc_20K_B45_T4.2K_phi_28.dat", 0, 1, 80]
data_dict[4.2, 36] = ["../data/Tl2201_Tc_20K_Hussey_2003/rhozz_vs_theta_Tl2201_Tc_20K_B45_T4.2K_phi_36.dat", 0, 1, 80]
data_dict[4.2, 44] = ["../data/Tl2201_Tc_20K_Hussey_2003/rhozz_vs_theta_Tl2201_Tc_20K_B45_T4.2K_phi_44.dat", 0, 1, 80]


# Play
genetic_search(init_member,ranges_dict, data_dict, folder="../sim/Tl2201_Tc_20K",
                population_size=120, N_generation=50, mutation_s=0.1, crossing_p=0.9)


# utils.save_member_to_json(init_member, folder="../data_NdLSCO_0p25")
# member = utils.load_member_from_json(
#     "../data_NdLSCO_0p25",
#     "data_p0.24_T25.0_fit_p0.250_B45_t262.1_mu-0.877_tp-0.151_tpp0.075_tz0.068_tzz0.000_LargePocket_gzero17.8_gdos0.0_gk0.0_pwr12.0"
# )
# utils.fig_compare(init_member, data_dict, folder="../sim/Tl2201_Tc_20K")



# class ObjectView():
#     def __init__(self,dictionary):
#         self.__dict__.update(dictionary)