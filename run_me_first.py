from multiprocessing import Process
from os import mkdir
from os.path import isdir
from random import random
from threading import Thread
from time import time_ns

"""
A program to init two large text files to use
with multiprocessing exampels.
"""


def creatFiles(baseDir, fileName):
    if not isdir(baseDir):
        mkdir(baseDir)
    completePath = baseDir + "\\" + fileName
    with open(completePath, "w") as file:
        for i in range(10000):
            for j in range(1000):
                file.write(str(int(random() * 10000)) + "\n")


def with_multiprocessing(baseDir, fileName1, fileName2):
    f1Process = Process(
        target=creatFiles,
        args=(
            baseDir,
            fileName1,
        ),
    )
    f2Process = Process(
        target=creatFiles,
        args=(
            baseDir,
            fileName2,
        ),
    )
    f1Process.start()
    f2Process.start()
    f1Process.join()
    f2Process.join()


def without_multiprocessing(baseDir, fileName1, fileName2):
    creatFiles(baseDir, fileName1)
    creatFiles(baseDir, fileName2)


def with_multithreading(baseDir, fileName1, fileName2):
    thread1 = Thread(target=creatFiles, args=(baseDir, fileName1))
    thread2 = Thread(target=creatFiles, args=(baseDir, fileName2))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


def test(func, msg, baseDir, file1Name, file2Name):
    start_time = time_ns()
    func(baseDir, file1Name, file2Name)
    end_time = time_ns()
    print(msg, str((end_time - start_time) / 1000000000))


def main():

    baseDir = "C:\\Python_Multiprocessing_example"
    file1Name = "f1.txt"
    file2Name = "f2.txt"
    test(
        without_multiprocessing,
        "The total time required without\
            multiprocessing or multithreading =",
        baseDir,
        file1Name,
        file2Name,
    )
    test(
        with_multithreading,
        "The total time required with multithreading =",
        baseDir,
        file1Name,
        file2Name,
    )
    test(
        with_multiprocessing,
        "The total time required with multiprocessing =",
        baseDir,
        file1Name,
        file2Name,
    )


if __name__ == "__main__":
    main()
