from dataclasses import dataclass, field


@dataclass
class MazeCell:
    x: int
    y: int
    component: 'MazeCell' = None
    is_open: bool = False
    walls: list = field(default_factory=lambda: [True, True, True, True])
