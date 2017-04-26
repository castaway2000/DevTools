#!/usr/bin/env python
"""Description: this file automatically parses a lof for patterns and prints it. for use in linux environment"""
import sys
__Author__ = "Adam Szablya"
__date__ = "8/30/2016"
__version__ = "1.0"
FP = {"fail": 0, "pass": 0}
INDEXOF = []

def get_log():
    if len(sys.argv) < 2:
        with open("./fubar.log") as file:
            data = file.readlines()
    else:
        with open(sys.argv[1]) as file:
            data = file.readlines()
    return data


def parse_log(input):
    for line in input:
        if "start pattern" in line:
            INDEXOF.append(input.index("start pattern"))

        if "end pattern" in line:
            INDEXOF.append(input.index("end pattern"))
            if "Result: Fail" in line:
                FP["fail"] += 1
            elif "Results: Pass" in line:
                FP["Pass"] += 1
            for i in range(INDEXOF[0], INDEXOF[1]):
                print(input[i])


if __name__ == "__main__":
    log = get_log()
    parse_log(log)
    print("Number of pass and fails:\n")
    print("PASS: "+FP["Pass"]+"\n")
    print("FAIL" + FP["Fail"])