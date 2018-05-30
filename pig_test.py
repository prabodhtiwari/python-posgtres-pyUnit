import subprocess

def first_test():
    return subprocess.check_output(["cat", "/home/hadoop/output.csv"])


print first_test()