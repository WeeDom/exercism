import random
import string
import os


class Robot:
    def generate_random_name(self):
        # generate a random name, and check against extant robot_names.txt
        name = ''.join(random.choice(string.ascii_uppercase) for i in range(2)) + \
            ''.join(random.choice(string.digits) for i in range(3))
        if not os.path.exists('robot_names.txt'):
            open('robot_names.txt', mode='w').close()
        with open('robot_names.txt', mode='r+') as f:
            # this may need to be refactored if we had a large number of robots
            known_names = f.readlines()
            if name in known_names:
                self.generate_random_name()
            else:
                with open('robot_names.txt', mode='a') as f:
                    f.write(f'{name}\n')
        return name

    def reset(self):
        self.name = self.generate_random_name()

    def __init__(self):
        self.reset()
        self.name = self.generate_random_name()
