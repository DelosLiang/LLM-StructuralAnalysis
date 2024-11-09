# Parameters configuration

import openseespy.opensees as ops  # Import OpenSeesPy for structural analysis
import opsvis as opsv  # Import opsvis for visualization
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

ops.wipe()  # Clear any existing model
ops.model('basic', '-ndm', 2, '-ndf', 3)  # Define a 2D model with 3 degrees of freedom per node (DOF)

# Column and girder lengths
colL, girL = 4., 6.

# Section properties: cross-sectional area (A) and moment of inertia (Iz)
Acol, Agir = 2.e-3, 6.e-3
IzCol, IzGir = 1.6e-5, 5.4e-5

# Young's modulus (E)
E = 200.e9

# Define time series for constant loads
ops.timeSeries('Constant', 1)

# Define load pattern using the constant time series
ops.pattern('Plain', 1, 1)