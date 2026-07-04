# Day6：综合练习 — 词频统计工具
# 任务：读取一个文本文件，统计每个单词出现的次数，然后按次数从高到低输出。
# 这个练习串起你学过的：文件读写、字符串处理、字典、sorted +lambda 、列表推导式。
import string
import sys

def count_words(filename):
    # 读取文本
    with open(filename,"r",encoding="utf-8") as f:
        content=f.read()
    # print(content)

    # 统计单词出现次数   要分词，去标点符号，统一大小写
    # 去掉英文标点
    for ch in string.punctuation:
        content=content.replace(ch," ")
    #去掉中文标点
    for ch in "，。！？；：”“‘’【】《》（）··· 、 -":
        content=content.replace(ch," ")
    # 统一转为小写
    content=content.lower()
    # print(content)

    # 按空白字符分割
    words=content.split()
    # 统计词频
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    #查看结果
    # for word,count in word_count.items():
    #     print(f"{word}:{count}")

    # 按次数降序排列
    sorted_words=sorted(word_count.items(),key=lambda item:item[1],reverse=True)
    return sorted_words

def print_report(sorted_words):
    # 输出
    for word,count in sorted_words:
        print(f"{word}:{count}")


# 主程序入口
if __name__=="__main__":
    if len(sys.argv)>1:
        filename=sys.argv[1]
    else:
        filename="test.txt"
    try:
        result=count_words(filename)
        print_report(result)
    except FileNotFoundError:
        print(f"文件'{filename}'不存在，请检查路径！")








