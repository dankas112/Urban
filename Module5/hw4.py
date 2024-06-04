class Building:
    total = 0

    def __init__(self):
        Building.total += 1


for Building in range(4):
    print(Building)


