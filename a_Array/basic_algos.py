# utf-8


def merge_sorted_arrays(a1, a2):
    ret = []
    i = j = 0
    while len(a1) >= i + 1 and len(a2) >= j + 1:
        if a[i] <= b[j]:
            ret.append(a1[i])
            i += 1
        else:
            ret.append(a2[j])
            j += 1

    if len(a) > i:
        ret += a1[i:]
    if len(b) > j:
        ret += a2[j:]

    return ret


if __name__ == '__main__':
    a = [1, 3, 4, 6, 7, 78, 97, 190]
    b = [2, 5, 6, 8, 10, 12, 14, 16, 18]
    print(merge_sorted_arrays(a, b))