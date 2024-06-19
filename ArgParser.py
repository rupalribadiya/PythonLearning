# run command:
# help: python ArgParser.py -h
# exec: python ArgParser.py -n 3

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="Number of times to meow", type=int, default=1)
parser.add_argument("-t", help="Type of n", type=str, default="int")
args = parser.parse_args()

print(args)
for i in range(args.n):
    print("meow")