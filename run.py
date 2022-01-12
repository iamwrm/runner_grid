import sys

def get_id(args):
    assert(len(args) == 4)
    dim_length = 4
    args = [int(i) for i in args]
    idx = 0
    for i,v in enumerate(args[::-1]):
        idx +=v* (dim_length**i)
    return idx


if __name__ == '__main__':
    provided_args = sys.argv[1:]

    idx= get_id(provided_args)

    print(f"job_id: {idx}")
