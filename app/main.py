from typing import List, Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[List[float]] = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[List[float]] = None
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]

        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo = None,
            coords: Optional[List[float]] = None,
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]

        super().__init__(name, weight, coords)

        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo_object: Cargo) -> None:
        if self.current_load is None \
                and cargo_object.weight <= self.max_load_weight:
            self.current_load = cargo_object

    def unhook_load(self) -> None:
        self.current_load = None
