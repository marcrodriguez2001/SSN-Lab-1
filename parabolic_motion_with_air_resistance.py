#
# Example parabolic motion
#

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt
 
#
# FUNCTION DRAW A TRAJECTORY FOR PARABOLIC MOTION
# Input: velocity and angle 
#
def draw_trajectory(u, theta):
    #convert angle in degrees to rad
    theta = np.radians(theta)
    #gravity acceleration in m/s^2
    g = 9.8
    # Time of flight
    t_flight = (100*(1/b)*np.log(1+(b*u*np.sin(theta))/g))
    # find time intervals
    intervals = np.arange(0, t_flight, 0.001)
    # create an empty list of x and y coordinates
    x = []
    y = []
    #Do a loop over time calculating the coordinates
    for t in intervals:
        y.append((1/b)*((g/b)+u*np.sin(theta))*(1-np.exp(-b*t))-(g/b)*t)
        x.append((u*np.cos(theta)/b)*(1-np.exp(-b*t)))
        if  y[-1]<0:
            break
    #Plot the results
    plt.plot(x, y)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile motion with air friction')

#--------------------------------------------------------------------------------
# Main Program: give specific values and call to the function draw_trajectory
#--------------------------------------------------------------------------------

print("Parabolic motion of a projectile\n")

#Ask the user for angle
print("Enter desired launch angle in degrees (recommended 45 degrees):")
theta=float(input())

# Ask the user for initial velocity
print("Enter desired launch initial velocity in m/s:")
u=float(input())

#Ask the user for b parameter
print("Enter desired launch friction coefficient in s^-1(recommended values between 0 and 1):")
b=float(input())

#Graph
draw_trajectory(u, theta)

        
# Add a legend and show the graph
plt.legend(["angle:"+str(theta)+"º  \ninitial velocity:"+str(u)+" m/s\nb:"+str(b)+" s^-1"])
plt.show()
