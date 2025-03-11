import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.autolayout"] = True
plt.rcParams["figure.figsize"] = (8, 11)

file = np.loadtxt("flowdata.txt", delimiter='\t')
im = plt.imread("PaperFundyDiagram.png")
im2 = plt.imread("CloseUp.png")

column1 = file[:, 0]
column2 = file[:, 1]

aspect_ratio = im.shape[1] / im.shape[0]
aspect_ratio2 = im2.shape[1] / im2.shape[0]

print(im.shape)
print(im2.shape)

indices = np.where(column1 == 0.0)[0]
indices2 = np.where(column1 == 0.8)[0]


""" plt.imshow(im, extent=[-2.51, 9.5, -1, 5.08], alpha=1.0, aspect=aspect_ratio)
plt.plot(column1[indices[1]:indices2[1]+1]*10, column2[indices[1]:indices2[1]+1]
         * 10, label="Average in $10^6$ timesteps", color="r", linestyle="dashed")
plt.scatter(column1[:indices2[0]]*10, column2[:indices2[0]]
            * 10, s=5, label="Averaged in $10^2$ timesteps", color="r")
# plt.xlim([0, im.shape[1]])
# plt.ylim([im.shape[0], 0])
plt.axis("off")
plt.gca().set_aspect('equal')
plt.savefig("OverlayedPlot1.png")
plt.show() """



#plt.imshow(im2, extent=[-2.5, 8.5, -1.4, 5.0], alpha=1.0, aspect=aspect_ratio2, origin="upper")
plt.scatter(column1[indices[0]:indices2[0]]*10, column2[indices[0]:indices2[0]]*10,
            label="Average in $10^6$ timesteps", color="r", facecolors="none")
plt.axis("off")
plt.ylim(2.6,3.4)
plt.xlim(0.4, 1.78)
plt.gca().set_aspect('equal')
plt.savefig("OverlayedPlot2.png", transparent = True)
plt.show()


""" plt.scatter(column1[:indices2[0]]*10, column2[:indices2[0]]*10, s = 5, label = "Averaged in $10^2$ timesteps", color = "k")
plt.plot(column1[indices[1]:indices2[1]+1]*10, column2[indices[1]:indices2[1]+1]*10, label = "Average in $10^6$ timesteps", color = "k") 
plt.xlabel("Density [cars per site]")
plt.ylabel("Flow [cars per time step]")
plt.xticks(np.arange(0, 9, 2.0))
plt.yticks(np.arange(0, 4.5, 1.0))
plt.ylim(0,4.5)
plt.xlim(0,8)
plt.tick_params(axis="y", direction = "in", left = True, right = True, length = 7)
plt.tick_params(axis = "x", direction = "in", bottom = True, top = True, length = 7)
plt.tick_params(axis = "x", which = "minor", direction = "in", bottom = True, top = True, length = 3)
plt.tick_params(axis = "y", which = "minor", direction = "in", left = True, right = True, length = 3)
plt.minorticks_on()
plt.title("Simulation")
plt.legend()
plt.savefig("FundamentalDiagram.png")
plt.show() """

""" #plt.scatter(column1[:indices2[0]]*10, column2[:indices2[0]]*10, s = 5, label = "Averaged in $10^2$ timesteps", color = "k")
plt.scatter(column1[indices[1]:indices2[1]], column2[indices[1]:indices2[1]], label = "Average in $10^6$ timesteps", color = "k")
plt.xlabel("Density [cars per site]")
plt.ylabel("Flow [cars per time step]")
plt.ylim(0.26,0.34)
plt.xlim(0.04, 0.16)
plt.tick_params(axis="y", direction = "in", left = True, right = True, length = 7)
plt.tick_params(axis = "x", direction = "in", bottom = True, top = True, length = 7)
plt.tick_params(axis = "x", which = "minor", direction = "in", bottom = True, top = True, length = 3)
plt.tick_params(axis = "y", which = "minor", direction = "in", left = True, right = True, length = 3)
plt.title("Simulation")
plt.legend()
plt.savefig("ZoomedIn.png")
plt.show() """
