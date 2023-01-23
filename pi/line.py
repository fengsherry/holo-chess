

class Line():
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1 
        self.x2 = x2 
        self.y1 = y1 
        self.y2 = y2

        self.dx = self.x2 - self.x1
        self.dy = self.y2 - self.y1
    

    def intersection(self, other):
        # Determinant for finding points of intersection 
        x = ((self.x1*self.y2 - self.y1*self.x2)*(other.x1-other.x2) - (self.x1-self.x2)*(other.x1*other.y2 - other.y1*other.x2))/ ((self.x1-self.x2)*(other.y1-other.y2) - (self.y1-self.y2)*(other.x1-other.x2)) 
        y = ((self.x1*self.y2 - self.y1*self.x2)*(other.y1-other.y2) - (self.y1-self.y2)*(other.x1*other.y2 - other.y1*other.x2))/ ((self.x1-self.x2)*(other.y1-other.y2) - (self.y1-self.y2)*(other.x1-other.x2)) 
        x = int(x) 
        y = int(y) 
        return x,y