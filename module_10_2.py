from threading import Thread
import threading
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enamies = 100
        self.days = 0
        print(f'{self.name}, we are under attack!')
    def run(self):
        thr = Thread(target=self.battle())
        thr.start()
        self.repeater()
        thr.join()
    def battle(self):
        if self.enamies > 0:
            self.enamies -= self.power
            self.days += 1
            print(f'{self.name} is in battle {self.days} days. {self.enamies} enemies left.\n',end='')
    def repeater(self):
        if self.enamies > 0:
            threading.Timer(1, self.repeater,).start()
            self.battle()
        else:
            print(f'{str(self.name).upper()} HAS WON AFTER {self.days} DAYS!')
if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.run()
    second_knight.run()
    # first_knight.join()
    # second_knight.join()