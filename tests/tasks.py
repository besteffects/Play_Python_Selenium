def max_value(array):
    max_num = 0
    for i in array:
        if i > max_num:
            max_num = i
    print(max_num)


if __name__ == '__main__':
    tex_array = [1, 2, 4, 5, 7, 2, 6, 7, 8, 2, 88, -1, 5]
    max_value(tex_array)
