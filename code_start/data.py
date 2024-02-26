class Data:
    def __init__(self, ui):
        self.ui = ui
        self._coins =  0
        self._health = 5 # private member of class Data
        self.ui.create_hearts(self._health)
        self.unlocked_level = 0
        self.current_level = 0

    # getter , decorator
    @property
    def health(self):
        return self._health

    #setter
    @health.setter
    def health(self, value):
        self._health = value
        self.ui.create_hearts(value)


    # getter , decorator
    @property
    def coins(self):
        return self._coins

    #setter
    @coins.setter
    def coins(self, value):
        self._coins = value
        if self._coins >=100:
            self._coins -=100
            self.health += 1
        self.ui.show_coins(self.coins)