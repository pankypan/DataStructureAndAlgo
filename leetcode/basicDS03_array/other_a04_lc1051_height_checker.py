def height_checker(heights: list) -> int:
    sorted_heights = sorted(heights)
    move_counts = 0
    for i in range(len(heights)):
        if sorted_heights[i] != heights[i]:
            move_counts += 1
    return move_counts


if __name__ == '__main__':
    print(height_checker([1, 1, 4, 2, 1, 3]))
    print(height_checker([5, 1, 2, 3, 4]))
    print(height_checker([1, 2, 3, 4, 5]))
