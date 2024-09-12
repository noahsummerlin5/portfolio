import matplotlib.pyplot as plt
import random
import numpy as np

# define body template
bodyTemplate = {
    "name": "0",
    "position": np.array([0, 0, 0]),  # Position
    "velocity": np.array([0, 0, 0]),  # Velocity
    "acceleration": np.array([0, 0, 0]),  # Acceleration
    "mass": 0,
    "radius": 0
}

# list of bodies
bodies = []

# create body function
def createBody(name, xp, yp, zp, xv, yv, zv, xa, ya, za, mass, radius): # name must be a string in quotation marks
    body = bodyTemplate.copy()
    body["name"] = f"{name}"
    body["position"] = np.array([xp, yp, zp])
    body["velocity"] = np.array([xv, yv, zv])
    body["acceleration"] = np.array([xa, ya, za])
    body["mass"] = mass
    body["radius"] = radius
    bodies.append(body)

# simulation parameters
u = 2.05 * 2.36e6  # total time
v = 1000     # interval
w = 2    # number of bodies to keep after time "s" - **OPTIONAL PARAMETER** - set s = u if useless
s = u    # when to remove all bodies besides the first "w" from system - **OPTIONAL PARAMETER** - set s = u if useless

# create bodies (examples)
createBody("third",0,0,5e10,1,0,1e1,0,0,0,1e29,1.7375e6)
createBody("moon", 3.844e8, 0, 0, 0, 1.023e3, 0, 0, 0, 0, 7.348e22, 1.7375e6)
createBody("planet", 0, 0, 0, 0, 0, 0, 0, 0, 0, 5.92e24, 6.371e6)

# gravitational constant
G = 6.6743e-11

# track positions
positionHistory = {body["name"]: {"x": [], "y": [], "z": []} for body in bodies}

# simulation loop
t = 0
while t <= u:

    # resetting gravity to sum interactions with n other bodies without over-counting as the while loop runs
    for body in bodies:
        body["acceleration"] = [0.0, 0.0, 0.0]

    # interactions between all pairs of bodies
    for i, first in enumerate(bodies):
        for nth in bodies[i + 1:]:
            # components of distance
            distances = np.subtract(first["position"], nth["position"])

            # distance equation and crash detection
            distance = np.sqrt((distances[0]) ** 2 + (distances[1]) ** 2 + (distances[2]) ** 2)

            # check for collisions
            if distance < first["radius"] + nth["radius"]:
                print(f"{first["name"]} collided with {nth["name"]} at time = {t}")
                continue # skips further interactions

            # force of gravity between two objects
            gforce = ((G * first["mass"] * nth["mass"]) / (distance ** 2))

            # gravitational acceleration
            g1 = gforce / first["mass"]
            g2 = gforce / nth["mass"]

            # update acceleration
            first["acceleration"] = np.subtract(first["acceleration"], np.divide(np.multiply(distances, g1), distance))
            nth["acceleration"] = np.add(nth["acceleration"], np.divide(np.multiply(distances, g2), distance))
    for body in bodies:
        # update velocity based on current acceleration
        body["velocity"] = np.add((np.multiply(body["acceleration"], v)), body["velocity"])

        # update position based on current velocity
        body["position"] = np.add((np.multiply(body["velocity"], v)), body["position"])

        # append the new positions to the position history
        positionHistory[body["name"]]["x"].append(body["position"][0])
        positionHistory[body["name"]]["y"].append(body["position"][1])
        positionHistory[body["name"]]["z"].append(body["position"][2])

    # taking bodies besides the first "w" out of system when allotted time passes
    if t > s:
        while len(bodies) > w:
            bodies.pop()

    # next time increment
    t += v

print(len(bodies))

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