import psycopg2

from db_app.sql_pool import GET_DBS_SQL, GET_TABLES_SQL, GET_TABLE_DATAS_SQL, GET_TABLE_ATTRS_SQL, \
    GET_FILTER_TABLE_DATAS_SQL


class DB(object):
    def __init__(self, host: str = "127.0.0.1", port: int = 5432,
                 user: str = "postgres", password: str = "westos", **kwargs):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.conn = psycopg2.connect(host=self.host,
                                     port=self.port,
                                     user=self.user,
                                     password=self.password)
        self.cur = self.conn.cursor()

    def get_sql_results(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_dbs(self):
        IGNORE_DBNAME = []
        sql_results = self.get_sql_results(GET_DBS_SQL)
        table_names = [item[0] for item in sql_results if item[0] not in IGNORE_DBNAME]
        return table_names

    def use_db(self, database):
        self.database = database
        self.conn = psycopg2.connect(host=self.host,
                                     port=self.port,
                                     user=self.user,
                                     password=self.password,
                                     database=self.database)

        self.cur = self.conn.cursor()

    def get_tables(self):
        table_names = [item[0] for item in self.get_sql_results(GET_TABLES_SQL)]
        return table_names

    def get_table_datas(self, table_name):
        table_names = self.get_tables()
        if table_name not in table_names:
            raise ValueError(f"tablename = {table_name} not exists, please check it")
        sql = GET_TABLE_DATAS_SQL.format(table_name=table_name)
        return self.get_sql_results(sql)

    def get_filter_table_datas(self, table_name, attr, value):
        table_names = self.get_tables()
        if table_name not in table_names:
            raise ValueError(f"tablename = {table_name} not exists, please check it")
        sql = GET_FILTER_TABLE_DATAS_SQL.format(table_name=table_name, attr=attr, value=value)
        print("sql", sql)
        return self.get_sql_results(sql)

    def get_table_attrs(self, table_name):
        table_names = self.get_tables()
        if table_name not in table_names:
            raise ValueError(f"tablename = {table_name} not exists, please check it")

        sql = GET_TABLE_ATTRS_SQL.format(table_name=table_name)
        attrs = [item[0] for item in self.get_sql_results(sql)]
        return attrs


#
# con = psycopg2.connect(user="postgres", password="westos", host="127.0.0.1", port="5432", database="postgres")
db_obj = DB()
