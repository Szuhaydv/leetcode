class Box:
    def __init__(self, boxes = [], hasKey = false):
        self.boxes = boxes
        self.key = hasKey

def box_search:
    boxWithKey = Box([], true)
    box3 = Box([boxWithKey])
    box2a = Box([box3])
    box2b = Box([])
    box1 = Box([box2a, box2b])

    boxesToSearch = []

    while box1.length != 0:
        box1

