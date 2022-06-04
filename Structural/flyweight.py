# Phones


class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state: list) -> None:
        print(f"Flyweight with the following parameters:")
        print(f"Shared state: {', '.join(self._shared_state)}")
        print(f"Unique state: {', '.join(unique_state)}")


class FlyweightFactory:
    _flyweights: dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: list):
        for state in initial_flyweights:
            self._flyweights[self.get_hashed_key(state)] = Flyweight(state)

    def get_hashed_key(self, key: list) -> str:
        return "_".join(sorted(key))

    def get_flyweight(self, shared_state) -> Flyweight:
        key = self.get_hashed_key(shared_state)

        if not self._flyweights.get(key):
            print("Creating new flyweight")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("Using existing flyweight")

        return self._flyweights[key]


def create_phone(factory: FlyweightFactory, brand: str, model: str,
                 gpu: str, cpu: str, ram: str) -> None:
    flyweight = factory.get_flyweight([gpu, cpu, ram])
    flyweight.operation([brand, model])


if __name__ == '__main__':
    # 1. GPU  2. CPU  3. RAM
    initial_state = [
        ["M210", "Snapdragon 500", "4gb"],
        ["M210", "Snapdragon 450", "3gb"],
        ["M230", "Snapdragon 650", "6gb"],
    ]

    factory = FlyweightFactory(initial_state)

    create_phone(factory, "Xiaomi", "Redmi 7", *initial_state[0])

    print()
    create_phone(factory, "Samsung", "Galaxy S20", "M230", "Snapdragon 550", "4gb")

