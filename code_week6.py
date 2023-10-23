# Hàm đếm số lần 2 ký tự liền nhau bị trùng lặp
# def count_adjacent_repeats(s):
#     repeats = 0
#     for i in range(len(s) -1 ):
#         if s[i] == s[i + 1]:
#             repeats += 1
#         i = i +1
#     return repeats
#
# s = 'Happy birthday Tammie cchu'
# print(count_adjacent_repeats(s))

# Cùng là đếm lần bị lặp nhưng đếm từ sau ra truocws:
def count_adjacent_repeat2(s):
    repeat = 0
    for i in range(1, len(s)): #range từ n đến 1 range(len(s), range(1, len(s)), range(len(s) + 1), range(1, len(s) + 1)
        # i = len(s)
        if s[i] == s[i - 1]:
            repeat = repeat + 1
        # i = i - 1
    return repeat

s = 'Happy birthday Tammie cchu'
print(count_adjacent_repeat2(s))

# for i in range(26,0,-1):
#     print(s[i - 1])