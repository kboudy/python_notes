import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--x", type=float, default=1.0, help="What is the first number?"
    )
    parser.add_argument(
        "--y", type=float, default=1.0, help="What is the second number?"
    )
    parser.add_argument(
        "--operation",
        type=str,
        default=1.0,
        help="What operation? (add, sub, mul, or div)",
    )
    args = parser.parse_args()
    print(str(calc(args)))


def calc(args):
    if args.operation == "add":
        return args.x + args.y
    if args.operation == "sub":
        return args.x - args.y
    if args.operation == "mul":
        return args.x * args.y
    if args.operation == "div":
        return args.x / args.y


if __name__ == "__main__":
    main()


# for help:
# python 02\ command\ line\ args.py --h

# ex:
# python 02\ command\ line\ args.py --x=1 --y=2 --operation=add
