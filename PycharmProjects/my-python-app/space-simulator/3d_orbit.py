# from math import pi
# from math import sin
# from math import cos
# from math import tan
# from math import asin
# from math import acos
# from math import atan

# object = {
#     "xpos": 0 + xvel*(t) + 1/2*xacc*(t)^2
#     "ypos": y
#     "xvel": 0
#     "yvel": 0
#     "xacc": 0
#     "yacc": 0
# }
# veryyyyy rough first draft
# t = 0
#
# while t <= 10:
#     xacc = 0
#     xvel = 0 + xacc * (t)
#     xpos = 0 + xvel * (t) + 0.5 * xacc * (t) ** 2
#
#     yacc = -9.8
#     yvel = 0 + yacc * (t)
#     ypos = 0 + yvel * (t) + 0.5 * yacc * (t) ** 2
#
#     print(f"{xpos}, {ypos}")
#
#     t += 0.1
#
# # print(f"{xpos}, {ypos}")


# second draft
# t = 0
# a = 0
# v = 0
# p = 0
#
# while t <= 100:
#
#     if xp < 20:
#         xa = (10 / ((20 - xp) ** 2))  # x-gravity and integrations
#     if xp > 20:
#         xa = (-10 / ((20 - xp) ** 2))
#     else:
#         xa = 0
#     xv += 0.01 * xa
#     xp += 0.01 * xv
#     print(f"Time = {t} seconds, Position = {p} meters")
#     t += 0.001


# third draft - never functional
# while t <= 100:
#     if xp < 20:
#         xa = (10 / ((20 - xp) ** 2))  # x-gravity and integrations
#     if xp > 20:
#         xa = (10 / ((20 - xp) ** 2))
#     else:
#         xa = 0
#     xv += 0.01 * xa
#     xp += 0.01 * xv
#
#     if yp < 20:
#         a = (10 / ((distance) ** 2))  # y-gravity and integrations
#     if yp > 20:
#         a = (-10 / ((distance) ** 2))
#     else:
#         a = 0
#     yv += 0.01 * ya
#     yp += 0.01 * yv
#
#     print(f"Time = {t} seconds, Position = {p} meters")
#
#     t += 0.01


# fourth draft - lets gooooooo
# import math
#
# t = 0
#
# # x-variables
# xa = 0
# xv = 5
# xp = 0.01
#
# # y-variables
# ya = 0
# yv = 0
# yp = 20
#
# # z-variables
# # za = 0
# # zv = 0
# # zp = 0
#
#
# while t <= 100:
#
#     # general vars
#     distance = math.sqrt((0 - xp) ** 2 + (0 - yp) ** 2)
#     if xp != 0:
#         theta = math.atan(abs(0 - yp) / abs(0 - xp))
#     elif xp == 0:
#         print("Could not execute properly, x coordinate cannot equal 0")
#
#     # gravity vars
#     objectmass = 1 #units?
#     pointmass = 100 #
#     gforce = (objectmass * pointmass) / (distance ** 2)
#     gravsum = gforce / objectmass
#
#     # x-component
#     if (0 - xp) > 0:
#         xgrav = math.cos(theta) * gravsum
#     elif (0 - xp) < 0:
#         xgrav = -1 * math.cos(theta) * gravsum
#
#     xa = 0 + xgrav
#     xv += 0.01 * xa
#     xp += 0.01 * xv
#
#     # y-component
#     if (0 - yp) > 0:
#         ygrav = math.sin(theta) * gravsum
#     elif (0 - yp) < 0:
#         ygrav = -1 * math.sin(theta) * gravsum
#
#     ya = 0 + ygrav
#     yv += 0.01 * ya
#     yp += 0.01 * yv
#
#     # print and reset
#     print(f"At {t} seconds, the object is at ({xp},{yp})")
#     t += 0.01


# fifth draft (2D PLOTTING ACHIEVED)
import numpy as np
import matplotlib.pyplot as plt

G = 6.6743 * (10 ** -11)
pradius = 6.371 * (10 ** 6)

# n is interval size and m is range
# the succeeding variables define initial position and initial velocity components in the x, y, and z directions
def orbit(m, n, xinit, yinit, zinit, xvel, yvel, zvel):
    t = 0
    altitude = 2 * (10 ** 6)  # 2 * (10 ** 6) is stable LEO

    # x-variables
    xa = 0
    xv = xvel  # 6.9 * (10 ** 3) is stable LEO
    xp = xinit

    # y-variables
    ya = 0
    yv = yvel
    yp = yinit # pradius + altitude works great for equatorial orbit

    # z-variables
    za = 0
    zv = zvel
    zp = zinit

    # position lists
    xvars = []
    yvars = []
    zvars = []

    while t <= m:

        t += n

        # general vars
        distance = np.sqrt((0 - xp) ** 2 + (0 - yp) ** 2 + (0 - zp) ** 2)
        if distance < 6.371 * (10 ** 6):
            print("The orbiting object crashed into the Earth!")
            break

        # gravity vars
        objectmass = 10000 #kilograms
        pointmass = 5.972 * (10 ** 24) #kilograms
        gforce = G * (objectmass * pointmass) / (distance ** 2)
        gravsum = gforce / objectmass

        # x-coordinate
        # if (0 - yp) > 0:
        #     ygrav = np.sin(theta) * gravsum
        # elif (0 - yp) < 0:
        #     ygrav = -1 * np.sin(theta) * gravsum

        xgrav = (0 - xp) * gravsum / distance

        xa = 0 + xgrav
        xv += n * xa
        xp += n * xv

        # y-component
        # if (0 - yp) > 0:
        #     ygrav = np.sin(theta) * gravsum
        # elif (0 - yp) < 0:
        #     ygrav = -1 * np.sin(theta) * gravsum

        ygrav = (0 - yp) * gravsum / distance

        ya = 0 + ygrav
        yv += n * ya
        yp += n * yv

        # z-component
        # if (0 - zp) > 0:
        #     zgrav = np.sin(theta) * gravsum
        # elif (0 - zp) < 0:
        #     zgrav = -1 * np.sin(theta) * gravsum

        zgrav = (0 - zp) * gravsum / distance

        za = 0 + zgrav
        zv += n * za
        zp += n * zv

        # append to lists
        xvars.append(xp)
        yvars.append(yp)
        zvars.append(zp)

    # plot orbit
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(xvars, yvars, zvars, color='b', label='orbit')
    ax.legend()

    # draw sphere
    u, v = np.mgrid[0:2 * np.pi:50j, 0:np.pi:50j]
    x = pradius * np.cos(u) * np.sin(v)
    y = pradius * np.sin(u) * np.sin(v)
    z = pradius * np.cos(v)
    # alpha controls opacity
    ax.plot_surface(x, y, z, color="g", alpha=0.6)

    ax.set_zlim3d(-10 * pradius, 10 * pradius)  # viewrange for z-axis should be [-4,4]
    ax.set_ylim3d(-10 * pradius, 10 * pradius)  # viewrange for y-axis should be [-2,2]
    ax.set_xlim3d(-10 * pradius, 10 * pradius)  # viewrange for x-axis should be [-2,2]

    plt.show()

# printing lists legibly
# vars = []
# while len(vars) < (m / n):
#     vars.append(len(vars))
# # print(vars)
#
# for var in vars:
#     print(
#         f"At {times[var]} seconds, "
#         f"position is {xvars[var]},"
#         f"{yvars[var]}."
#     )
#     if var == (m / n):
#         break

orbit(50000, 100, 0, pradius + 2 * (10 ** 6), 0, 8.9 * (10 ** 3), 0, 0)
