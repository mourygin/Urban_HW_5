import time
from threading import Thread
import threading
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enamies = 100
        self.days = 1
        print(f'{self.name}, we are under attack!')
    def run(self):
        thr = Thread(target=self.battle())
    def battle(self):
        while self.enamies > 0:
            if self.enamies > 0:
                self.enamies -= self.power
                print(f'{self.name} is in battle {self.days} days. {self.enamies} enemies left.\n',end='')
                if self.enamies <= 0:
                    print(f'{str(self.name).upper()} HAS WON AFTER {self.days} DAYS!')
            self.days += 1
            time.sleep(1)

if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()