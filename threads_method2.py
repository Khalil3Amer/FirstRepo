import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def run(self) -> None:
        print(self.name + " started!")
        time.sleep(10)
        print(self.name + " finished!")


def main():
    start_time = time.time_ns()
    threads = []
    for i in range(50):
        t = MyThread("Thread" + str(i))
        t.start()
        threads.append(t)
    for j in threads:
        j.join()
    end_time = time.time_ns()
    print(
        "The total time required =", str((end_time - start_time) / 1000000000)
    )


if __name__ == "__main__":
    main()
