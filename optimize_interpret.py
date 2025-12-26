import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
from nibabel.affines import apply_affine
import numpy.linalg as npl

scaling_affine = np.array([[-3.87167655e-01,  6.94654902e-01, 6.06263783e-01, -54.5319739e+01]
                            [ 8.65854948e-01,  4.99901587e-01, -1.98396448e-02, -14.6180111e+01]
                            [-3.16853934e-01,  5.17255227e-01, -7.95016110e-01,  101.787764e+02]
                            [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])
print(scaling_affine)
M = scaling_affine[:3, :3]
abc = scaling_affine[:3, 3]
stimulation= (-43.4, -20.7, 83.4)
def f(i, j, k):
   """ Return X, Y, Z coordinates for i, j, k """
   return M.dot([i, j, k]) + abc
epi_vox_center = (np.array(stimulation))
print(scaling_affine.dot(list(epi_vox_center) + [1]))
print(f(epi_vox_center[0], epi_vox_center[1], epi_vox_center[2]))
print(apply_affine(scaling_affine, epi_vox_center))



