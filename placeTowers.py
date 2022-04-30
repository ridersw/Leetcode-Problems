class Solution:
    def placeTowers(self, locations, range):
        locations.sort()
        print(f'locations: {locations}')

        pointer = 0
        towerLocations = []

        while pointer < len(locations):
            ref = locations[pointer]
            while pointer < len(locations) and locations[pointer] <= ref + range:
                pointer += 1

            towerLocations.append(locations[pointer-1])

            ref = towerLocations[-1]
            while pointer < len(locations) and locations[pointer] <= ref + range:
                pointer += 1

        print(f'towerLocations: {towerLocations}')

if __name__ == "__main__":
    obj = Solution()
    print(obj.placeTowers(locations = [10, 45, 34, 12, 4, 6, 14, 19 ], range = 4))

#place towers so that every house gets covered