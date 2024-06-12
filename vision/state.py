# state.py

class State:
    def __init__(self):
        self.frame = None
        self.running = False
        self.results = None
        self.center_x = 0
        self.center_y = 0
        self.obj_center_x = 0
        self.obj_center_y = 0
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def update(self, frame, running, results, center_x, center_y, obj_center_x, obj_center_y, x1, y1, x2, y2):
        self.frame = frame
        self.running = running
        self.results = results
        self.center_x = center_x
        self.center_y = center_y
        self.obj_center_x = obj_center_x
        self.obj_center_y = obj_center_y
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

state = State()
