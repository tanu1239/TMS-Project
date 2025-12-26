from simnibs.msh import mesh_io
from simnibs import sim_struct, run_simnibs
import numpy as np
import pickle

n_cpu = 10

# ### General Information
S = sim_struct.SESSION()

mesh = 'firstmshtrial.msh'
S.fnamehead = mesh  # head mesh
S.pathfem = 'tms_optimization/'  # Directory for the simulation

# ## Define the TMS simulation
tms = S.add_tmslist()

tms.fnamecoil = 'No9_H1.nii.gz'

# get coil position at start position

pos = tms.add_position()
pos.centre = [18.167,  9.373, -5.34]

pos.distance = 1


print("prepare")
# mesh = mesh_io.read_msh(mesh)
# mesh.fix_surface_labels()
mesh = pickle.load(open("firstmshtrial.msh",'rb'))

print("calc matsimnibs")
mat = pos.calc_matsimnibs(mesh)  # get skull coil position for cortex target
# TODO: magic here to get coil positions




