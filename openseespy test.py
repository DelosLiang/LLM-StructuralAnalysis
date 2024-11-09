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

# Material properties dictionary for each element type
Ep = {1: [E, Acol, IzCol],
      2: [E, Acol, IzCol],
      3: [E, Agir, IzGir]}

# Define node coordinates
ops.node(1, 0., 0.)  # Node 1 at (0, 0)
ops.node(2, 0., colL)  # Node 2 at (0, column length)
ops.node(3, girL, 0.)  # Node 3 at (girder length, 0)
ops.node(4, girL, colL)  # Node 4 at (girder length, column length)

# Define boundary conditions (supports)
ops.fix(1, 1, 1, 1)  # Fix node 1 in all 3 DOFs (x, y, rotation)
ops.fix(3, 1, 1, 0)  # Fix node 3 in x and y, but allow rotation

# Plot the model before defining elements
opsv.plot_model()
plt.title('plot_model before defining elements')

# Define transformation type for elements (Linear)
ops.geomTransf('Linear', 1)

# Define column elements (elastic beam-column elements)
ops.element('elasticBeamColumn', 1, 1, 2, Acol, E, IzCol, 1)  # Element between nodes 1 and 2
ops.element('elasticBeamColumn', 2, 3, 4, Acol, E, IzCol, 1)  # Element between nodes 3 and 4

# Define girder element
ops.element('elasticBeamColumn', 3, 2, 4, Agir, E, IzGir, 1)  # Element between nodes 2 and 4

# External loads: point load at node 2, distributed load on element 3
Px = 2.e+3  # Axial load in the x-direction at node 2
Wy = -10.e+3  # Uniform distributed load in the y-direction on element 3
Wx = 0.  # Uniform distributed load in the x-direction on element 3

# Dictionary to store element loads
Ew = {3: ['-beamUniform', Wy, Wx]}  # Element 3 has a uniform distributed load

# Define time series and load pattern
ops.timeSeries('Constant', 1)  # Constant load pattern
ops.pattern('Plain', 1, 1)  # Apply pattern to load case 1
ops.load(2, Px, 0., 0.)  # Apply point load at node 2 (Px in x-direction)

# Apply distributed loads on elements
for etag in Ew:
    ops.eleLoad('-ele', etag, '-type', Ew[etag][0], Ew[etag][1], Ew[etag][2])

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