import pyxel
import helpers
from sprite import Sprite

class Player(Sprite):
    def __init__(self, img_bank, editX, editY, width, height, scale):
        super().__init__(img_bank, editX, editY, width, height,scale)

        self.speed = 2

    def update(self):
        original_x = self.posX
        original_y = self.posY

        if pyxel.btn(pyxel.KEY_LEFT):
            self.posX -= self.speed

        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.posX += self.speed

        elif pyxel.btn(pyxel.KEY_UP):
            self.posY -= self.speed
        
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.posY += self.speed

        if self.is_colliding(self.posX, self.posY, helpers.WALL_TILE):
            self.set_pos(original_x,original_y)
        

       


