from simnibs import sim_struct, run_simnibs, mni2subject_coords

#Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '75_Guys.msh'
# Output folder
s.pathfem = 'perigray1_75/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_75_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '76_Guys.msh'
# Output folder
s.pathfem = 'perigray1_76/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_76_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)


# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '77_Guys.msh'
# Output folder
s.pathfem = 'perigray1_77/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_77_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '78_Guys.msh'
# Output folder
s.pathfem = 'perigray1_78/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_78_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '84_Guys.msh'
# Output folder
s.pathfem = 'perigray1_84/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_84_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '85_Guys.msh'
# Output folder
s.pathfem = 'perigray1_85/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_85_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '86_Guys.msh'
# Output folder
s.pathfem = 'perigray1_86/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_86_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '87_Guys.msh'
# Output folder
s.pathfem = 'perigray1_87/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_87_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '88_Guys.msh'
# Output folder
s.pathfem = 'perigray1_88/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_88_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '89_Guys.msh'
# Output folder
s.pathfem = 'perigray1_89/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_89_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '90_Guys.msh'
# Output folder
s.pathfem = 'perigray1_90/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_90_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '91_Guys.msh'
# Output folder
s.pathfem = 'perigray1_91/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_91_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '98_Guys.msh'
# Output folder
s.pathfem = 'perigray1_98/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_98_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '99_Guys.msh'
# Output folder
s.pathfem = 'perigray1_99/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_99_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = 'IXI496.msh'
# Output folder
s.pathfem = 'perigray1IXI496/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-81.9, -31.4, -33], 'm2m_IXI496')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)


#Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '75_Guys.msh'
# Output folder
s.pathfem = 'perigray2_75/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_75_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '76_Guys.msh'
# Output folder
s.pathfem = 'perigray2_76/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_76_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)


# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '77_Guys.msh'
# Output folder
s.pathfem = 'perigray2_77/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_77_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '78_Guys.msh'
# Output folder
s.pathfem = 'perigray2_78/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_78_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '84_Guys.msh'
# Output folder
s.pathfem = 'perigray2_84/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_84_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '85_Guys.msh'
# Output folder
s.pathfem = 'perigray2_85/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_85_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '86_Guys.msh'
# Output folder
s.pathfem = 'perigray2_86/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_86_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '87_Guys.msh'
# Output folder
s.pathfem = 'perigray2_87/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_87_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '88_Guys.msh'
# Output folder
s.pathfem = 'perigray2_88/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_88_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '89_Guys.msh'
# Output folder
s.pathfem = 'perigray2_89/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_89_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '90_Guys.msh'
# Output folder
s.pathfem = 'perigray2_90/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_90_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '91_Guys.msh'
# Output folder
s.pathfem = 'perigray2_91/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_91_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '98_Guys.msh'
# Output folder
s.pathfem = 'perigray2_98/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_98_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '99_Guys.msh'
# Output folder
s.pathfem = 'perigray2_99/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_99_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = 'IXI496.msh'
# Output folder
s.pathfem = 'perigray2IXI496/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([51.22, -42.6, -47.6], 'm2m_IXI496')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)


#Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '75_Guys.msh'
# Output folder
s.pathfem = 'fornix1_75/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_75_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '76_Guys.msh'
# Output folder
s.pathfem = 'fornix1_76/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_76_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)


# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '77_Guys.msh'
# Output folder
s.pathfem = 'fornix1_77/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_77_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '78_Guys.msh'
# Output folder
s.pathfem = 'fornix1_78/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_78_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '84_Guys.msh'
# Output folder
s.pathfem = 'fornix1_84/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_84_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '85_Guys.msh'
# Output folder
s.pathfem = 'fornix1_85/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_85_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '86_Guys.msh'
# Output folder
s.pathfem = 'fornix1_86/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_86_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '87_Guys.msh'
# Output folder
s.pathfem = 'fornix1_87/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_87_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '88_Guys.msh'
# Output folder
s.pathfem = 'fornix1_88/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_88_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '89_Guys.msh'
# Output folder
s.pathfem = 'fornix1_89/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_89_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '90_Guys.msh'
# Output folder
s.pathfem = 'fornix1_90/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_90_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '91_Guys.msh'
# Output folder
s.pathfem = 'fornix1_91/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_91_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '98_Guys.msh'
# Output folder
s.pathfem = 'fornix1_98/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_98_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '99_Guys.msh'
# Output folder
s.pathfem = 'fornix1_99/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_99_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = 'IXI496.msh'
# Output folder
s.pathfem = 'fornix1IXI496/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-56.6, 11.18, 66.13], 'm2m_IXI496')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)


#Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '75_Guys.msh'
# Output folder
s.pathfem = 'fornix2_75/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_75_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '76_Guys.msh'
# Output folder
s.pathfem = 'fornix2_76/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_76_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)


# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '77_Guys.msh'
# Output folder
s.pathfem = 'fornix2_77/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_77_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '78_Guys.msh'
# Output folder
s.pathfem = 'fornix2_78/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_78_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '84_Guys.msh'
# Output folder
s.pathfem = 'fornix2_84/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_84_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '85_Guys.msh'
# Output folder
s.pathfem = 'fornix2_85/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_85_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '86_Guys.msh'
# Output folder
s.pathfem = 'fornix2_86/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_86_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '87_Guys.msh'
# Output folder
s.pathfem = 'fornix2_87/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_87_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '88_Guys.msh'
# Output folder
s.pathfem = 'fornix2_88/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_88_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '89_Guys.msh'
# Output folder
s.pathfem = 'fornix2_89/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_89_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '90_Guys.msh'
# Output folder
s.pathfem = 'fornix2_90/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_90_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '91_Guys.msh'
# Output folder
s.pathfem = 'fornix2_91/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_91_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '98_Guys.msh'
# Output folder
s.pathfem = 'fornix2_98/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_98_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = '99_Guys.msh'
# Output folder
s.pathfem = 'fornix2_99/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_99_Guys')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)

# Initalize a session
s = sim_struct.SESSION()
# Name of head mesh
s.fnamehead = 'IXI496.msh'
# Output folder
s.pathfem = 'fornix2IXI496/'

# Initialize a list of TMS simulations
tmslist = s.add_tmslist()
# Select coil
tmslist.fnamecoil = 'No9_H1.nii.gz'

# Initialize a coil position
pos = tmslist.add_position()
# Select coil centre
pos.centre = mni2subject_coords([-47.5, 14.07, 73.99], 'm2m_IXI496')
# Select coil direction
pos.pos_ydir = 'CP1'
pos.didt = 200e6

run_simnibs(s)
