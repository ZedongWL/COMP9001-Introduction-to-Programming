import config
from space_object import SpaceObject


class Engine:
    def __init__(self, game_state_filename, player_class, gui_class):
        
        self.import_state(game_state_filename)
        self.player = player_class()
        self.GUI = gui_class(self.width, self.height)
        

    def import_state(self, game_state_filename):
        # The key required by the state and the number of corresponding required values are made into basic tuples
        variable_state = ((["asteroid_small","asteroid_large"],4), (["upcoming_asteroid_large","upcoming_asteroid_small"],4))
        expect_state = [("width",1), ("height",1), ( "score",1), ("spaceship",4), ("fuel",1), ("asteroids_count",1),\
            ("bullets_count",1), ("upcoming_asteroids_count",1)]
        self.exist_asteroid_ls = []
        self.bullets_ls = []
        self.upcoming_asteroid_ls = []
        asteroid_dic = {"upcoming_asteroid_small":"asteroid_small","upcoming_asteroid_large":"asteroid_large"}
        try:
            with open(game_state_filename,"r") as f:
                self.state = f.read().splitlines()
        except FileNotFoundError:
            raise FileNotFoundError ('Error: unable to open {}'.format(game_state_filename))
        i = 0
        while i < len(self.state): 
            line_state = self.state[i].split() # Check each line of statements
            if len(line_state) !=2: # Error: not consist of a key and value pair
                raise ValueError ('Error: expecting a key and value in line {}'.format(i+1))
            if i >= len(expect_state): # Exceeding the expected number of rows
                raise ValueError ('Error: unexpected key: {} in line {}'.format(line_state[0], i+1))
            if line_state[0] not in expect_state[i][0]: # Error: an unexpected key
                raise ValueError ('Error: unexpected key: {} in line {}'.format(line_state[0], i+1))
            value_state = line_state[1].split(",")
            if len(value_state) == expect_state[i][1]: # Error: an invalid data type
                if len(value_state) == 1:
                    if not isint(value_state[0]):
                        raise ValueError ('Error: invalid data type in line {}'.format(i+1))
                elif len(value_state) == 4:
                    if not (isfloat(value_state[0]) and isfloat(value_state[1]) and isint(value_state[2]) and isint(value_state[3])):
                        raise ValueError ('Error: invalid data type in line {}'.format(i+1))
            else:
                raise ValueError ('Error: invalid data type in line {}'.format(i+1))
            if line_state[0] == "width": # Add value for each attribute
                self.width = int(line_state[1])
            elif line_state[0] == "height":
                self.height = int(line_state[1])
            elif line_state[0] == "score":
                self.score = int(line_state[1])
            elif line_state[0] == "spaceship":
                self.spaceship = SpaceObject(float(value_state[0]),float(value_state[1]),self.width,self.height,int(value_state[2]),line_state[0],int(value_state[3]))
            elif line_state[0] == "fuel": # At warning_threshold, the original fuel will be used for comparison with fuel
                self.fuel = int(line_state[1])
                self.original_fuel = int(line_state[1])
            elif line_state[0] == "asteroids_count": # Add list content
                for _ in range(int(line_state[1])):
                    expect_state.insert(-2,variable_state[0])
                self.asteroid_count = int(line_state[1]) # Mark the number of asteroids
            elif line_state[0] == "upcoming_asteroids_count": 
                for _ in range(int(line_state[1])):
                    expect_state.append(variable_state[1])
            elif line_state[0] in ["asteroid_small","asteroid_large"]:
                self.exist_asteroid_ls.append(SpaceObject(float(value_state[0]),float(value_state[1]),self.width,self.height,int(value_state[2]),line_state[0],int(value_state[3])))
            elif line_state[0] in asteroid_dic:
                self.upcoming_asteroid_ls.append(SpaceObject(float(value_state[0]),float(value_state[1]),self.width,self.height,int(value_state[2]),asteroid_dic[line_state[0]],int(value_state[3])))
            i = i + 1
        if len(self.state) != len(expect_state): # Error: file is incomplete
            raise ValueError ('Error: game state incomplete')
        

    def export_state(self, game_state_filename):
        asteroid_dic = {"asteroid_small":"upcoming_asteroid_small","asteroid_large":"upcoming_asteroid_large"}
        with open(game_state_filename,"w") as f:
            f.write("width {}\n".format(self.width))
            f.write("height {}\n".format(self.height))
            f.write("score {}\n".format(self.score))
            f.write("{}\n".format(self.spaceship.__repr__()))
            f.write("fuel {}\n".format(self.fuel))
            f.write("asteroids_count {}\n".format(len(self.exist_asteroid_ls)))
            for i in range(len(self.exist_asteroid_ls)):
                f.write("{}\n".format(self.exist_asteroid_ls[i].__repr__()))
            f.write("bullets_count {}\n".format(len(self.bullets_ls)))
            for i in range(len(self.bullets_ls)):
                f.write("{}\n".format(self.bullets_ls[i].__repr__()))
            f.write("upcoming_asteroids_count {}\n".format(len(self.upcoming_asteroid_ls)))
            for i in range(len(self.upcoming_asteroid_ls)):
                f.write("{} {:.1f},{:.1f},{},{}\n".format(asteroid_dic[self.upcoming_asteroid_ls[i].obj_type],self.upcoming_asteroid_ls[i].x,self.upcoming_asteroid_ls[i].y,self.upcoming_asteroid_ls[i].angle,self.upcoming_asteroid_ls[i].id))

    def run_game(self):
        bullet_id = 0 # Shoot id
        fuel_warning = [False]*len(config.fuel_warning_threshold) # List should have fuel warning relationship
        while True:
            stop_game = False
            # 1. Receive player input
            self.action = self.player.action(self.spaceship,self.exist_asteroid_ls,self.bullets_ls,self.fuel,self.score)

            # 2.1 Manoeuvre the spaceship as per the Player's input
            if self.action[1]:
                self.spaceship.turn_left()
            if self.action[2]:
                self.spaceship.turn_right()
            if self.action[0]:
                self.spaceship.move_forward()

            # 2.2 Update positions of asteroids
            for asteroid in range(len(self.exist_asteroid_ls)):
                self.exist_asteroid_ls[asteroid].move_forward()
            
            # 2.3 Update positions of bullets
            if self.action[3]: # Shoot
                if self.fuel < config.shoot_fuel_threshold:
                    print("Cannot shoot due to low fuel")
                    self.action[3] = False
                else:
                    self.bullets_ls.append(SpaceObject(self.spaceship.x,self.spaceship.y,self.width,self.height,self.spaceship.angle,"bullet",bullet_id))
                    bullet_id = bullet_id + 1
            i = 0
            while i < len(self.bullets_ls): # Remove expired bullets
                if self.bullets_ls[i].move_count >= config.bullet_move_count:
                    del self.bullets_ls[i]
                    i = i - 1
                i = i + 1
            for bullet in range(len(self.bullets_ls)): # Update positions of bullets
                self.bullets_ls[bullet].move_forward()
                self.bullets_ls[bullet].move_count = self.bullets_ls[bullet].move_count + 1
            
            # 2.4 Deduct fuel for spaceship and bullets (if launched)
            self.fuel = self.fuel - config.spaceship_fuel_consumption
            if self.action[3]:
                self.fuel = self.fuel - config.bullet_fuel_consumption
            for i in range(len(fuel_warning)):
                if fuel_warning[i]:
                    continue
                if not fuel_warning[i]:
                    if self.fuel <= 0.01*config.fuel_warning_threshold[i]*self.original_fuel:
                        fuel_warning[i] = True
                        print("{}% fuel warning: {} remaining".format(config.fuel_warning_threshold[i],self.fuel))
                break

            # 2.5 Detect collisions
            # A bullet collides with an asteroid
            i = 0
            while i < len(self.bullets_ls): 
                j = 0
                while j < len(self.exist_asteroid_ls):
                    if self.bullets_ls[i].collide_with(self.exist_asteroid_ls[j]):
                        if self.exist_asteroid_ls[j].obj_type == "asteroid_small":
                            self.score = self.score + config.shoot_small_ast_score
                        elif self.exist_asteroid_ls[j].obj_type == "asteroid_large":
                            self.score = self.score + config.shoot_large_ast_score
                        print("Score: {} \t [Bullet {} has shot asteroid {}]".format(self.score,self.bullets_ls[i].id,self.exist_asteroid_ls[j].id))
                        del self.bullets_ls[i]
                        del self.exist_asteroid_ls[j]
                        i = i - 1
                        break
                    j = j + 1
                i = i + 1

            # Spaceship collides with an asteroid            
            j = 0
            while j < len(self.exist_asteroid_ls): 
                if self.spaceship.collide_with(self.exist_asteroid_ls[j]):
                    self.score = self.score + config.collide_score
                    print("Score: {} \t [Spaceship collided with asteroid {}]".format(self.score,self.exist_asteroid_ls[j].id))
                    del self.exist_asteroid_ls[j]
                    j = j - 1
                j = j + 1
            
            # Replenish asteroids
            while len(self.exist_asteroid_ls) < self.asteroid_count:
                if len(self.upcoming_asteroid_ls) == 0:
                    print("Error: no more asteroids available")
                    stop_game = True
                    break
                print("Added asteroid {}".format(self.upcoming_asteroid_ls[0].id))
                self.exist_asteroid_ls.append(self.upcoming_asteroid_ls[0])
                del self.upcoming_asteroid_ls[0]

            # 3. Draw the game state on screen using the GUI class
            self.GUI.update_frame(self.spaceship,self.exist_asteroid_ls,self.bullets_ls,self.score,self.fuel)

            # Game loop should stop when:
            # - the spaceship runs out of fuel, or
            # - no more asteroids are available
            if self.fuel == 0:
                stop_game = True
            if stop_game:
                break

        # Display final score
        self.GUI.finish(self.score)
        
def isnum(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isint(value): # Determines whether it is a int type
    try:
        if isnum(value):
            int(value)
            return True
        return False
    except ValueError:
        return False
    
def isfloat(value): # Determines whether it is a float type
    if isnum(value):
        if not isint(value):
            return True
    return False
