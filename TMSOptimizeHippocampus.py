from simnibs import opt_struct, mni2subject_coords

tms_opt56_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt56_HH.fnamehead = 'IXI56_HH.msh'
### Select output folder
tms_opt56_HH.pathfem = 'hippocampusIXI56_HHH1/'
### Select coil model
tms_opt56_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt56_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI56_HH')
### pardiso solver
tms_opt56_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI56_HH = tms_opt56_HH.run()

tms_opt57_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt57_HH.fnamehead = 'IXI57_HH.msh'
### Select output folder
tms_opt57_HH.pathfem = 'hippocampusIXI57_HHH1/'
### Select coil model
tms_opt57_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt57_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI57_HH')
### pardiso solver
tms_opt57_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI57_HH = tms_opt57_HH.run()

tms_opt59_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt59_HH.fnamehead = 'IXI59_HH.msh'
### Select output folder
tms_opt59_HH.pathfem = 'hippocampusIXI59_HHH1/'
### Select coil model
tms_opt59_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt59_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI59_HH')
### pardiso solver
tms_opt59_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI59_HH = tms_opt59_HH.run()

tms_opt67_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt67_HH.fnamehead = 'IXI67_HH.msh'
### Select output folder
tms_opt67_HH.pathfem = 'hippocampusIXI67_HHH1/'
### Select coil model
tms_opt67_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt67_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI67_HH')
### pardiso solver
tms_opt67_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI67_HH = tms_opt67_HH.run()

tms_opt72_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt72_HH.fnamehead = 'IXI72_HH.msh'
### Select output folder
tms_opt72_HH.pathfem = 'hippocampusIXI72_HHH1/'
### Select coil model
tms_opt72_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt72_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI72_HH')
### pardiso solver
tms_opt72_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI72_HH = tms_opt72_HH.run()

tms_opt79_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt79_HH.fnamehead = 'IXI79_HH.msh'
### Select output folder
tms_opt79_HH.pathfem = 'hippocampusIXI79_HHH1/'
### Select coil model
tms_opt79_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt79_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI79_HH')
### pardiso solver
tms_opt79_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI79_HH = tms_opt79_HH.run()

------------------------------------------

tms_opt80_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt80_HH.fnamehead = 'IXI80_HH.msh'
### Select output folder
tms_opt80_HH.pathfem = 'hippocampusIXI80_HHH1/'
### Select coil model
tms_opt80_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt80_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI80_HH')
### pardiso solver
tms_opt80_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI80_HH = tms_opt80_HH.run()

tms_opt83_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt83_HH.fnamehead = 'IXI83_HH.msh'
### Select output folder
tms_opt83_HH.pathfem = 'hippocampusIXI83_HHH1/'
### Select coil model
tms_opt83_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt83_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI83_HH')
### pardiso solver
tms_opt83_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI83_HH = tms_opt83_HH.run()

tms_opt92_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt92_HH.fnamehead = 'IXI92_HH.msh'
### Select output folder
tms_opt92_HH.pathfem = 'hippocampusIXI92_HHH1/'
### Select coil model
tms_opt92_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt92_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI92_HH')
### pardiso solver
tms_opt92_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI92_HH = tms_opt92_HH.run()



tms_opt93_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt93_HH.fnamehead = 'IXI93_HH.msh'
### Select output folder
tms_opt93_HH.pathfem = 'hippocampusIXI93_HHH1/'
### Select coil model
tms_opt93_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt93_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI93_HH')
### pardiso solver
tms_opt93_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI93_HH = tms_opt93_HH.run()




tms_opt94_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt94_HH.fnamehead = 'IXI94_HH.msh'
### Select output folder
tms_opt94_HH.pathfem = 'hippocampusIXI94_HHH1/'
### Select coil model
tms_opt94_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt94_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI94_HH')
### pardiso solver
tms_opt94_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI94_HH = tms_opt94_HH.run()



tms_opt95_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt95_HH.fnamehead = 'IXI95_HH.msh'
### Select output folder
tms_opt95_HH.pathfem = 'hippocampusIXI95_HHH1/'
### Select coil model
tms_opt95_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt95_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI95_HH')
### pardiso solver
tms_opt95_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI95_HH = tms_opt95_HH.run()


