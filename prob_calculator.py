import random
import copy
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for i in kwargs:
            for a in range(0,kwargs[i]):
                (self.contents).append(i)
    def draw(self,num_balls):
        self.draw_list = []
        if num_balls >= len(self.contents):
            self.draw_list.extend(self.contents)
            self.contents.clear()
        else:
            for i in range(0,num_balls):
                self.rand_ball = random.choice(self.contents)
                (self.draw_list).append(self.rand_ball)
                self.contents.remove(self.rand_ball)
        return self.draw_list
    def get_hats(self):
        print(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = []
    for i in expected_balls:
        for a in range(0,expected_balls[i]):
            expected_balls_list.append(i)
    M = 0
    check = None
    for i in range(0,num_experiments):
        another_hat = copy.deepcopy(hat)
        another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if another_hat.draw_list.count(k) >= v])
        M += 1 if balls_req == len(expected_balls) else 0
    return M/num_experiments

