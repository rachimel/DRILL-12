from pico2d import load_image
import os
path = os.getcwd() + '\\Labs\\LEC12_CharacterController\\'

class Grass:
    def __init__(self):
        self.image = load_image(path + 'grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass
