import sys

def print_id(args):
    args = [int(i) for i in args]
    idx = 0
    for i,v in enumerate(args):
        idx +=v* (8**i)
    print(f"job_id: {idx}")


if __name__ == '__main__':
    provided_args = sys.argv[1:]
    print_id(provided_args)
