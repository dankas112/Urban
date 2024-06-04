class Buildings:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self):
        return self.numberOfFloors == self.buildingType


shop = Buildings(6, 'store')

print(shop.__eq__())
