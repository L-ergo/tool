# coding:utf-8
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--b', type=int, default=0)
parser.add_argument('-n', "--number", type=str, help='输入一个数字')
args = parser.parse_args()

print(args.loc)
print(args.loc2)
print(args.b)
print(args.number)
