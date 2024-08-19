# coding=UTF-8
'''Добрый день! Я намеренно усложнил задачу и постарался ее немного "раскрасить", ну, то-есть оживить...
На площади у входа в парк расположено четыре кафе. В них разное количество столиков и разная скорость обслуживания.
Чем больше столов, тем медленнее они обслуживаются. (официанты страшно мешают друг другу!)
Клиенты кроме оплаты счета могут оставлять чаевые, которые зависят от суммы заказа и скорости обслуживания.
В конце смены подводятся итоги. Если располагаете временем, досмотрите до конца (3 минуты) и Вы увидите статистику.
Спасибо.
Хорошего дня!'''
import threading
import queue
import time
from datetime import datetime, timedelta
from random import randint

customer_nr = 1
service_time = 20
ff = []     #список функций обслуживания
trtr = []   #список потоков обслуживания
class Menu():
    def __init__(self, dishes = [('шашлык', 2,5), ('люля-кебаб', 2.5), ('гамбургер', 1.5), ('антрекот', 3), ('форель', 5)], \
                 drinks = [('лимонад', 1), ('боржоми', 1.5), ('пиво', 1.25), ('киндзмараули', 3), ('рислинг', 3.5)]):
        self.dishes = dishes
        self.drinks = drinks
    def make_order(self):
        di = randint(0,4)
        dr = randint(0,4)
        order = str(self.dishes[di][0]) + ' и ' + str(self.drinks[dr][0])
        order_cost =float(self.dishes[di][1]) + float(self.drinks[dr][1])
        return [order, order_cost]
class Table():
    def serve_customer(self):
        global final
        if self.customer != None:
            # real_t = datetime.now() - self.customer.beg_moment
            real_t = float(time.time()) - float(self.customer.beg_moment)
            money = self.customer.payment
            tip = Customer.tip_calc(self.customer, real_t)
            print(f'Клиент {self.customer.number} заплатил по счету ${money} и оставил ${tip} чаевых.\n', end='')
            # print(f'real_t = {real_t}, money = {money}, tip = {tip}')
            # Сдаем деньги в кассу
            self.cafe.lock.acquire()
            self.cafe.kassa += money
            self.cafe.lock.release()
            self.customer.payment = 0
            # Суммируем чаевые
            self.cafe.tips_lock.acquire()
            self.cafe.tips += tip
            self.cafe.tips_lock.release()
            self.customer = None
            self.is_busy = False
            # Учет посетителей
            self.cafe.cust_lock.acquire()
            self.cafe.customer_counter += 1
            self.cafe.cust_lock.release()
            # проверяем остались ли еще необслужанные посетители, не пора ли выводить статистику?
            if time.time() - work_start >= working_day:
                final = True
                for cafe in squere.cafes:
                    for table in cafe.table_list:
                        if table.is_busy:
                            final = False
                if final:
                    squere.make_statistics()

    def __init__(self, id, cafe):
        self.cafe = cafe
        self.id = id
        self.nr = None
        self.is_busy = False
        self.customer = None
        # # Каждому столу создаем функцию "обслужить клиента" и помещаем ее в отдельный поток
        def f():
            global final
            self.serve_customer()
            if not final:
                tmr = threading.Timer(cafe.serv_t,function=f)
                tmr.start()
        ff.append(f)
        tr = threading.Thread(target=f)
        trtr.append(tr)
        tr.start()
        tr.join()

class Cafe():
    def __init__(self, name, tables):
        self.name = name
        self.queue = queue.Queue()
        self.q_len = 0
        self.tables = tables
        self.table_list = []
        self.serv_t = service_time * (1 + (tables / 20))
        self.kassa = 0.0
        self.lock = threading.Lock()
        self.tips = 0.0
        self.tips_lock = threading.Lock()
        self.customer_counter = 0
        self.cust_lock = threading.Lock()

    def customer_arrival(self, customer):
        self.queue.put(customer)
        self.q_len += 1
        for i in self.table_list:
            if not i.is_busy:
                cust_from_q = self.queue.get()
                customer.table = cust_from_q
                self.q_len -= 1
                i.is_busy = True
                order = menu.make_order()
                print(f'{datetime.now()} Клиент {customer_nr} занял столик {i.id}.')
                i.customer = customer
                print(f'{datetime.now()} Клиент {customer_nr} заказал {order[0]}. ({order[1]}$.)')
                customer.payment = order[1]
                customer.beg_moment = time.time()
                return
