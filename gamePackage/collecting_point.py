
class CollectingPoint:
    """CollectingPoint class represents a collecting point on the grid"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pos(self):
        return self.x, self.y

