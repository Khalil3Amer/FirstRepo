import threading
import time


def task_that_takes_time(name):
    print(name + " started!")
    time.sleep(10)
    print(name + " finished!")


def main():
    start_time = time.time_ns()
    threads = []
    for i in range(30):
        t = threading.Thread(
            target=task_that_takes_time, args=("Thread" + str(i),)
        )
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
