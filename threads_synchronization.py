from threading import Lock, Thread
from time import time_ns


class Bank:
    # Private
    __balance = 0
    # Public

    def getBalance(self):
        return self.__balance

    def addBalance(self, balance):
        self.__balance += balance


class AddBalanceWithoutSynchronization(Thread):
    # Private
    __account: Bank
    # Public

    def __init__(self, account: Bank) -> None:
        super().__init__()
        self.__account = account

    def run(self) -> None:
        for i in range(1000000):
            self.__account.addBalance(i)


class AddBalanceWithSynchronization(Thread):
    # Private
    __account: Bank
    __lock: Lock
    # Public

    def __init__(self, account: Bank, lock: Lock) -> None:
        super().__init__()
        self.__account = account
        self.__lock = lock

    def run(self) -> None:
        for i in range(1000000):
            self.__lock.acquire()
            self.__account.addBalance(i)
            self.__lock.release()


def main():
    account = Bank()
    threads = []
    start_time = time_ns()
    for i in range(10):
        thread = AddBalanceWithoutSynchronization(account)
        thread.start()
        threads.append(thread)
    for i in threads:
        i.join()
    end_time = time_ns()
    print(
        f"Balance after incerement\
             without Synchronization = {account.getBalance()}",
        f"The total time required =\
             {str((end_time - start_time) / 1000000000)}",
    )
    lock = Lock()
    account = Bank()
    threads = []
    start_time = time_ns()
    for i in range(10):
        thread = AddBalanceWithSynchronization(account, lock)
        thread.start()
        threads.append(thread)
    for i in threads:
        i.join()
    end_time = time_ns()
    print(
        f"Balance after incerement\
             with Synchronization = {account.getBalance()}",
        f"The total time required =\
             {str((end_time - start_time) / 1000000000)}",
    )


if __name__ == "__main__":
    main()

# With Synchronization requires more time but accurte.
