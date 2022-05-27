class House:
    def __init__(self):
        self._features = []

    def add_feature(self, feature: str) -> None:
        self._features.append(feature)

    def get_features(self) -> str:
        return f"House with the following features: {', '.join(self._features)}"
