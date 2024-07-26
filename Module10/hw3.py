from threading import Thread, Lock


class BankAccount(Thread):
    def __init__(self, account):
        super().__init__()
        self.account = account
        self.deposit_lock = Lock()
        self.withdraw_lock = Lock()

    def deposit(self, amount):
        self.deposit_lock.acquire()
        self.account += amount
        print(f'Deposited {amount}, new balance is {self.account}')
        self.deposit_lock.release()

    def withdraw(self, amount):
        self.withdraw_lock.acquire()
        self.account -= amount
        print(f'Withdrew {amount}, new balance is {self.account}')
        self.withdraw_lock.release()


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount(1000)

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
