from numpy import *
import matplotlib.pyplot as plt

def cylinder(cx, cy, r, hz):
    th = linspace(0, 2 * pi, 50)
    z = linspace(0, hz, 50)
    tg, zg = meshgrid(th, z)
    xg = r * cos(tg) + cx
    yg = r * sin(tg) + cy
    return xg, yg, zg
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
Xc, Yc, Zc = cylinder(0.2, 0.2, 0.05, 0.1)
ax.plot_surface(Xc, Yc, Zc, alpha=0.5)
ax.set_axis_off()

plt.show()