tms_opt96_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt96_HH.fnamehead = 'IXI96_HH.msh'
### Select output folder
tms_opt96_HH.pathfem = 'hippocampusIXI96_HHH1/'
### Select coil model
tms_opt96_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt96_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI96_HH')
### pardiso solver
tms_opt96_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI96_HH = tms_opt96_HH.run()


tms_opt97_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt97_HH.fnamehead = 'IXI97_HH.msh'
### Select output folder
tms_opt97_HH.pathfem = 'hippocampusIXI97_HHH1/'
### Select coil model
tms_opt97_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt97_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI97_HH')
### pardiso solver
tms_opt97_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI97_HH = tms_opt97_HH.run()


tms_opt559_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt559_HH.fnamehead = 'IXI559_HH.msh'
### Select output folder
tms_opt559_HH.pathfem = 'hippocampusIXI559_HHH1/'
### Select coil model
tms_opt559_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt559_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI559_HH')
### pardiso solver
tms_opt559_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI559_HH = tms_opt559_HH.run()


tms_opt565_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt565_HH.fnamehead = 'IXI565_HH.msh'
### Select output folder
tms_opt565_HH.pathfem = 'hippocampusIXI565_HHH1/'
### Select coil model
tms_opt565_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt565_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI565_HH')
### pardiso solver
tms_opt565_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI565_HH = tms_opt565_HH.run()

-------------------------------
tms_opt566_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt566_HH.fnamehead = 'IXI566_HH.msh'
### Select output folder
tms_opt566_HH.pathfem = 'hippocampusIXI566_HHH1/'
### Select coil model
tms_opt566_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt566_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI566_HH')
### pardiso solver
tms_opt566_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI566_HH = tms_opt566_HH.run()


tms_opt567_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt567_HH.fnamehead = 'IXI567_HH.msh'
### Select output folder
tms_opt567_HH.pathfem = 'hippocampusIXI567_HHH1/'
### Select coil model
tms_opt567_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt567_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI567_HH')
### pardiso solver
tms_opt567_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI567_HH = tms_opt567_HH.run()



tms_opt568_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt568_HH.fnamehead = 'IXI568_HH.msh'
### Select output folder
tms_opt568_HH.pathfem = 'hippocampusIXI568_HHH1/'
### Select coil model
tms_opt568_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt568_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI568_HH')
### pardiso solver
tms_opt568_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI568_HH = tms_opt568_HH.run()


tms_opt572_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt572_HH.fnamehead = 'IXI572_HH.msh'
### Select output folder
tms_opt572_HH.pathfem = 'hippocampusIXI572_HHH1/'
### Select coil model
tms_opt572_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt572_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI572_HH')
### pardiso solver
tms_opt572_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI572_HH = tms_opt572_HH.run()


tms_opt575_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt575_HH.fnamehead = 'IXI575_HH.msh'
### Select output folder
tms_opt575_HH.pathfem = 'hippocampusIXI575_HHH1/'
### Select coil model
tms_opt575_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt575_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI575_HH')
### pardiso solver
tms_opt575_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI575_HH = tms_opt575_HH.run()



tms_opt577_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt577_HH.fnamehead = 'IXI577_HH.msh'
### Select output folder
tms_opt577_HH.pathfem = 'hippocampusIXI577_HHH1/'
### Select coil model
tms_opt577_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt577_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI577_HH')
### pardiso solver
tms_opt577_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI577_HH = tms_opt577_HH.run()


tms_opt598_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt598_HH.fnamehead = 'IXI598_HH.msh'
### Select output folder
tms_opt598_HH.pathfem = 'hippocampusIXI598_HHH1/'
### Select coil model
tms_opt598_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt598_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI598_HH')
### pardiso solver
tms_opt598_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI598_HH = tms_opt598_HH.run()


tms_opt599_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt599_HH.fnamehead = 'IXI599_HH.msh'
### Select output folder
tms_opt599_HH.pathfem = 'hippocampusIXI599_HHH1/'
### Select coil model
tms_opt599_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt599_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI599_HH')
### pardiso solver
tms_opt599_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI599_HH = tms_opt599_HH.run()


