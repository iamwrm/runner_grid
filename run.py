import sys
import get_data


def get_id(args):
    assert(len(args) == 4)
    dim_length = 4
    args = [int(i) for i in args]
    idx = 0
    for i, v in enumerate(args[::-1]):
        idx += v * (dim_length**i)
    return idx

# 20-> 000020.SZ
def get_stock_code(idx: int):
    return (6-len(str(idx))) * '0' + str(idx) + '.SZ'


if __name__ == '__main__':
    provided_args = sys.argv[1:]

    idx = get_id(provided_args)
    ts_code = get_stock_code(idx)

    print(f"job_id: {idx}")
    print(f"ts_code: {ts_code}")

    df = get_data.get_stock_info(ts_code)
    print(df)