class Customer():
    def __init__(self, number):
        self.number = number
        self.table = None
        self.payment = 0
        self.tip = 0
        self.beg_moment = None
    def select_cafe(self):
        # Выбираем кафе с самой короткой очередью, а еще лучше со свободным столиком
        q_max = 0
        res = None
        # Но сначала, к сожалению, придется найти максимум
        for i in squere.cafes:
            if i.q_len > q_max:
                q_max = i.q_len
        # print('q_max =',q_max)
        q_min = q_max * -1
        # А теперь ищем минимум
        for i in squere.cafes:
            # print(i.name, 'q_len =', i.q_len)
            if i.q_len == 0:
                for j in i.table_list:
                    if not j.is_busy:
                        # Ура! Свободный столик! Нам сюда!
                        return i
                q_min = 0
                res = i
            else:
                if i.q_len * -1 >= q_min:
                    q_min = i.q_len * -1
                    res = i
        return res
    def tip_calc(self,cust_time):
        a = self.payment * 0.1
        k = (service_time - cust_time) / service_time + 1 # коэффициент  за скорость
        a *= k
        # округляем чаевые до 50 центов
        c = int(a)
        d = a - c
        d = d * 2
        d = round(d)
        d = d / 2
        a = c + d
        if a < 0:
            # print(f'***TIP*** payment = {self.payment} time = {cust_time} tip = {a}\n', end='')
            a = 0
        return a


class Squere():
    def __init__(self):
        self.cafes = []

    def hunger(self):
        global work_start
        while True:
            self.cust_gen()
            time.sleep(1)
            # Конец смены. Прекращение появления новых клиентов.
            if time.time() - work_start >= working_day:
                break
    def cust_gen(self):
        global customer_nr
        new_customer = Customer(customer_nr)
        print(f'{datetime.now()} Клиент {customer_nr} проголодался')
        best_cafe = new_customer.select_cafe()
        print(f'{datetime.now()} Клиент {customer_nr} выбрал кафе "{best_cafe.name}" (q_len={best_cafe.q_len})')
        best_cafe.customer_arrival(new_customer)
        customer_nr += 1
    def make_statistics(self):
        for cafe in squere.cafes:
            print('======================================================')
            print(f'Кафе "{cafe.name}":')
            print(f'За смену обслужено {cafe.customer_counter} посетителей. ({round(cafe.customer_counter / cafe.tables, 2)} в пересчете на 1 стол.)')
            print(f'Получено ${cafe.kassa} выручки. (${round(cafe.kassa / cafe.tables, 2)} в пересчете на 1 стол.)')
            print(f'Заплачено чаевых ${cafe.tips}. (${round(cafe.tips / cafe.tables, 2)} в пересчете на 1 стол.)')
        print('======================================================')
        tr_alive = False
        for tr in trtr:
            if tr.is_alive():
                tr_alive = True
        if (not tr_alive) and (not tr_cust_gen.is_alive()):
            print('Все потоки корректно завершили свою работу.')
        exit()
if __name__ == '__main__':
    working_day = 18 # Длительностьь смены (в секундах реальной работы программы)
    final = False
    trs = []
    squere = Squere()
    menu = Menu()
    tables = []
    nord = Cafe('NORD', 3)
    squere.cafes.append(nord)
    west = Cafe('WEST', 2)
    squere.cafes.append(west)
    south = Cafe('SOUTH',3)
    squere.cafes.append(south)
    east = Cafe('EAST',4)
    squere.cafes.append(east)
    tt = 0 # количество столов в предыдущих кафе
    for i in squere.cafes:
        jj = 0 #  номера столов п/п
        for j in range(i.tables):
            table = Table(str(i.name) + '-' + str(j+1),i)
            table.nr = tt + jj
            tables.append(table) # потом уберем
            i.table_list.append(table)
            jj += 1
        tt += i.tables
    work_start = time.time()
    tr_cust_gen = threading.Thread(target=squere.hunger)
    tr_cust_gen.start()
    tr_cust_gen.join()
