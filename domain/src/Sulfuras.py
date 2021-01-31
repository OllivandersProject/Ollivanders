
# class Sulfuras(NormalItem):
class Sulfuras():
    
    def __init__(self, name='', sell_in=0, quality=80):
        # super().__init__(name, sell_in, quality)
        
        #* Contructor sin aplicar Herencia aún
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.legendary = True
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_sell_in(self):
        return self.sell_in
    
    def set_sell_in(self, sell_in):
        self.sell_in = sell_in
    
    def get_quality(self):
        return self.quality
    
    def set_quality(self, quality):
        self.quality = quality
    
    def is_legendary(self):
        return self.legendary
    
    def set_legendary(self, legendary):
        self.legendary = legendary
        
    def update_quality(self):
        
        assert self.get_quality() == 80, f"The Quality of {self.__class__.__name__} is different of 80"
        pass
    
    