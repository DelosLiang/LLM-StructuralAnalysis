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
# Define the material property dictionary for columns and girders
Ep = {
    1: [2e11, 2e-3, 1.6e-5],  # Element 1 is a column
    2: [2e11, 2e-3, 1.6e-5],  # Element 2 is a column
    3: [2e11, 6e-3, 5.4e-5]   # Element 3 is a girder
}

# Define the node coordinates
ops.node(1, 0, 0)          # Node 1 at (0, 0)
ops.node(2, 0, 4.0)        # Node 2 at (0, 4.0)
ops.node(3, 6.0, 0)        # Node 3 at (6.0, 0)
ops.node(4, 6.0, 4.0)      # Node 4 at (6.0, 4.0)

# Define boundary conditions (supports)
ops.fix(1, 1, 1, 1)  # Fix all 3 DOFs (x, y, rotation) for node 1
ops.fix(3, 1, 1, 1)  # Fix all 3 DOFs (x, y, rotation) for node 3

# Plot the model before defining elements
opsv.plot_model()
# Add title
plt.title('plot_model before defining elements')

# Define transformation type for elements (Linear)
ops.geomTransf('Linear', 1)

# Define column and girder elements (elastic beam-column elements)
ops.element('elasticBeamColumn', 1, 1, 2, 2e-3, 2e11, 1.6e-5, 1)  # Column element 1
ops.element('elasticBeamColumn', 2, 3, 4, 2e-3, 2e11, 1.6e-5, 1)  # Column element 2
ops.element('elasticBeamColumn', 3, 2, 4, 6e-3, 2e11, 5.4e-5, 1)  # Girder element

# Define external loads
Px = 2e3     # Point load in x-direction
Wy = -1e4    # Uniform load in y-direction
Wx = 0.0     # Uniform load in x-direction

# Create a dictionary to store element loads
Ew = {
    3: ['-beamUniform', Wy, Wx]  # Element 3 has a uniform distributed load
}

# Define time series for constant loads
ops.timeSeries('Constant', 1)
# Define load pattern using the constant time series
ops.pattern('Plain', 1, 1)

# Applying point loads
ops.load(2, Px, 0.0, 0.0)  # Px applied in x-direction at node 2

# Applying distributed loads
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