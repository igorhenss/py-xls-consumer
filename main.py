import pandas as pd
import time
from product_service import exists_by_sku, process_registers
from database_connection import connect, disconnect


def __process_file(file_path):
    reading_start = time.time()
    file = __read_xls(file_path)
    __persist_to_database(file.values)
    reading_end = time.time()
    print('Arquivo [{}] processado em {:.3f} segundos.'.format(file_path, reading_end - reading_start))


def __read_xls(file_path):
    return pd.read_excel(file_path)


def __persist_to_database(rows):
    conn, cursor = connect()
    rows_to_insert = []
    rows_to_update = []
    list(map(lambda row: __define_row_operation(cursor, row, rows_to_insert, rows_to_update), rows))
    print('Inserindo {} registros.'.format(len(rows_to_insert)))
    print('Atualizando {} registros.'.format(len(rows_to_update)))
    process_registers(conn, cursor, rows_to_insert, rows_to_update)
    disconnect(conn, cursor)


def __define_row_operation(cursor, row, rows_to_insert, rows_to_update):
    sku = row[0]
    is_update = exists_by_sku(cursor, sku)
    print('Definindo operação do SKU {}.'.format(sku))
    if is_update:
        rows_to_update.append(row)
    else:
        rows_to_insert.append(row)
    print('Operação [{}] definida para o SKU {}.\n'.format(__get_operation_name(is_update), sku))


def __get_operation_name(is_update):
    return 'ATUALIZAÇÃO' if is_update else 'INSERÇÃO'


if __name__ == '__main__':
    __process_file('./files/produtos_2022-06-20_23_42_10.xlsx')
