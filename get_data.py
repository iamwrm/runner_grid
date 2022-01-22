import tushare as ts


def get_stock_info(ts_api, ts_code):
    start_date = '2019-01-01'
    end_date = '2020-01-01'
    df = ts_api.daily(
        ts_code=ts_code,
        start_date=start_date,
        end_date=end_date)
    return df


def create_tushare_api():
    with open('./env') as f:
        lines = f.readlines()
        ts_token = lines[0].strip()
        ts_api = ts.pro_api(ts_token)
        return ts_api


if __name__ == '__main__':
    ts_code = '000001.SZ'  # 第一号股票，平安
    ts_api = create_tushare_api()
    df = get_stock_info(ts_api, ts_code)
    print(df)
