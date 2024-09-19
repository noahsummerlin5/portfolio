import random
dice_roll = random.randint(1, 20)

suspense = f"The die clatters across the table before rolling to a stop. {dice_roll}."
print(suspense)
print()

modifier = 4
AC = 12
result = (dice_roll + modifier >= AC)

if result is True:
    print("Success! The arrow sinks into the goblin's chest. Roll damage.")
else:
    print("Failure; the goblin throws the primitive shield up just in time to glance away your arrow.")

if dice_roll == 20:
    print("CRITICAL HIT!! The arrow hits a vital organ - roll an extra hit die.")
