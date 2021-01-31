class NormalItem():

    def __init__(self, name, sell_in, quality):
        self.name = name
        self. sell_in = sell_in
        self.quality = quality

    def get_quality(self):
        return self.quality

    def update_quality(self):
        if self.sell_in > 0:
            if self.quality > 0:
                self.quality -= 1
        else:
            if self.quality > 0:
                self.quality -= 2
