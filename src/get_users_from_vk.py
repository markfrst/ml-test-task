import vk_api

import pandas
import numpy as np


def main():
    vk_session = vk_api.VkApi('+1234', '1234')
    vk_session.auth()
    vk = vk_session.get_api()

    data_frame = pandas.DataFrame(
        columns=['first_name', 'last_name', 'city',
                 'bdate', 'type_1', 'type_2', 'type_3', 'type_4']
    )

    rows = pandas.read_excel(
        "/Users/markfrost/my_projects/ds/test-ml-nik/data/most_typed.xlsx",
        usecols=["Ид", "Интро/Экстра", "Логик/Этик",
                 "Сенс/Интуит", "Рац/Иррац"]
    )

    for i, row in rows.iterrows():
        print(i)
        user = vk.users.get(user_ids=row['Ид'], fields=["city", "bdate"])[0]
        city = user.get('city', None)

        data_frame = data_frame.append(
            {
                'first_name': user['first_name'],
                'last_name': user['last_name'],
                'bdate': user.get('bdate', None),
                'city': city['title'] if city is not None else None,
                'type_1': row['Интро/Экстра'],
                'type_2': row['Логик/Этик'],
                'type_3': row['Сенс/Интуит'],
                'type_4': row['Рац/Иррац']
            },
            ignore_index=True
        )

    data_frame.to_csv(
        "/Users/markfrost/my_projects/ds/test-ml-nik/data/data.csv",
        sep=';',
        encoding='utf-8'
    )


if __name__ == '__main__':
    main()
