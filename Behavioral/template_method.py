from abc import ABC, abstractmethod


class CocktailMaker(ABC):
    """
    Template method abstract class
    """
    def make(self):
        """ Template method """
        self.add_ingredient1()
        self.add_ingredient2()
        self.add_ingredient3()
        self.shake()
        self.add_decor()
        print(self.__class__.__name__, "cocktail is ready")

    @abstractmethod
    def add_ingredient1(self):
        pass

    @abstractmethod
    def add_ingredient2(self):
        pass

    def add_ingredient3(self):
        pass

    @abstractmethod
    def add_decor(self):
        pass

    def shake(self):
        print("Shaking")


class CocktailA(CocktailMaker):
    def add_ingredient1(self):
        print("Adding mint")

    def add_ingredient2(self):
        print("Adding lemon")

    def add_decor(self):
        print("Adding umbrella decor for the cup")


class CocktailB(CocktailMaker):
    def add_ingredient1(self):
        print("Adding alcohol")

    def add_ingredient2(self):
        print("Adding orange")

    def add_decor(self):
        print("Adding lime decor for the cup")


if __name__ == '__main__':
    CocktailA().make()
    print()
    CocktailB().make()
