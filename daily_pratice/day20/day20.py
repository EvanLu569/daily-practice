'''
pytest测试基础
pytest就是自动检查代码是否正确的工具
'''
# 安装和基本用法
# pip install pytest
import pytest
def add(a:int,b:int)->int:
    return a+b;
def test_add_position():
    assert add(2,3)==5  # assert  断言 eg.我断言。。。是正确的
def test_add_negative():
    assert add(-2,3)==1
def test_add_zero():
    assert add(5,0)==5

# 测试异常
def divide(a:float,b:float)->float:
    if b==0:
        raise ZeroDivisionError("不能除以0")
    return a/b
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError): # 测试异常raises 检查是否报错
        divide(10,0)

# 参数化测试（一组输入输出，一次测完）
@pytest.mark.parametrize("a,b,expected",[
    (2,3,5),
    (-2,3,1),
    (0,0,0),
    (100,200,300),
])
def test_add(a,b,expected):
    assert add(a,b)==expected

# fixture 准备测试数据
@pytest.fixture
def sample_tasks():
    return [
        {"title":"背书","done":False},
        {"title":"刷题","done":True},
        {"title":"写作业","done":False}
    ]
def test_count_undone(sample_tasks):
    undone=[t for t in sample_tasks if not t["done"]]
    assert len(undone)==2
def test_all_have_title(sample_tasks):
    for task in sample_tasks:
        assert "title"in task

