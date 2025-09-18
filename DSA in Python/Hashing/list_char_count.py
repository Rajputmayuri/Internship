# s = "azyxyyzaaaa"
# q = ["a", "a", "y", "x"]
# dic = {}
# for ch in q:
#     if ch not in dic:
#         dic[ch] = s.count(ch)
# print(dic)


"""usig ascii value"""

s = "azyxyyzaaaa"
q = ["a", "a", "y", "x"]
hash_list = [0] * 26
for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1
for ch in q:
    ascii_value = ord(ch)
    index = ascii_value - 97
    print(ch, ":", hash_list[index])
