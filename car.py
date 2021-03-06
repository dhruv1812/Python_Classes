class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def staystate(self):
        print(f'I am going at {self.speed} kmph')

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer/self.time
        else:
            pass


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car")

    while True:
        action = input('What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average_speed [S]peed').upper()

        if action not in "ABOS" or len(action) != 1:
            print("I don't know what to do")
            continue

        if action == 'A':
            my_car.accelerate()

        elif action == 'B':
            my_car.brake()

        elif action == 'O':
            print(f'The car has driven {my_car.odometer} kms')

        elif action == 'S':
            print(f'The car\'s average speed is {my_car.average_speed}kmph')

        my_car.step()
        my_car.staystate()






