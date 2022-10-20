# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def read():
    return [line.split(';') for line in csv.split('\n')]


def sort(data):
    return sorted(data, key=lambda v: v[1])


def filt(data):
    return [x for x in data if int(x[1]) > 10]


def get_users_list():
    data = read()
    data = sort(data)
    return filt(data)


if __name__ == '__main__':
    print(get_users_list())
