import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items(): # Unpacks key and value from kwargs dictionary
            for i in range(count):
                self.contents.append(color)
    
    def draw(self, num):
        total_num = len(self.contents)
        num_list = []
        updated_contents = []
        self.drawn_balls = []
        if num > len(self.contents):
            pass
        else:
            self.drawn_balls = random.sample(self.contents, k=num) # Generates x unique random numbers within a given range
            for x in self.drawn_balls:
                self.contents.remove(x)
            return self.drawn_balls
        # Subtracts drawn_balls from self.contents
        # self.contents = set([self.contents]) - set([drawn_balls])
            # does not work since sets only contain unique items - eg set([green, green, blue]) = ([green, blue])
        # self.contents = [x for x in self.contents if x not in drawn_balls]
            # not sure why this doesnt work
    

    # loop number of experiments
        # hat.draw(num_balls_drawn)
            # check that expected_balls = drawn_balls
            # num_success += 1
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_contents = []
    num_success = 0
    for color, count in expected_balls.items():
        for i in range(count):
            expected_balls_contents.append(i)
            # lists the colors*count of the balls
    for i in range(num_experiments):
      copyhat = copy.deepcopy(hat)
      copyhat.draw(num_balls_drawn)
      for j in expected_balls_contents:
        if j in copyhat.drawn_balls:
            copyhat.drawn_balls.remove(j)
        if len(copyhat.drawn_balls) == 0:
          num_success += 1
    
    probability = float(num_success)/num_experiments
    return probability
