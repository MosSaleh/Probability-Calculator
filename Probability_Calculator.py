import copy
import random


class Hat:
    def __init__(self, **colors):
        self.contents = []
        for color, number in colors.items():
            for i in range(number):
                self.contents.append(color)

    def draw(self, num):
        # function that randomly draws a number of balls given as argument
        # and removes the specific balls from the hat

        removedballs = []
        emptyl = []

        for i in range(num):
            # makes sure if number of balls to draw is greater than number of balls
            # present that it breaks out of loops and returns the balls to hat
            if self.contents == emptyl:
                self.contents = removedballs
                break
            randomball = random.choice(self.contents)
            removedballs.append(str(randomball))
            self.contents.remove(randomball)

        return removedballs


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    def findnumcolor(list, colortofind):
        x = 0
        for color in list:
            if color == colortofind:
                x += 1
        return x

    hatcopy = copy.deepcopy(hat)

    removedballs = hatcopy.draw(num_balls_drawn)

    # to ensure that if the balls drawn are equal to or greater
    # than the content of the hat that it returns 1.0 without going through loops
    if hatcopy.contents == removedballs:
        prob = 1.0
        return prob

    M = 0

    for i in range(num_experiments):
        hatcopy = copy.deepcopy(hat)

        removedballs = hatcopy.draw(num_balls_drawn)

        for color, num in expected_balls.items():
            OGnum = findnumcolor(hat.contents, color)

            finalnum = findnumcolor(hatcopy.contents, color)

            expectednum = OGnum - num

            condition = True

            if finalnum > expectednum:
                condition = False
                if condition == False:
                    break

        if condition is True:
            M += 1

    N = num_experiments

    prob = M / N
    return prob
