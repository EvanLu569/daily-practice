# 1. 所有练习给 TypedDict 注解：定义 Movie 类型（title, year, rating）
#    写函数 best_movie(movies: list[Movie]) -> Movie
from collections import defaultdict
from collections.abc import Callable
from typing import TypedDict, Literal, TypeVar, Any, List, Dict


class Movie(TypedDict):
    title:str
    year:int
    rating:float
def best_movie(movies:list[Movie])->Movie:
    return max(movies,key=lambda m:m['rating'])
movie={'title':'这个杀手不太冷','year':2010,'rating':9.9}
title=movie['title']
year=movie['year']
rating=movie['rating']
# 2. 用 Literal 限制参数：写函数 sort_data(data, order)，order 只能是 "asc" 或 "desc"
T=TypeVar('T')
def sort_data(data:list[T],order:Literal["asc","desc"])->list[T]:
    return sorted(data,reverse=order=="desc")
# 3. 用 Callable 注解高阶函数：写一个 filter_by 函数，
#    接收 list[int] 和一个 Callable[[int], bool]，返回筛选后的 list[int]
T=TypeVar('T')
def filter_by(data:list[T],predicate:Callable[[T],bool])->list[T]:
    return [x for x in data if predicate(x)]
print(filter_by([1,2,3,4,5,6],lambda x:x>3))
# 4. 定义一个 Union 类型的函数，根据不同的输入类型执行不同逻辑
from typing import Union
def process_data(data:Union[int,str,list[int]])->Union[int,str,list[int]]:
    if isinstance(data,int):
        return data*2
    elif isinstance(data,str):
        return data.lower()
    elif isinstance(data,list):
        return [x*2 for x in data]
    else:
        raise TypeError(f"不支持的类型：{type(data)}")


# 1. 用单例模式写一个 AppConfig 类（存数据库配置、API URL 等）
class AppConfig:
    _instance=None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not hasattr(self,"_initialized"):
            self._initialized=True
            # 数据库配置
            self.DB_HOST="localhost"
            self.DB_PORT=3306
            self.DB_NAME="myapp"
            self.DB_USER="root"
            self.DB_PASSWORD="123456"
            # API配置
            self.API_URL="https://api.example.com"
            self.API_KEY="xxxxxxxxxxxxxxx"
            self.API_TIMEOUT=30
            # 应用配置
            self.DEBUG=True
            self.LOG_LEVEL="INFO"
    @property
    def DATABASE_URL(self)->str:
        return f"mysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
config=AppConfig()
print(config.DATABASE_URL)
print(config.API_URL)

# 2. 用工厂模式写一个 create_parser(file_type) 函数
#    file_type="csv" 返回 CsvParser，file_type="json" 返回 JsonParser
class Parser:
    def parse(self,data:str):
        raise NotImplementedError
    def serialize(self,data:Any)->str:
        raise NotImplementedError
class CsvParser(Parser):
    def parse(self,data:str)->List[list[[str]]]:
        lines=data.strip().split('\n')
        return [line.split(',')for line in lines]
    def serialize(self,data:List[List[str]]) ->str:
        return '\n'.join(','.join(row) for row in data)
class JsonParser(Parser):
    def parse(self,data:str)->Dict[str,Any]:
        import json
        return json.loads(data)
    def serialize(self,data:Dict[str,Any]) ->str:
        import json
        return json.dumps(data,indent=2,ensure_ascii=False)
def create_parser(file_type:str)->Parser:
    if file_type=="csv":
        return CsvParser()
    elif file_type=="json":
        return JsonParser()
    else:
        raise ValueError(f"不支持的文件类型：{file_type}")

csv_parser=create_parser("csv")
csv_data="name,age,city\nAlice,23,Beijing\nBob,33,Shanghai"
parsed_csv=csv_parser.parse(csv_data)
print("CSV解析结果：",parsed_csv)
print("CSV序列化：",csv_parser.serialize(parsed_csv))

# 3. 用观察者模式，给 TODO 管理器加上事件通知
#    添加任务时触发 "task_added" 事件（打印日志 + 统计任务数）
class EventBus:
    def __init__(self):
        self._handlers:Dict[str,List[Callable]]=defaultdict(list)
    def on(self,event:str):
        def decorator(handler:Callable)->Callable:
            self._handlers[event].append(handler)
            return handler
        return decorator
    def emit(self,event:str,*args,**kwargs):
        for handler in self._handlers.get(event,[]):
            handler(*args,**kwargs)
class TodoManager:
    def __init__(self):
        self.tasks:List[str]=[]
        self.bus=EventBus()
    def add_task(self,task:str):
        self.tasks.append(task)
        self.bus.emit("task_added",task,len(self.tasks))
manager=TodoManager()
@manager.bus.on("task_added")
def log_task(task:str,count:int):
    print(f"[日志]添加：{task},共{count}个")
@manager.bus.on("task_added")
def show_count(task:str,count:int):
    print(f"[统计]当前任务数：{count}")
manager.add_task("学习python")
manager.add_task("写作业")