tms_opt600_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt600_HH.fnamehead = 'IXI600_HH.msh'
### Select output folder
tms_opt600_HH.pathfem = 'hippocampusIXI600_HHH1/'
### Select coil model
tms_opt600_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt600_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI600_HH')
### pardiso solver
tms_opt600_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI600_HH = tms_opt600_HH.run()


tms_opt601_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt601_HH.fnamehead = 'IXI601_HH.msh'
### Select output folder
tms_opt601_HH.pathfem = 'hippocampusIXI601_HHH1/'
### Select coil model
tms_opt601_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt601_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI601_HH')
### pardiso solver
tms_opt601_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI601_HH = tms_opt601_HH.run()


tms_opt603_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt603_HH.fnamehead = 'IXI603_HH.msh'
### Select output folder
tms_opt603_HH.pathfem = 'hippocampusIXI603_HHH1/'
### Select coil model
tms_opt603_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt603_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI603_HH')
### pardiso solver
tms_opt603_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI603_HH = tms_opt603_HH.run()


tms_opt605_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt605_HH.fnamehead = 'IXI605_HH.msh'
### Select output folder
tms_opt605_HH.pathfem = 'hippocampusIXI605_HHH1/'
### Select coil model
tms_opt605_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt605_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI605_HH')
### pardiso solver
tms_opt605_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI605_HH = tms_opt605_HH.run()


tms_opt606_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt606_HH.fnamehead = 'IXI606_HH.msh'
### Select output folder
tms_opt606_HH.pathfem = 'hippocampusIXI606_HHH1/'
### Select coil model
tms_opt606_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt606_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI606_HH')
### pardiso solver
tms_opt606_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI606_HH = tms_opt606_HH.run()


tms_opt608_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt608_HH.fnamehead = 'IXI608_HH.msh'
### Select output folder
tms_opt608_HH.pathfem = 'hippocampusIXI608_HHH1/'
### Select coil model
tms_opt608_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt608_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI608_HH')
### pardiso solver
tms_opt608_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI608_HH = tms_opt608_HH.run()


tms_opt609_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt609_HH.fnamehead = 'IXI609_HH.msh'
### Select output folder
tms_opt609_HH.pathfem = 'hippocampusIXI609_HHH1/'
### Select coil model
tms_opt609_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt609_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI609_HH')
### pardiso solver
tms_opt609_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI609_HH = tms_opt609_HH.run()


tms_opt610_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt610_HH.fnamehead = 'IXI610_HH.msh'
### Select output folder
tms_opt610_HH.pathfem = 'hippocampusIXI610_HHH1/'
### Select coil model
tms_opt610_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt610_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI610_HH')
### pardiso solver
tms_opt610_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI610_HH = tms_opt610_HH.run()

tms_opt611_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt611_HH.fnamehead = 'IXI611_HH.msh'
### Select output folder
tms_opt611_HH.pathfem = 'hippocampusIXI611_HHH1/'
### Select coil model
tms_opt611_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt611_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI611_HH')
### pardiso solver
tms_opt611_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI611_HH = tms_opt611_HH.run()

tms_opt612_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt612_HH.fnamehead = 'IXI612_HH.msh'
### Select output folder
tms_opt612_HH.pathfem = 'hippocampusIXI612_HHH1/'
### Select coil model
tms_opt612_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt612_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI612_HH')
### pardiso solver
tms_opt612_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI612_HH = tms_opt612_HH.run()

tms_opt613_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt613_HH.fnamehead = 'IXI613_HH.msh'
### Select output folder
tms_opt613_HH.pathfem = 'hippocampusIXI613_HHH1/'
### Select coil model
tms_opt613_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt613_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI613_HH')
### pardiso solver
tms_opt613_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI613_HH = tms_opt613_HH.run()

tms_opt614_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt614_HH.fnamehead = 'IXI614_HH.msh'
### Select output folder
tms_opt614_HH.pathfem = 'hippocampusIXI614_HHH1/'
### Select coil model
tms_opt614_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt614_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI614_HH')
### pardiso solver
tms_opt614_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI614_HH = tms_opt614_HH.run()

