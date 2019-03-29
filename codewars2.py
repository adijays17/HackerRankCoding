d = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

NS = 0
EW = 0
for e in d:
    if e is "NORTH":
        NS += 1
    elif e is "SOUTH":
        NS -= 1
    elif e is "EAST":
        EW += 1
    elif e is "WEST":
        EW -= 1

ud = []

if NS > 0:
    while NS:
        ud.append("NORTH")
        NS -= 1
elif NS < 0:
    while NS:
        ud.append("SOUTH")
        NS += 1

if EW > 0:
    while EW:
        ud.append("EAST")
        EW -= 1
elif EW < 0:
    while EW:
        ud.append("WEST")
        EW += 1

print(ud)