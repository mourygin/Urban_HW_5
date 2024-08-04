from threading import Thread, Lock
class BankAccount():

    def __init__(self,account_nr):
        self.account_nr = account_nr
        self.sum = 1000

    def deposit(self, amount):
        # lock.acquire()
        self.sum += amount
        # lock.release()
        print(f'Deposited {amount}, new balance is {self.sum}')
    def withdraw(self, amount):
        # lock.acquire()
        self.sum -= amount
        # lock.release()
        print(f'Withdrew {amount}, new balance is {self.sum}')

if __name__ == '__main__':
    def deposit_task(account, amount):
        for i in range(5):
            lock.acquire()
            account.deposit(amount)
            lock.release()
    def withdraw_task(account, amount):
        for i in range(5):
            lock.acquire()
            account.withdraw(amount)
            lock.release()

    lock = Lock()
    account = BankAccount('1010101')
    deposit_thread = Thread(target=deposit_task, args=(account, 100))
    withdraw_thread = Thread(target=withdraw_task, args=(account, 150))
    deposit_thread.start()
    withdraw_thread.start()
    deposit_thread.join()
    withdraw_thread.join()
    print(f'TOTAL BALANCE IS {account.sum}')