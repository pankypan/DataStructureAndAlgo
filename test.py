import sys
import json


def change_str_to_lis(in_string):
    if len(in_string) == 2:
        return list()
    las_res = []
    res = []
    temp_lis = in_string.split(',')
    for item in temp_lis:
        if item.startswith('[['):
            res.append(int(item[2:]))
        elif item.startswith('['):
            res.append(int(item[1:]))
        elif item.endswith("]]"):
            res.append(int(item[: len(item) - 2]))
        elif item.endswith(']'):
            res.append(int(item[: len(item) - 1]))
    index = 0
    while index < len(res):
        tem = []
        for i in range(2):
            tem.append(res[index])
            index += 1
        las_res.append(tem)
    return las_res


def compare_book_increase(book1, book2):
    return book1[0] < book2[0] and book1[1] < book2[1]


def compare_book_decrease(book1, book2):
    return book1[0] > book2[0] and book1[1] > book2[1]


def get_books_arrays(books):
    books.sort()
    total = len(books)
    dp_increase = [1] * total
    dp_decrease = [1] * total

    for i in range(1, total):
        for j in range(i):
            if compare_book_increase(books[j], books[i]):
                dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)
                pass
            if compare_book_decrease(books[j], books[i]):
                dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)
    print(dp_increase, dp_decrease)
    return max(dp_increase + dp_decrease)


if __name__ == "__main__":
    get_books_arrays([[9, 10], [10, 10], [15, 11], [20, 16]])
    change_str_to_lis('[]')

