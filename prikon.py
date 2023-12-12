
class spotrebic:

    def __init__(self, napeti: float, proud: float):
        if not (isinstance(napeti, float) or isinstance(napeti, int)):
            raise ValueError
        if not (isinstance(proud, float) or isinstance(proud, int)):
            raise ValueError
        self.napeti = napeti
        self.proud = proud
    def prikon(self):
        return  self.napeti * self.proud

    def odpor(self):
        return self.napeti / self.proud


