# 定义两个列表
letters = ["a", "b", "c"]
numbers = [2, 1, 3]

# 使用zip函数将两个列表结合起来，然后根据数字列表排序
zipped_lists = zip(letters, numbers)
sorted_pairs = sorted(zipped_lists)
print(zipped_lists, sorted_pairs)

# 解压排序后的列表
sorted_numbers, sorted_letters = zip(*sorted_pairs)
print(sorted_letters)

