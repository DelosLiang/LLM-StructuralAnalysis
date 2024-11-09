from openseespy.opensees import *

# Define the model
model('basic', '-ndm', 2, '-ndf', 2)

# Define nodes
node(1, 0, 0)
node(2, 4, 0)
node(3, 2, 4)

# Define elements
element('elasticBeamColumn', 1, 1, 2, 20,000000000000000000000., 1.6e-05, 2e-03)
element('elasticBeamColumn', 2, 2, 3, 20,000000000000000000000., 1.6e-05, 2e-03)
element('elasticBeamColumn', 3, 3, 1, 20,000000000000000000000., 5.4e-05, 6e-03)

# Define boundary condition
fix(1, 1, 1)
fix(2, 1, 1)

# Define loads
pattern('Plain')
load(1, -2000, 0)
load(3, 0, -10000)

# Perform analysis
analysis('Static')

# Print results
print('Displacements:')
for i in range(1, 4):
    print('Node', i, ':', disp(i))

print('Reactions:')
for i in range(1, 3):
    print('Support', i, ':', reaction(i))