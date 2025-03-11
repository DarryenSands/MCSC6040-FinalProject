import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

# Rain Plotting Code && Speed Limit Code

""" roadSection = np.loadtxt("roaddata.txt", dtype=str)

s = '\n'.join(str(x) for x in roadSection)

empty_val = -1

velocities4 = np.array([[empty_val if c == '.' else int(c) for c in line.strip()] for line in s.split('\n')])

# Create a figure and axes object
fig, ax = plt.subplots()

# Invert the y-axis to show time increasing downward
ax.invert_yaxis()

# Plot the velocity data as a space-time diagram
im1 = ax.imshow(velocities4[:101, :], cmap='Greys', origin='upper', vmin=-1, vmax=5, aspect='auto', interpolation="None") 

plt.colorbar(im1)
# Add labels and titles
ax.set_xlabel('Space (Road)')
ax.set_ylabel('Time')
# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none') # tick markers
ax.yaxis.set_ticks_position('none')
ax.set_title('Space-Time Diagram of Traffic Flow')

plt.savefig("RoadValuesSpeedLimit.png", bbox_inches = "tight")

# Show the plot
plt.show()  """

plt.rcParams["figure.autolayout"] = True
plt.rcParams["figure.figsize"] = (8, 11)

file = np.loadtxt("flowdata.txt", delimiter='\t')
im = plt.imread("RainDiagram.png")

aspect_ratio = im.shape[1] / im.shape[0]

column1 = file[:, 0]
column2 = file[:, 1]

indicesc = np.where(column1 == 0.0)[0]
indicesc2 = np.where(column1 == 0.8)[0]


plt.imshow(im, extent=[-2.51, 9.5, -1, 5.08], alpha=1.0, aspect=aspect_ratio)
#plt.plot(column1[indicesc[0]:indicesc2[0]]*10, column2[indicesc[0]:indicesc2[0]]
#         * 10, label="Average in $10^6$ timesteps", color="r", linestyle="dashed")
plt.plot(column1[indicesc[1]:indicesc2[1]]*10, column2[indicesc[1]:indicesc2[1]]
         * 10, label="Average in $10^6$ timesteps", color="r", linestyle="dashed")
plt.axis("off")
#plt.savefig("ComboDiagram.png", bbox_inches = "tight")
#plt.savefig("SectionDiagram.png", bbox_inches = "tight")
#plt.savefig("RainDiagram.png", bbox_inches = "tight")
plt.show()

""" file2 = np.loadtxt("velocitydata.txt", delimiter='\t')


densities = file2[:, 0]
averageVelocities = file2[:, 1]

indices = np.where(densities == 0.005)[0]
indices2 = np.where(densities == 0.8)[0]

plt.plot(densities[indices[0]:indices2[0]], averageVelocities[indices[0]:indices2[0]], label="Average velocities in 10^6 timesteps without speed limit")
plt.plot(densities[indices[1]:indices2[1]], averageVelocities[indices[1]:indices2[1]], label="Average velocities in 10^6 timesteps with speed limit")
plt.ylabel("Average Velocity")
plt.xlabel("Density")
plt.legend()
plt.savefig(f"AverageVelocityDiagram{sys.argv[1]}.png", bbox_inches="tight")
plt.show() """