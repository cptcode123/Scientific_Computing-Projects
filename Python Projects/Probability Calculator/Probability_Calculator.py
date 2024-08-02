import copy
import random

class Hat:
    '''
    Hats class: Takes a variable amount of keyword arguments
    Instance variable = 'contents'
    contents: list, str items, number of items depends, # of each color is determined by args
    '''
    __slot__ = 'contents'
    def __init__(self, **kwargs):
        self.contents = []
        for color,num in kwargs.items():
            while num > 0:
                self.contents.append(color)
                num -= 1

    def draw(self, num):
        '''
        remove ball at random from the contents
        return a list of removed items
        '''
        drawn = []
        if num >= len(self.contents):
            drawn = self.contents
            self.contents = []
            return drawn
        drawn = list(random.sample(self.contents, k=num))
        for item in drawn:
            self.contents.remove(item)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    Returns float number M/N where M is # of successful experiments and N is # of experiments

M += 1 if expected_balls is in drawn list
    expected_balls should be list for easier check
    '''
    expected = []
    for color,num in expected_balls.items():
            while num > 0:
                expected.append(color)
                num -= 1
    print(expected)
    M = 0
    N = 0
    while N < num_experiments:
        pool = copy.deepcopy(hat)
        pick = pool.draw(num_balls_drawn)
        print(pick)
        temp = 0
        for item in expected:
            if item in pick:
                temp += 1
                pick.remove(item)
        if temp == len(expected):
            M += 1   
        N += 1 
    P = M/N
    return P

#Example 
bucket = Hat(black=6, red=4, green=3)
probability = experiment(hat=bucket,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=5)
print(probability)      