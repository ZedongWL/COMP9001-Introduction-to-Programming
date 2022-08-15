import math
import config

class SpaceObject:
    def __init__(self, x, y, width, height, angle, obj_type, id):
        # Define the initial attributes of an object, including dimension and velocity.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.obj_type = obj_type
        self.id = id
        self.radius = config.radius[self.obj_type]
        self.speed = config.speed[self.obj_type]
        if self.obj_type == "spaceship":
            self.rotational_speed = config.angle_increment
        if self.obj_type == "bullet":
            self.move_count = 0
    
    # Correct parameters are required.
    def is_correct(self):
        if self.angle >= 360:
            self.angle = self.angle - 360
        elif self.angle < 0:
            self.angle = self.angle + 360
        if self.x >= self.width:
            self.x = self.x - self.width
        elif self.x < 0:
            self.x = self.x + self.width
        if self.y >= self.height:
            self.y = self.y - self.height
        elif self.y < 0:
            self.y = self.y + self.height

    def turn_left(self):
        self.angle = self.angle + self.rotational_speed
        self.is_correct()

    def turn_right(self):
        self.angle = self.angle - self.rotational_speed
        self.is_correct()

    def move_forward(self):
        self.x = self.x + math.cos(math.radians(self.angle))*self.speed
        self.y = self.y - math.sin(math.radians(self.angle))*self.speed
        self.is_correct()

    def get_xy(self):
        return (self.x, self.y)

    def collide_with(self, other):
        # Compare the sum of distance and radius of two objects.
        # Considered objects wrapping around
        if abs(self.x - other.x) <= self.width/2:
            distance_x = abs(self.x - other.x)
        else:
            distance_x = self.width - abs(self.x - other.x)
        if abs(self.y - other.y) <= self.height/2:
            distance_y = abs(self.y - other.y)
        else:
            distance_y = self.height - abs(self.y - other.y)
        distance = math.sqrt((distance_x)**2 + (distance_y)**2)
        if self.radius + other.radius >= distance:
            return True
        return False
        
    def __repr__(self):
        self.state = "{} {:.1f},{:.1f},{},{}".format(self.obj_type, self.x, self.y, self.angle,self.id)
        return self.state
