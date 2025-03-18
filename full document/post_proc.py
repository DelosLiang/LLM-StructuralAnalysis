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