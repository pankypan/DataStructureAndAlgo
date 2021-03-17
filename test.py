from typing import List
"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。

示例 1：
输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：
输入：["cool","lock","cook"]
输出：["c","o"]

潘柯 2021-03-06
"""


def check(lis):
    if sum(lis) == 0: return False

    min_val = min(lis)
    if min_val == 0: return False
    return True


def get_common_chars(str_lis: List[str]):
    res = []

    words_count = len(str_lis)
    all_char_lis = [[0 for _ in range(words_count)] for _ in range(26)]

    for i, word in enumerate(str_lis):
        for char in word:  # ord('a') : 97
            all_char_lis[ord(char) - 97][i] += 1

    for index, item in enumerate(all_char_lis):
        if check(item):
            for i in range(min(item)):
                res.append(chr(97 + index))
    return res


if __name__ == '__main__':
    print(get_common_chars(["bella", "label", "roller"]))
    print(get_common_chars(["cool", "lock", "cook"]))
    pass
