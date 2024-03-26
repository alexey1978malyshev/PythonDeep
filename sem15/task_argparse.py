import argparse

parser = argparse.ArgumentParser(description="Enter data")
parser.add_argument('-bs', type=int, default=100)
parser.add_argument('-bn', type=int, default=10)

args = parser.parse_args()

def func(base, bonus):
    return base + base * bonus/100

#print(func(120000, 10))
print(func(args.bs, args.bn))