import time
from concurrent.futures import ThreadPoolExecutor


def task_that_takes_time(name):
    print(name + " started!")
    time.sleep(10)
    print(name + " finished!")


def main():
    with ThreadPoolExecutor(max_workers=10) as executors:
        for i in range(10):
            executors.submit(task_that_takes_time, str(i))


if __name__ == "__main__":
    main()
