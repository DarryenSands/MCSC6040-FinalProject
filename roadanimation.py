import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

otherdatastr = np.loadtxt("roaddata.txt", dtype=str)

s = "\n".join(str(x) for x in otherdatastr)
#print(s)
empty_val = -1
velocities2 = np.array([[empty_val if c == '.' else int(c) for c in line.strip()] for line in s.split('\n')])
#print(velocities2)


# Define the function that updates the plot for each frame of the animation
def update(frame):
    # Clear the plot
    ax.clear()
    ax.axis("off")
    # Get the velocities for the current frame
    current_velocities = velocities2[frame-1:frame+1,:]
    # Display the values directly in the plot using the imshow function
    im = ax.imshow(current_velocities, cmap='Greys', origin='upper', interpolation='nearest', vmin=np.min(velocities2), vmax=np.max(velocities2))
    
    # Add labels and titles
    """ ax.set_xlabel('Vehicle Position')
    ax.set_ylabel('Time')
    ax.set_title('Space-Time Diagram of Traffic Flow') """
    
    # Invert the y-axis to show time increasing downward
    ax.invert_yaxis()

# Create a figure and axes object
fig, ax = plt.subplots()


# Create the animation object
anim = ani.FuncAnimation(fig, update, frames=velocities2.shape[0], interval=100, repeat = True, repeat_delay = 1000)

anim.save("test.mp4", writer = 'ffmpeg')