tms_opt631_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt631_HH.fnamehead = 'IXI631_HH.msh'
### Select output folder
tms_opt631_HH.pathfem = 'hippocampusIXI631_HHH1/'
### Select coil model
tms_opt631_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt631_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI631_HH')
### pardiso solver
tms_opt631_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI631_HH = tms_opt631_HH.run()

tms_opt632_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt632_HH.fnamehead = 'IXI632_HH.msh'
### Select output folder
tms_opt632_HH.pathfem = 'hippocampusIXI632_HHH1/'
### Select coil model
tms_opt632_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt632_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI632_HH')
### pardiso solver
tms_opt632_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI632_HH = tms_opt632_HH.run()

tms_opt633_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt633_HH.fnamehead = 'IXI633_HH.msh'
### Select output folder
tms_opt633_HH.pathfem = 'hippocampusIXI633_HHH1/'
### Select coil model
tms_opt633_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt633_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI633_HH')
### pardiso solver
tms_opt633_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI633_HH = tms_opt633_HH.run()

tms_opt634_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt634_HH.fnamehead = 'IXI634_HH.msh'
### Select output folder
tms_opt634_HH.pathfem = 'hippocampusIXI634_HHH1/'
### Select coil model
tms_opt634_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt634_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI634_HH')
### pardiso solver
tms_opt634_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI634_HH = tms_opt634_HH.run()

tms_opt635_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt635_HH.fnamehead = 'IXI635_HH.msh'
### Select output folder
tms_opt635_HH.pathfem = 'hippocampusIXI635_HHH1/'
### Select coil model
tms_opt635_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt635_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI635_HH')
### pardiso solver
tms_opt635_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI635_HH = tms_opt635_HH.run()

tms_opt636_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt636_HH.fnamehead = 'IXI636_HH.msh'
### Select output folder
tms_opt636_HH.pathfem = 'hippocampusIXI636_HHH1/'
### Select coil model
tms_opt636_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt636_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI636_HH')
### pardiso solver
tms_opt636_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI636_HH = tms_opt636_HH.run()

tms_opt637_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt637_HH.fnamehead = 'IXI637_HH.msh'
### Select output folder
tms_opt637_HH.pathfem = 'hippocampusIXI637_HHH1/'
### Select coil model
tms_opt637_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt637_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI637_HH')
### pardiso solver
tms_opt637_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI637_HH = tms_opt637_HH.run()

tms_opt638_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt638_HH.fnamehead = 'IXI638_HH.msh'
### Select output folder
tms_opt638_HH.pathfem = 'hippocampusIXI638_HHH1/'
### Select coil model
tms_opt638_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt638_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI638_HH')
### pardiso solver
tms_opt638_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI638_HH = tms_opt638_HH.run()

tms_opt643_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt643_HH.fnamehead = 'IXI643_HH.msh'
### Select output folder
tms_opt643_HH.pathfem = 'hippocampusIXI643_HHH1/'
### Select coil model
tms_opt643_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt643_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI643_HH')
### pardiso solver
tms_opt643_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI643_HH = tms_opt643_HH.run()

tms_opt646_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt646_HH.fnamehead = 'IXI646_HH.msh'
### Select output folder
tms_opt646_HH.pathfem = 'hippocampusIXI646_HHH1/'
### Select coil model
tms_opt646_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt646_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI646_HH')
### pardiso solver
tms_opt646_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI646_HH = tms_opt646_HH.run()
#
tms_opt661_HH = opt_struct.TMSoptimize()
### Select head mesh
tms_opt661_HH.fnamehead = 'IXI661_HH.msh'
### Select output folder
tms_opt661_HH.pathfem = 'hippocampusIXI661_HHH1/'
### Select coil model
tms_opt661_HH.fnamecoil = 'No9_H1.nii.gz'
### Select a target for the optimization
tms_opt661_HH.target = mni2subject_coords([-29.85, -24.27, -21.85], 'm2m_IXI661_HH')
### pardiso solver
tms_opt661_HH.solver_options = 'pardiso'
### Run optimization to get optimal coil position
opt_posIXI661_HH = tms_opt661_HH.run()