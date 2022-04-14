from time import time_ns

from find_sum import main as trad
from find_sum_executors import main as exec

if __name__ == "__main__":
    start_time = time_ns()
    trad()
    end_time = time_ns()
    print(
        "\033[92mtraditional way of multiprocessing : \033[0m",
        str((end_time - start_time) / 1000000000),
    )
    print("\033[91m*************************************\033[0m")
    start_time = time_ns()
    exec()
    end_time = time_ns()
    print(
        "\033[92mexecutors pool way of multiprocessing : \033[0m",
        str((end_time - start_time) / 1000000000),
    )
