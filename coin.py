from sprite import Sprite


class Coin(Sprite):
    def __init__(self, img_bank, editX, editY, width, height, scale):
        super().__init__(img_bank, editX, editY, width, height,scale)

        self.speed = 2

        self.active = True

    
    def is_active(self):
        return self.active
    
    def set_active(self, bool):
        '''Set active'''

        self.active = bool
 




    


