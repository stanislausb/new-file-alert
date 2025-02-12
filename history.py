import os
import glob
import config


def add(path):
    with open(config.root_dir + os.path.sep + ".history", "a") as f:
        f.write(path + "\n")


def exists(path):
    with open(config.root_dir + os.path.sep + ".history", 'r') as f:
        for line in f:
            if path in line:
                return True
            else:
                return False

def  fillHistory():
    for path in glob.glob(config.root_dir + "./01*/**/*.*", recursive=True):
        add(path)


if __name__ == "__main__":
    fillHistory()
