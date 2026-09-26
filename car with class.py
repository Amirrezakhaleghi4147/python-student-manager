class Car :

    def __init__(self, brand, model, current_speed) :

        self.brand = brand

        self.model = model

        self.current_speed = current_speed

    def accelerate(self, accelerate_amount) :

        self.accelerate_amount = accelerate_amount

        self.current_speed = self.current_speed + self.accelerate_amount

        return self.current_speed

    def brake(self, brake_amount) :

        self.brake_amount = brake_amount

        if self.current_speed == 0 :

            raise ValueError('you are already stopped ! ')

        if self.current_speed < self.brake_amount :

            raise ValueError('speed can not be minus !')

        self.current_speed = self.current_speed - self.brake_amount

        return self.current_speed

    def show_speed(self) :

        return f'the car is moving with {self.current_speed} km/h speed '


try :

    car_1 = Car('Toyota', 'Supra 1993', 30 )

    print(car_1.current_speed)

    print(car_1.accelerate(30))

except ValueError as e :

    print(f'Error : {e}')