from time import time_ns

from find_sum import main as trad
from find_sum_executors import main as exec

if __name__ == "__main__":
    start_time = time_ns()
    trad()
    end_time = time_ns()
    print(
        "traditional way of multiprocessing : ",
        str((end_time - start_time) / 1000000000),
    )
    start_time = time_ns()
    exec()
    end_time = time_ns()
    print(
        "executors pool way of multiprocessing : ",
        str((end_time - start_time) / 1000000000),
    )
