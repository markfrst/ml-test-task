import pandas
import numpy as np
from datetime import datetime
import sys


def main(argv):
    data = pandas.read_csv(
        "/Users/markfrost/my_projects/ds/test-ml-nik/data/data.csv",
        header=0,
        sep=';'
    )

    if argv[0] == 'clear':
        clear(data)
    elif argv[0] == 'with_full_date':
        with_full_date(data)


def get_data_frame():
    return(pandas.DataFrame(
        columns=['first_name', 'last_name', 'city',
                 'bdate', 'type_1', 'type_2', 'type_3', 'type_4']
    ))


def clear(data):
    data_frame = get_data_frame()

    for i, row in data.iterrows():
        if row['first_name'] != 'DELETED':
            data_frame = data_frame.append(row,
                                           ignore_index=True)

    data_frame.to_csv(
        "/Users/markfrost/my_projects/ds/test-ml-nik/data/data1.csv",
        sep=';',
        encoding='utf-8'
    )


def with_full_date(data):
    data_frame = get_data_frame()

    for i, row in data.iterrows():
        if str(row['bdate']).count('.') == 2:
            row['bdate'] = datetime.strptime(
                str(row['bdate']), '%d.%m.%Y').date()
            data_frame = data_frame.append(row,
                                           ignore_index=True)

    data_frame.to_csv(
        "/Users/markfrost/my_projects/ds/test-ml-nik/data/data_with_full_date.csv",
        sep=';',
        encoding='utf-8',
        columns=['first_name', 'last_name', 'city',
                 'bdate', 'type_1', 'type_2', 'type_3', 'type_4']
    )


if __name__ == '__main__':
    main(sys.argv[1:])
