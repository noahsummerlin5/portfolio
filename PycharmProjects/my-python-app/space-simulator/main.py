import math
import matplotlib.pyplot as plt
import random
from playground import G as G

# Define body template
bodyTemplate = {
    "name": "0",
    "xp": 0, "yp": 0, "zp": 0,  # Position
    "xv": 0, "yv": 0, "zv": 0,  # Velocity
    "xa": 0, "ya": 0, "za": 0,  # Acceleration
    "mass": 0,
    "radius": 0
}

# list of bodies
bodies = []

# create body function
def createBody(name, xp, yp, zp, xv, yv, zv, xa, ya, za, mass, radius): # name must be a string in quotation marks
    body = bodyTemplate.copy()
    body["name"] = f"{name}"
    body["xp"] = xp
    body["yp"] = yp
    body["zp"] = zp
    body["xv"] = xv
    body["yv"] = yv
    body["zv"] = zv
    body["xa"] = xa
    body["ya"] = ya
    body["za"] = za
    body["mass"] = mass
    body["radius"] = radius
    bodies.append(body)


# simulation parameters
u = 2.0 * 2.36e6  # total time
v = 100     # interval

# create bodies (examples)
createBody("planet", 0, 0, 0, 0, 0, 0, 0, 0, 0, 5.92e24, 6.371e6)
createBody("moon",3.844e8,0,0,0,1.023e3,0,0,0,0,7.348e22,1.7375e6)
# createBody("third",0,0,5e10,1e4,0,1e1,0,0,0,1e29,1.7375e6)

# track positions
positionHistory = {body["name"]: {"x": [], "y": [], "z": []} for body in bodies}

# simulation loop
t = 0
while t <= u:

    # resetting gravity to sum interactions with n other bodies without over-counting as the while loop runs
    for body in bodies:
        body["xa"] = 0
        body["ya"] = 0
        body["za"] = 0

    # interactions between all pairs of bodies
    for i, first in enumerate(bodies):
        for nth in bodies[i + 1:]:
            xdistance = (first["xp"] - nth["xp"])
            ydistance = (first["yp"] - nth["yp"])
            zdistance = (first["zp"] - nth["zp"])

            # distance equation and crash detection
            distance = (math.sqrt ( xdistance ** 2 + ydistance ** 2 + zdistance ** 2 ) )
            if distance < first["radius"] + nth["radius"]:
                print(f"{first["name"]} collided with {nth["name"]} at time = {t}")
                continue # skips further interactions

            # force of gravity between two objects
            gforce = ((G * first["mass"] * nth["mass"]) / (distance ** 2))

            # gravitational acceleration
            g1 = gforce / first["mass"]
            g2 = gforce / nth["mass"]

            # update acceleration
            first["xa"] += -1 * xdistance * g1 / distance
            nth["xa"] += xdistance * g2 / distance
            first["ya"] += -1 * ydistance * g1 / distance
            nth["ya"] += ydistance * g2 / distance
            first["za"] += -1 * zdistance * g1 / distance
            nth["za"] += zdistance * g2 / distance


    # executing kinematics and recording values
    for body in bodies:
        # update velocity based on current acceleration
        body["xv"] += body["xa"] * v
        body["yv"] += body["ya"] * v
        body["zv"] += body["za"] * v

        # update position based on current velocity
        body["xp"] += body["xv"] * v
        body["yp"] += body["yv"] * v
        body["zp"] += body["zv"] * v

        # append the new positions to the position history
        positionHistory[body["name"]]["x"].append(body["xp"])
        positionHistory[body["name"]]["y"].append(body["yp"])
        positionHistory[body["name"]]["z"].append(body["zp"])

    # next time increment
    t += v

# plotting results
ax = plt.figure().add_subplot(projection='3d')
for body in positionHistory:
    # color randomizer
    a = random.randint(1, 100) / 100
    b = random.randint(1, 100) / 100
    c = random.randint(1, 100) / 100
    color = (a, b, c)

    # plot results
    coords = positionHistory[body]
    ax.plot(coords["x"], coords["y"], coords["z"], color=color, label=f'{body} path')
ax.legend()
plt.show()