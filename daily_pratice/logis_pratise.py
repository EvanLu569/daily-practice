# # 写一个函数
# # count_vowels(text)，统计字符串里有多少个元音字母（a,e, i, o, u），大小写都算。
# def count_vowels(text):
#     vowels=['a','e','i','o','u']
#     count=0
#     for ch in text.lower():
#         if ch in vowels:
#             count+=1
#     return count
# print(count_vowels("hello world"))

# # 写函数
# # is_palindrome(text)，判断一个字符串是不是回文（正着读反着读一样）。忽略大小写和空格。
# def is_palindrome(text):
#     text=text.lower()
#     text=text.replace(" ", "")
#     return text==text[::-1]
# print(is_palindrome("hello"))
#
# # 写函数
# # remove_duplicates(lst)，去掉列表中的重复元素，保持原有顺序。
# def remove_duplicates(lst):
#     seen=set()
#     result=[]
#     for item in lst:
#         if item not in seen:
#             result.append(item)
#             seen.add(item)
#     return result
#
# # 写函数 flatten(nested)，把嵌套列表展平一层。
# def flatten(nested):
#     result=[item for sublist in nested for item in sublist ]
#     return result


















