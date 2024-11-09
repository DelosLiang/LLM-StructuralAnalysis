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