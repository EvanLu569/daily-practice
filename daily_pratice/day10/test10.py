'''
  Day 10 练习：给词频统计工具加上类型注解
  把 Day 6 那个词频统计工具拿出来，加上完整的类型注解。
'''
import string
import sys


# 清洗文本
def clean_text(text:str)->str:
    for ch in string.punctuation:
        text=text.replace(ch," ")
    for ch in "，。？；：’”‘“【】《》（）···-、":
        text=text.replace(ch," ")
    return text.lower()
#读取文件，返回词频字典
def count_words(filename:str)->str:
    with open(filename,"r",encoding="utf-8") as f:
        content:str=f.read()
    content=clean_text(content)
    words:list[str]=content.split()

    word_count:dict[str,int]={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count
# 返回出现次数最多的前n个单词
def get_top_words(word_count:dict[str,int],n:int=10)->list[tuple[str,int]]:
    return sorted(word_count.items(),key=lambda x:x[1],reverse=True)[:n]
# 打印词频报告
def print_report(top_words:list[tuple[str,int]])->None:
    print("*"*10)
    print("词频统计TOP",len(top_words))
    print("*"*10)
    for i,(word,count)in enumerate(top_words,start=1):
        print(f"{i}.{word:<15} {count}次")
    print("*"*10)

if __name__=="__main__":
    filename:str=sys.argv[1]if len(sys.argv)>1 else "test.txt"
    try:
        result:dict[str,int]=count_words(filename)
        top:list[tuple[str,int]]=get_top_words(result)
        print_report(top)
    except FileNotFoundError:
        print(f"文件{filename}不存在。")







