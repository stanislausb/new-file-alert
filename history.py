import os
import config


def add(path):
    with open(config.root_dir + os.path.sep + ".history", "a") as f:
        f.write(path + "\n")


def getList():
    with open(config.root_dir + os.path.sep + ".history") as f:
        return [line.rstrip("\n") for line in f]
