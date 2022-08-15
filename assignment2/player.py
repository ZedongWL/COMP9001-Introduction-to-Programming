import config
import math

class Player:
    
    def __init__(self):
        
        # Enter your code here
        self.treated_asteroid_ls = []
        

    def action(self, spaceship, asteroid_ls, bullet_ls, fuel, score):
        
        # Enter your code here
        
        self.score_ls = []
        self.spaceship = MySpaceObject(spaceship.x, spaceship.y, spaceship.width, spaceship.height, spaceship.angle, spaceship.obj_type, spaceship.id)
        self.asteroid_ls = asteroid_ls
        self.bullet_ls = bullet_ls
        self.fuel = fuel
        self.score = score
        score_dic = {"asteroid_small":config.shoot_small_ast_score,"asteroid_large":config.shoot_large_ast_score}

        if self.fuel <= config.shoot_fuel_threshold:
            return (False, False, False, False)

        for bullet in self.bullet_ls: # Check which asteroids the bullet can hit
            for asteroid in self.asteroid_ls:
                if self.crash(bullet,asteroid):
                    self.treated_asteroid_ls.append(asteroid)
                    break
            
        self.asteroid_ls = [asteroid for asteroid in asteroid_ls if asteroid not in self.treated_asteroid_ls]

        if len(self.asteroid_ls) == 0: # If there is no asteroid to shoot, stay put
            return (False, False, False, False)

        for i in range(len(self.asteroid_ls)):
            self.score_ls.append(score_dic[self.asteroid_ls[i].obj_type] /self.step_num(self.spaceship,self.asteroid_ls[i]))
        target_asteroid = self.asteroid_ls[self.score_ls.index(max(self.score_ls))] 

        decision = self.step_first(self.spaceship,target_asteroid)
        thrust = decision[0]
        left = decision[1]
        right = decision[2]
        if thrust:
            self.spaceship.move_forward()
        if left:
            self.spaceship.turn_left()
        if right:
            self.spaceship.turn_right()
        bullet = self.shoot(self.spaceship,target_asteroid)

        return (thrust, left, right, bullet)

    def shoot(self,spaceship,asteroid): # Check whether the shooting conditions are met
        s_ectype = MySpaceObject(spaceship.x, spaceship.y, spaceship.width, spaceship.height, spaceship.angle, "bullet", spaceship.id)
        a_ectype = MySpaceObject(asteroid.x, asteroid.y, asteroid.width, asteroid.height, asteroid.angle, asteroid.obj_type,asteroid.id)

        for i in range(config.bullet_move_count):
            s_ectype.move_forward()
            a_ectype.move_forward()
            if s_ectype.collide_with(a_ectype):
                return True
        return False

    def step_num(self,spaceship,asteroid): # Calculate how many steps it takes to successfully shoot an asteroid
        s_ectype = MySpaceObject(spaceship.x, spaceship.y, spaceship.width, spaceship.height, spaceship.angle, spaceship.obj_type, spaceship.id)
        a_ectype = MySpaceObject(asteroid.x, asteroid.y, asteroid.width, asteroid.height, asteroid.angle, asteroid.obj_type,asteroid.id)

        if self.shoot(s_ectype,a_ectype):
            return 0.01 # Avoid zerodivisionerror

        # Determine the angle of spaceship and asteroid using the arctangent
        if abs(s_ectype.x - a_ectype.x) <= s_ectype.width/2:
            distance_x = a_ectype.x - s_ectype.x
        elif s_ectype.x - a_ectype.x > 0:
            distance_x = a_ectype.x + s_ectype.width - s_ectype.x
        else:
            distance_x = a_ectype.x - s_ectype.width - s_ectype.x
        if abs(s_ectype.y - a_ectype.y) <= s_ectype.height/2:
            distance_y = -(a_ectype.y - s_ectype.y)
        elif s_ectype.y - a_ectype.y > 0:
            distance_y = -(a_ectype.y + s_ectype.height - s_ectype.y)
        else:
            distance_y = -(a_ectype.y - s_ectype.height - s_ectype.y)
        angle = math.degrees(math.atan2(distance_y, distance_x)) 

        # Adjust angle in [0,360)
        if angle < 0:
            angle = angle + 360
        
        # Adjust the spacecraft angle
        # Set the angle threshold. Asteroids in this range are not considered, because of excessive consumption
        upper_angle_threshold = 180 + config.angle_increment
        lower_angle_threshold = 180 - config.angle_increment
        if abs(s_ectype.angle - angle) > lower_angle_threshold and abs(s_ectype.angle - angle) < upper_angle_threshold:
            return float("inf")
        if abs(s_ectype.angle - angle) <= lower_angle_threshold:
            if s_ectype.angle - angle > config.angle_increment/2 :
                s_ectype.turn_right()
            elif s_ectype.angle - angle < -config.angle_increment/2 :
                s_ectype.turn_left()
            if abs(s_ectype.angle - angle) < 90: # Avoid moving in the opposite direction
                s_ectype.move_forward()
            a_ectype.move_forward()
            return 1 + self.step_num(s_ectype,a_ectype)
        else:
            if s_ectype.angle - angle > 0:
                if angle + 360 - s_ectype.angle > config.angle_increment/2 :
                    s_ectype.turn_left()
                    if angle + 360 - s_ectype.angle < 90:
                        s_ectype.move_forward()
            elif s_ectype.angle - angle < 0:
                if s_ectype.angle + 360 - angle > config.angle_increment/2 :
                    s_ectype.turn_right()
                    if s_ectype.angle + 360 - angle < 90:
                        s_ectype.move_forward()
            if abs(s_ectype.angle - angle) < 90: # Prevent turning 360 degrees
                s_ectype.move_forward()
            a_ectype.move_forward()
            return 1 + self.step_num(s_ectype,a_ectype)

    def step_first(self,spaceship,asteroid): # The first step of calculation
        s_ectype = MySpaceObject(spaceship.x, spaceship.y, spaceship.width, spaceship.height, spaceship.angle, spaceship.obj_type, spaceship.id)
        a_ectype = MySpaceObject(asteroid.x, asteroid.y, asteroid.width, asteroid.height, asteroid.angle, asteroid.obj_type,asteroid.id)
        thrust = False
        left = False
        right = False
        if self.shoot(s_ectype,a_ectype):
            return (thrust, left, right)

        # Determine the angle of spaceship and asteroid using the arctangent
        if abs(s_ectype.x - a_ectype.x) <= s_ectype.width/2:
            distance_x = a_ectype.x - s_ectype.x
        elif s_ectype.x - a_ectype.x > 0:
            distance_x = a_ectype.x + s_ectype.width - s_ectype.x
        else:
            distance_x = a_ectype.x - s_ectype.width - s_ectype.x
        if abs(s_ectype.y - a_ectype.y) <= s_ectype.height/2:
            distance_y = -(a_ectype.y - s_ectype.y)
        elif s_ectype.y - a_ectype.y > 0:
            distance_y = -(a_ectype.y + s_ectype.height - s_ectype.y)
        else:
            distance_y = -(a_ectype.y - s_ectype.height - s_ectype.y)
        angle = math.degrees(math.atan2(distance_y, distance_x)) 

        # Adjust angle in [0,360)
        if angle < 0:
            angle = angle + 360
        
        # Adjust the spacecraft angle
        lower_angle_threshold = 180 - config.angle_increment
        if abs(s_ectype.angle - angle) <= lower_angle_threshold:
            if s_ectype.angle - angle > config.angle_increment/2 :
                right = True
            elif s_ectype.angle - angle < -config.angle_increment/2 :
                left = True
            if abs(s_ectype.angle - angle) < 90: # Avoid moving in the opposite direction
                thrust = True
        else:
            if s_ectype.angle - angle > 0:
                if angle + 360 - s_ectype.angle > config.angle_increment/2 :
                    left = True
                    if angle + 360 - s_ectype.angle < 90:
                        thrust = True
            elif s_ectype.angle - angle < 0:
                if s_ectype.angle + 360 - angle > config.angle_increment/2 :
                    right = True
                    if s_ectype.angle + 360 - angle < 90:
                        thrust = True
            
        return (thrust, left, right)

    def crash(self,bullet,asteroid): # Determine whether the bullet can hit the asteroid
        b_ectype = MySpaceObject(bullet.x, bullet.y, bullet.width, bullet.height, bullet.angle, bullet.obj_type, bullet.id)
        a_ectype = MySpaceObject(asteroid.x, asteroid.y, asteroid.width, asteroid.height, asteroid.angle, asteroid.obj_type,asteroid.id)
        
        for i in range(config.bullet_move_count):
            b_ectype.move_forward()
            a_ectype.move_forward()
            if b_ectype.collide_with(a_ectype):
                return True
        return False


class MySpaceObject:
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