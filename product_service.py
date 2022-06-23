def exists_by_sku(cursor, sku):
    select_statement = "select 1 from produto where sku = '{}'".format(sku)
    cursor.execute(select_statement)
    fetched_row = cursor.fetchone()
    return bool(fetched_row)


def process_registers(conn, cursor, rows_to_insert, rows_to_update):
    list(map(lambda row: __insert_register(cursor, row), rows_to_insert))
    list(map(lambda row: __update_register(cursor, row), rows_to_update))
    conn.commit()


def __insert_register(cursor, row):
    insert_statement = __create_insert_statement(row)
    cursor.execute(insert_statement)


def __create_insert_statement(row):
    return "insert into produto (sku,descricao,estoque,valor,tier,ativo) values ('{}','{}','{}','{}','{}','{}')"\
        .format(row[0], row[1], row[2], row[3], row[4], __string_to_boolean(row[5]))


def __update_register(cursor, row):
    update_statement = __create_update_statement(row)
    cursor.execute(update_statement)


def __create_update_statement(product):
    return "update produto set descricao='{}',estoque='{}',valor='{}',tier='{}',ativo='{}' where sku='{}'"\
        .format(product[1], product[2], product[3], product[4], __string_to_boolean(product[5]), product[0])


def __string_to_boolean(string):
    return string.upper() == 'SIM'
