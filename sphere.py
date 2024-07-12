from numpy import *
import matplotlib.pyplot as plt

phi, theta = mgrid[
    0.0:2.0 * pi:100j, 0.0:pi:50j
]
x = sin(theta) * cos(phi)
y = sin(theta) * sin(phi)
z = cos(theta)

fig = plt.figure()
ax = fig.add_subplot(
    111, projection = '3d'
)
ax.plot_surface(
    x, y, z, color='b', alpha = 0.6
)
ax.set_axis_off()
plt.show() 