# this program is meant to determine minimum delta-v necessary to achieve stable circular orbit around a much greater body
# (mass 100:1 minimum) from a stable position at its surface.

# establish variables for user input
planetRadius = 6.0e6 # in m
planetMass = 6.0e24 # in kg, should be 0 if unknown mass or different gravitational constant; see surfaceGravity
orbitHeight = 2.0e6 # in m, desired altitude above surface during orbit
rotationPeriod = 0 # in s
surfaceGravity = 0 # in m/s^2, if surface "g" is all that is known, should be 0 if planetMass is used

# universal gravitational constant
G = 6.6743e-11

# establish global gravity
gravity = 0

# radius from mass center
radius = planetRadius + orbitHeight

# determine appropriate gravity calculation
if surfaceGravity > 0 and planetMass == 0:
    gravity = surfaceGravity * (planetRadius ** 2 / radius ** 2)
elif planetMass > 0 and surfaceGravity == 0:
    gravity = planetMass * G / (radius ** 2)
else:
    print("Either a positive planet mass or surface gravity must be entered.")

# orbital velocity calculation
orbitVelocity = (gravity * radius) ** 0.5

# print results
print(f"Orbital velocity at {int(orbitHeight / 1000)} kilometers altitude is approximately {int(orbitVelocity)} m/s")