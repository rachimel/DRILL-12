from pathlib import Path

from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    IDLE_SPEED = 10
    RUN_SPEED = 20
    image = None

    def __init__(self, x, y, direction, speed):
        if Ball.image is None:
            Ball.image = load_image(
                str(Path(__file__).resolve().with_name('ball21x21.png'))
            )
        self.x, self.y = x, y
        self.direction = direction
        self.speed = speed

    def update(self):
        self.x += self.direction * self.speed
        half_width = self.image.w / 2
        if self.x < -half_width or self.x > get_canvas_width() + half_width:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
