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
        drawn_balls = []
        if num > len(self.contents):
            return self.contents
        else:
            drawn_balls = random.sample(self.contents, k=num) # Generates x unique random numbers within a given range
            for x in drawn_balls:
                self.contents.remove(x)
            return drawn_balls
        # Subtracts drawn_balls from self.contents
        # self.contents = set([self.contents]) - set([drawn_balls])
            # does not work since sets only contain unique items - eg set([green, green, blue]) = ([green, blue])
        # self.contents = [x for x in self.contents if x not in drawn_balls]
            # not sure why this doesnt work
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_contents = []
    num_success = 0
    # for color, count in expected_balls.items():
    #     for i in range(count):
    #         expected_balls_contents.append(color)
    #         # lists the colors*count of the balls
    for i in range(num_experiments):
      success = True
      correct_color = 0
      copyhat = copy.deepcopy(hat)
      # copyhat.draw(num_balls_drawn)
      # drawn_balls = random.sample(copyhat.contents, k=num_balls_drawn)
      drawn_balls = copyhat.draw(num_balls_drawn)
      # if drawn_balls == expected_balls_contents:
      #   num_success += 1
      # for x in drawn_balls:
      #     copyhat.contents.remove(x)
      for key in expected_balls.keys():
        # if drawn_balls.count(key) >= expected_balls[key]:
      #   if j in drawn_balls:
          if drawn_balls.count(key) < expected_balls[key]:
            success = False
            break
          correct_color += 1
      # if correct_color == len(expected_balls):
      #   num_success += 1
      if success:
        num_success += 1
    
    probability =  float(num_success) / num_experiments
    return probability
