import multiprocessing
from ctypes import c_double
from os.path import exists

# Python program to find the sum of each files created.


def sum_of_file(path, result):
    if not exists(path):
        raise ValueError("please run run_me_first.py or check inserted path")
    nums = []
    with open(path) as file:
        for num in file:
            nums.append(int(num))
    result.value = sum(nums)


def main():
    result1 = multiprocessing.Value(c_double, 0)
    result2 = multiprocessing.Value(c_double, 0)
    process1 = multiprocessing.Process(
        target=sum_of_file,
        args=(
            "./Data/f1.txt",
            result1,
        ),
    )
    process2 = multiprocessing.Process(
        target=sum_of_file,
        args=(
            "./Data/f2.txt",
            result2,
        ),
    )
    process2.start()
    process1.start()
    process1.join()
    process2.join()
    print(
        "the sum of numbers inside the files =",
        str(result1.value + result2.value),
    )


if __name__ == "__main__":
    main()
