import pandas
import numpy as np

import sys


def main(argv):
    data = pandas.read_csv(
        "/Users/markfrost/my_projects/ds/test-ml-nik/data/data.csv",
        header=0,
        sep=';'
    )

    if argv[0] == 'clear':
        clear(data)


def clear(data):
    data_frame = pandas.DataFrame(
        columns=['first_name', 'last_name', 'city',
                 'bdate', 'type_1', 'type_2', 'type_3', 'type_4']
    )

    for i, row in data.iterrows():
        if row['first_name'] != 'DELETED':
            print(row)
            data_frame = data_frame.append(row)

    data_frame.to_csv(
        "/Users/markfrost/my_projects/ds/test-ml-nik/data/data1.csv",
        sep=';',
        encoding='utf-8'
    )


if __name__ == '__main__':
    main(sys.argv[1:])
