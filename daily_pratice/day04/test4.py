#  题1：有一行数据 "Evan,25,Python,北京"，用 split
#  切开，然后打印第三个字段（语言）。
info="Evan,26,python,光启"
result=info.split(",")
print(result[2])

#  题2：给下面的电影按评分从高到低排序：
movies = [
  {"title": "流浪地球", "rating": 7.9},
  {"title": "哪吒", "rating": 8.4},
  {"title": "长津湖", "rating": 7.4},
]
rank=sorted(movies,key=lambda x:x["rating"],reverse=True)
print(rank)
#  题3：有一个列表 [5, 12, 17, 8, 3, 10]，
#  用 filter 筛选出大于等于 10 的数。
nums=[5, 12, 17, 8, 3, 10]
result1=list(filter(lambda n:n>=10,nums))
print(result1)