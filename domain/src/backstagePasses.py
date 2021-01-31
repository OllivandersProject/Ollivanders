class BackstagePasses():

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def get_quality(self):
        return self.quality

    def update_quality(self):
        if self.sell_in > 10:
            if self.quality < 50:
                self.quality += 1
        elif self.sell_in > 5:
            if self.quality < 49:
                self.quality += 2
            else:
                self.quality = 50
        elif self.sell_in > 0:
            if self.quality < 48:
                self.quality += 3
            else:
                self.quality = 50
        else:
            self.quality = 0
