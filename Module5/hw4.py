class Building:
    total = 0

    def __init__(self):
        Building.total += 1


buildings = []
for x in range(40):
    building = Building()
    buildings.append(building)
    print(building)

print(buildings)

