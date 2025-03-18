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