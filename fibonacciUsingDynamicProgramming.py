from time import time_ns

dic = {}


def fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    if n not in dic:
        dic[n] = fib(n - 1) + fib(n - 2)
    return dic[n]


def main():
    startTime = time_ns()
    for i in range(100000):
        fib(i)
    endTime = time_ns()
    print("Running Time = ", (endTime - startTime) / 1000000000, "sec")


if __name__ == "__main__":
    main()
