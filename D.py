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
# Node coordinates   
ops.node(1, 0, 0)  # Node 1 at (0, 0)
ops.node(2, 0, colL)  # Node 2 at (0, colL)
ops.node(3, 0, 2*colL) # Node 3 at (0, 2*colL)
ops.node(4, girL, 0)  # Node 4 at (girL, 0)
ops.node(5, girL, colL) # Node 5 at (girL, colL)
ops.node(6, girL, 2*colL) # Node 6 at (girL, 2*colL)

# Boundary conditions (supports)
ops.fix(1, 1, 1, 1)  # Fix all 3 DOFs (x, y, rotation) for node 1
ops.fix(4, 1, 1, 1)  # Fix all 3 DOFs (x, y, rotation) for node 4

# Transformation type for elements (Linear)
ops.geomTransf('Linear', 1)  # Transformation ID 1 for linear transformation 

# Element definition (elastic beam-column elements)
ops.element('elasticBeamColumn', 1, 1, 2, Acol, E, IzCol, 1)  # Column element 1 between nodes 1 and 2
ops.element('elasticBeamColumn', 2, 2, 3, Acol, E, IzCol, 1)  # Column element 2 between nodes 2 and 3
ops.element('elasticBeamColumn', 3, 4, 5, Acol, E, IzCol, 1)  # Column element 3 between nodes 4 and 5
ops.element('elasticBeamColumn', 4, 5, 6, Acol, E, IzCol, 1)  # Column element 4 between nodes 5 and 6
ops.element('elasticBeamColumn', 5, 2, 5, Agir, E, IzGir, 1)  # Girder element 5 between nodes 2 and 5
ops.element('elasticBeamColumn', 6, 3, 6, Agir, E, IzGir, 1)  # Girder element 6 between nodes 3 and 6

# Global loads
Px = 2e3  # Point load in the x-direction
opsv.plot_model()
plt.title('plot_model before defining loads')

# Apply point load Px at node 2 and 3 in the x-direction
ops.load(2, Px, 0.0, 0.0)  # Px applied in x-direction, no load in y and rotation for node 2
ops.load(3, Px, 0.0, 0.0)  # Px applied in x-direction, no load in y and rotation for node 3

# Element loads
Wy, Wx = -10e3, 0.0  # Uniform loads in y and x directions
Ew = {5: ['-beamUniform', Wy, Wx],  
       6: ['-beamUniform', Wy, Wx]}  # element 5 and 6 have uniform distributed load

# Apply distributed loads on elements
for etag in Ew:
    ops.eleLoad('-ele', etag, '-type', Ew[etag][0], Ew[etag][1], Ew[etag][2])
# Post-processing

# Analysis settings
ops.constraints('Transformation')  # Apply transformation constraints
ops.numberer('RCM')  # Renumber the nodes using Reverse Cuthill-McKee (RCM)
ops.system('BandGeneral')  # Define the solution algorithm
ops.test('NormDispIncr', 1.0e-6, 6, 2)  # Convergence test criteria
ops.algorithm('Linear')  # Use linear algorithm for solving
ops.integrator('LoadControl', 1)  # Control load increments
ops.analysis('Static')  # Define a static analysis
ops.analyze(1)  # Perform the analysis

# Print the model data
ops.printModel()

# Plot the model after defining elements
opsv.plot_model()
plt.title('plot_model after defining elements')

# Plot the applied loads on the model in 2D
opsv.plot_loads_2d(nep=10,  # Number of points along each element
                   sfac=1,  # Scale factor for loads
                   fig_wi_he=(10, 5),  # Width and height of the figure
                   fig_lbrt=(0.1, 0.1, 0.9, 0.9),  # Left, bottom, right, top margins
                   fmt_model_loads={'color': 'red', 'linewidth': 1.5},  # Formatting for load arrows
                   node_supports=True,  # Display node supports
                   truss_node_offset=0.05,  # Offset for truss elements
                   ax=None)  # Matplotlib axis, None to use current axis

# Plot deformations (scaled) after analysis
opsv.plot_defo()
# Optional: plot deformations with a scale factor
# opsv.plot_defo(sfac)

# Optional: customize plot format for deformation visualization
# fmt_interp = {'color': 'blue', 'linestyle': 'solid', 'linewidth': 1.2, 'marker': '.', 'markersize': 6}
# opsv.plot_defo(sfac, fmt_interp=fmt_interp)

# Plot internal force diagrams: N (axial), V (shear), M (moment)
sfacN, sfacV, sfacM = 5.e-5, 5.e-5, 5.e-5  # Scale factors for internal force diagrams

# Plot axial force distribution
opsv.section_force_diagram_2d('N', sfacN)
plt.title('Axial force distribution')

# Plot shear force distribution
opsv.section_force_diagram_2d('T', sfacV)
plt.title('Shear force distribution')

# Plot bending moment distribution
opsv.section_force_diagram_2d('M', sfacM)
plt.title('Bending moment distribution')

# Show all plots
plt.show()

# Exit the program
exit()