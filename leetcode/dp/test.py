def get_words(input_str, pre):
    init_words = input_str.split(' ')
    valid_words = []
    invalid_char_lis = [".", ",", "?", "!"]
    for item in init_words:
        if item.find('.') > -1 or item.find(',') > -1:
            valid_words.append(item[:len(item) - 1])
            pass
        elif item.find("'") > -1:
            w_lis = item.split("'")
            valid_words += w_lis
            pass
        else:
            valid_words.append(item)
            pass
        pass
    res = []
    for item in valid_words:
        if item.startswith(pre):
            res.append(item)
            pass
        pass
    res.sort()

    # res 去重
    unique_res = []
    for item in res:
        if item not in unique_res:
            unique_res.append(item)
    return ' '.join(unique_res) if len(unique_res) > 0 else pre


if __name__ == "__main__":
    # 读取第一行的n
    # input_str = sys.stdin.readline().strip()
    # print(input_str)
    # common_str = sys.stdin.readline().strip()
    # print(common_str)
    ss = """The furthest distance in the world, Is not between life and death, But when I stand in front of you, Yet you don't know that I love you."""
    print(get_words(ss, 'f'))
    print(get_words("I love you", "He"))
    pass

