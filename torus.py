from numpy import *
import matplotlib.pyplot as plt
R = 4
r = 1
u = linspace(0, 2 * pi, 100)
v = linspace(0, 2 * pi, 100)
u, v = meshgrid(u, v)

x = (R + r * cos(v)) * cos(u)
y = (R + r * cos(v)) * sin(u)
z = r * sin(v)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(
    x, y, z, color='y', rstride=5,
    cstride = 5, alpha = 0.7
)
ax.set_axis_off()
plt.show() 
