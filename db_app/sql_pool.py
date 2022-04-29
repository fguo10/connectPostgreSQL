GET_DBS_SQL = 'select datname from pg_database;'

GET_TABLES_SQL = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"

GET_TABLE_DATAS_SQL = 'select * from {table_name};'
GET_FILTER_TABLE_DATAS_SQL = "select * from {table_name} where {attr} like '%{value}%';"

GET_TABLE_ATTRS_SQL = "SELECT column_name FROM information_schema.columns WHERE table_name ='{table_name}';"
