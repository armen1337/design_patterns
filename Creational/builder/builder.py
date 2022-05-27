from house_builders import ModernHouseBuilder, EuropeanHouseBuilder
from director_builder import Director


if __name__ == '__main__':
    # 1
    builder = ModernHouseBuilder()
    director = Director(builder)
    director.build_full_featured_house()
    print(builder.get_result().get_features())

    # 2
    builder = EuropeanHouseBuilder()
    director = Director(builder)
    director.build_minimum_featured_house()
    builder.build_backyard()   # control the builder manually (i.e. without a director)
    print(builder.get_result().get_features())
