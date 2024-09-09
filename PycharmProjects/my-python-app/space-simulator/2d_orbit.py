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

t = 0
altitude = 2 * (10 ** 6) # 2 * (10 ** 6) is stable LEO
pradius = 6.371 * (10 ** 6)

# x-variables
xa = 0
xv = .9 * (10 ** 3) # 6.9 * (10 ** 3) is stable LEO
xp = 0.00000001

# y-variables
ya = 0
yv = 0
yp = pradius + altitude

# z-variables
# za = 0
# zv = 0
# zp = 0

n = 10 # interval size
m = 15000 # range

# position lists
times = []
xvariables = []
yvariables = []

while t <= m:

    t += n

    # general vars
    distance = np.sqrt((0 - xp) ** 2 + (0 - yp) ** 2)
    if distance < 6.371 * (10 ** 6):
        print("The orbiting object crashed into the Earth!")
        break

    if xp != 0:
        theta = np.atan(abs(0 - yp) / abs(0 - xp))
    elif xp == 0:
        print("Could not execute properly, x coordinate cannot equal 0")

    # gravity vars
    objectmass = 10000 #kilograms
    pointmass = 5.972 * (10 ** 24) #kilograms
    gforce = ((6.6743 * (10 ** -11)) * (objectmass * pointmass)) / (distance ** 2)
    gravsum = gforce / objectmass

    # x-component
    if (0 - xp) > 0:
        xgrav = np.cos(theta) * gravsum
    elif (0 - xp) < 0:
        xgrav = -1 * np.cos(theta) * gravsum

    xa = 0 + xgrav
    xv += n * xa
    xp += n * xv

    # y-component
    if (0 - yp) > 0:
        ygrav = np.sin(theta) * gravsum
    elif (0 - yp) < 0:
        ygrav = -1 * np.sin(theta) * gravsum

    ya = 0 + ygrav
    yv += n * ya
    yp += n * yv

    # append to lists
    times.append(t)
    xvariables.append(xp)
    yvariables.append(yp)

# printing lists legibly
# vars = []
# while len(vars) < (m / n):
#     vars.append(len(vars))
# # print(vars)
#
# for var in vars:
#     print(
#         f"At {times[var]} seconds, "
#         f"position is {xvariables[var]},"
#         f"{yvariables[var]}."
#     )
#     if var == (m / n):
#         break

#plot orbit
fig, ax = plt.subplots()

ax.plot(xvariables, yvariables)

#plot planet
x = np.linspace(-pradius, pradius, 500)
y1 = np.sqrt(pradius ** 2 - x ** 2)
y2 = -np.sqrt(pradius ** 2 - x ** 2)
ax.plot(x, y1)
ax.plot(x, y2)

plt.show()