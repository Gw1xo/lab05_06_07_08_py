class Car:
    def __init__(self, mark, model, speed=0):
        self.mark = mark
        self.model = model
        self.speed = speed

    @property
    def accelerate(self):
        self.speed += 5
        return f'Speed car:{self.get_speed}'

    @property
    def brake(self):
        self.speed -= 5
        return f'Speed car:{self.get_speed}'

    @property
    def get_speed(self):
        return self.speed
