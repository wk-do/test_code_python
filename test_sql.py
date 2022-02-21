import sqlite3
from datetime import datetime

import numpy as np
import pandas as pd


class TestSqlCmd:
    def __init__(self, db_name):
        print('__init__ db_name:', db_name)
        self.db_name = db_name  #'./sql_test'
        self.con = sqlite3.connect('{}.db'.format(self.db_name))

    def check_table_exist(self, table_name):
        # with sqlite3.connect('{}.db'.format(self.db_name)) as con:
        cur = self.con.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table' and name=:table_name"
        cur.execute(sql, {"table_name": table_name})
        return True if len(cur.fetchall()) > 0 else False

    def insert_df_to_db(self, table_name, df, option="replace"):
       # with sqlite3.connect('{}.db'.format(self.db_name)) as con:
       df.to_sql(table_name, self.con, if_exists=option)

    def execute_sql(self, sql, param={}):
       # with sqlite3.connect('{}.db'.format(self.db_name)) as con:
       cur = self.con.cursor()
       cur.execute(sql, param)
       return cur


if __name__ == "__main__":
    sql_test = TestSqlCmd('./sql_test')

    # universe = {}
    # # universe[code] = code_name
    # universe[10] = 'hello'
    #
    # now = datetime.now().strftime("%Y%m%d")
    #
    # universe_df = pd.DataFrame({
    #     # 'code': universe.keys(),
    #     # 'code_name': universe.values(),
    #     # 'created_at': [now] * len(universe.keys())
    #     'code': '1004',
    #     'code_name': 'angel',
    #     # 'created_at': [now] * len(universe.keys())
    #     'created_at': '2022-02-18'
    #
    # })
    #
    # sql_test.insert_df_to_db('univers',  universe_df)

    np.random.seed(0)
    dates = pd.date_range('20220218', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
    print(df.sort_values(by=['B'], ascending=False))
    sql_test.insert_df_to_db('universe', df)

    print('universe_list', df['A'])

    # print('universe_list', df['20220218'])   # KeyError:
    print('universe_list', df.loc['20220218'])

    # sql = "SELECT name FROM sqlite_master WHERE type='table' and name=:table_name"
    sql = "select * from universe"
    cur = sql_test.execute_sql(sql)
    universe_list = cur.fetchall()
    print('universe_list', universe_list)

    sql = "select * from universe"
    cur = sql_test.execute_sql(sql)
    universe_list = cur.fetchone()
    print('fetchone {}'.format(cur.fetchone()))

    print(df.sort_values(by=['B'], ascending=False))

    print(df.iloc[3:5, 0:2])



