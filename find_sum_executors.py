from concurrent.futures.process import ProcessPoolExecutor
from os.path import exists

# Python program to find the sum of each files created.


def sum_of_file(path):
    if not exists(path):
        # TODO: how to catch error form child process in Parent
        # raise ValueError("please run run_me_first.py or check inserted path")
        return 0
    nums = []
    with open(path) as file:
        for num in file:
            nums.append(int(num))
    return sum(nums)


def main():
    result1 = result2 = 0
    with ProcessPoolExecutor(max_workers=2) as executor:
        result1 = executor.submit(sum_of_file, "./Data/f1.txt")
        result2 = executor.submit(sum_of_file, "./Data/f2.txt")
        if result1.result() == 0 or result2.result() == 0:
            print(
                "\033[91mplease run run_me_first.py\
                     or check inserted path\033[0m"
            )
        else:
            print(
                "\033[92mthe sum of numbers inside the files =\033[0m",
                "\033[94m"
                + str(result1.result() + result2.result())
                + "\033[0m",
            )


if __name__ == "__main__":
    main()
