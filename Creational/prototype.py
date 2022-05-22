import copy


class Microchip:
    def __init__(self, schema: str):
        self.schema = schema
    
    def __repr__(self):
        return f"{self.__class__.__name__}(schema='{self.schema}')"


class Robot:
    def __init__(self, name: str, model: str, list_of_microchips: list[Microchip]):
        self.name = name
        self.model = model
        self.list_of_microchips = list_of_microchips
    
    def __copy__(self):
        """ Called when copy.copy(self) function is called """

        name = copy.copy(self.name)
        model = copy.copy(self.model)
        list_of_microchips = copy.copy(self.list_of_microchips)
        new = self.__class__(name, model, list_of_microchips)
        return new

    def __deepcopy__(self, memo: dict = None):
        """ Called when copy.deepcopy(self) function is called """

        if memo is None:
            memo = {}
        name = copy.deepcopy(self.name, memo=memo)
        model = copy.deepcopy(self.model, memo=memo)
        list_of_microchips = copy.deepcopy(self.list_of_microchips, memo=memo)
        new = self.__class__(name, model, list_of_microchips)
        return new


list_of_microchips = [Microchip("MY-1"), Microchip("MY-2"), Microchip("MY-3")]
robot = Robot("Rex", "MY-1337", list_of_microchips)
print(f"Robot microchips: {robot.list_of_microchips}")


robot_copy = copy.copy(robot)
print(f"\nRobot (copy) microchips: {robot_copy.list_of_microchips}")


are_microchips_same = [robot_microchip is robot_copy_microchip for robot_microchip, robot_copy_microchip
                       in zip(robot.list_of_microchips, robot_copy.list_of_microchips)]
print(f"\nDo the robots have the same microchip object IDs? {all(are_microchips_same)}")
