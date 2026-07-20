import pytest
from my_functions import (
clean_text,
BankAccount,
InsufficientBalanceError,
is_valid_email,
TodoList
)
# 1. 给你之前写的 clean_text 函数写 3 个测试用例
def test_clean_text_basic():
    """测试基本清理功能"""
    assert clean_text("            hello world")=="hello world"
    assert clean_text("Python   Programming") == "python programming"
def test_clean_text_with_punctuation():
    """测试带标点符号的文本"""
    assert clean_text("  Hello, World!  ") == "hello, world!"
    assert clean_text("Python.   Programming.") == "python. programming."
def test_clean_text_edge_cases():
    """测试边界情况"""
    assert clean_text("") == ""  # 空字符串
    assert clean_text("   ") == ""  # 只有空格
    assert clean_text("SINGLE") == "single"  # 大写转小写
# 2. 给 BankAccount 类的 deposit 和 withdraw 写测试
def test_bank_account_deposit():
    """测试存款功能"""
    account = BankAccount(100)

    # 正常存款
    assert account.deposit(50) == 150
    assert account.get_balance() == 150

    # 多次存款
    account.deposit(30)
    account.deposit(20)
    assert account.get_balance() == 200


def test_bank_account_deposit_errors():
    """测试存款异常情况"""
    account = BankAccount(100)

    # 存款金额必须大于0
    with pytest.raises(ValueError, match="存款金额必须大于0"):
        account.deposit(0)

    with pytest.raises(ValueError, match="存款金额必须大于0"):
        account.deposit(-10)


def test_bank_account_withdraw():
    """测试取款功能"""
    account = BankAccount(200)

    # 正常取款
    assert account.withdraw(50) == 150
    assert account.get_balance() == 150

    # 取完所有钱
    account.withdraw(150)
    assert account.get_balance() == 0


def test_bank_account_withdraw_errors():
    """测试取款异常情况"""
    account = BankAccount(100)

    # 取款金额必须大于0
    with pytest.raises(ValueError, match="取款金额必须大于0"):
        account.withdraw(0)

    with pytest.raises(ValueError, match="取款金额必须大于0"):
        account.withdraw(-5)

    # 余额不足
    with pytest.raises(InsufficientBalanceError, match="余额不足！"):
        account.withdraw(200)


def test_bank_account_init():
    """测试初始化"""
    # 正常初始化
    account = BankAccount(100)
    assert account.get_balance() == 100

    # 默认余额为0
    account = BankAccount()
    assert account.get_balance() == 0

    # 负数余额报错
    with pytest.raises(ValueError, match="初始余额不能为负数"):
        BankAccount(-10)
# 3. 用 @pytest.mark.parametrize 给 is_valid_email 写 10 组测试数据
@pytest.mark.parametrize("email, expected", [
    # 有效的邮箱（应该返回 True）
    ("test@example.com", True),
    ("user123@gmail.com", True),
    ("john.doe@company.co.uk", True),
    ("info+123@test.org", True),
    ("admin@sub.domain.com", True),
    ("test_user-123@mail.net", True),
 # 无效的邮箱（应该返回 False）
    ("", False),  # 空字符串
    ("invalid-email", False),  # 没有 @
    ("@example.com", False),  # 缺少用户名
    ("test@", False),  # 缺少域名
    ("test@.com", False),  # 域名不完整
    ("test@example.", False),  # 缺少顶级域名
    ("test@example..com", False),  # 双点
    ("test space@example.com", False),  # 包含空格
    ("test@exam ple.com", False),  # 包含空格
    ("test@example", False),  # 缺少 .com
])
def test_is_valid_email(email, expected):
    """测试邮箱验证函数"""
    assert is_valid_email(email) == expected
# 4. 用 fixture 给 TodoList 的 add / done / delete 写测试
@pytest.fixture
def todo_list():
    """创建一个 TodoList 实例并添加一些任务"""
    tl = TodoList()
    # 添加几个初始任务供测试用
    tl.add("学习 Python")
    tl.add("写测试代码")
    tl.add("复习 pytest")
    return tl


def test_todo_add(todo_list):
    """测试添加任务"""
    # 添加新任务
    task = todo_list.add("完成项目")

    assert task["title"] == "完成项目"
    assert task["done"] is False
    assert task["id"] == 4  # 前面有3个任务

    # 验证任务列表长度
    assert len(todo_list.get_all()) == 4


def test_todo_add_empty_title(todo_list):
    """测试添加空标题（应该报错）"""
    with pytest.raises(ValueError, match="任务标题不能为空"):
        todo_list.add("")

    with pytest.raises(ValueError, match="任务标题不能为空"):
        todo_list.add("   ")


def test_todo_done(todo_list):
    """测试标记任务为已完成"""
    # 标记第一个任务为已完成
    task = todo_list.done(1)
    assert task["done"] is True

    # 验证只有第一个任务已完成
    done_tasks = todo_list.get_done()
    pending_tasks = todo_list.get_pending()

    assert len(done_tasks) == 1
    assert len(pending_tasks) == 2
    assert done_tasks[0]["id"] == 1
def test_todo_done_invalid_id(todo_list):
    """测试标记不存在的任务"""
    with pytest.raises(ValueError, match="任务 ID 999 不存在"):
        todo_list.done(999)


def test_todo_delete(todo_list):
    """测试删除任务"""
    # 删除第一个任务
    result = todo_list.delete(1)
    assert result is True

    # 验证任务已被删除
    all_tasks = todo_list.get_all()
    assert len(all_tasks) == 2
    assert all_tasks[0]["id"] == 2  # 原来的第2个变成了第1个
def test_todo_delete_invalid_id(todo_list):
    """测试删除不存在的任务"""
    with pytest.raises(ValueError, match="任务 ID 999 不存在"):
        todo_list.delete(999)


def test_todo_multiple_operations(todo_list):
    """测试多个操作的组合"""
    # 添加任务
    todo_list.add("测试组合操作")
    assert len(todo_list.get_all()) == 4

    # 完成任务
    todo_list.done(2)
    assert len(todo_list.get_done()) == 1

    # 删除任务
    todo_list.delete(3)
    assert len(todo_list.get_all()) == 3

    # 验证最终状态
    pending = todo_list.get_pending()
    assert len(pending) == 2

# 5. 用 pytest.raises 测试 withdraw 在余额不足时抛出 InsufficientBalanceError

def test_withdraw_insufficient_balance():
    """测试余额不足时抛出 InsufficientBalanceError"""
    account = BankAccount(100)

    # 尝试取出200（余额不足）
    with pytest.raises(InsufficientBalanceError) as exc_info:
        account.withdraw(200)

    # 验证异常信息
    assert "余额不足" in str(exc_info.value)
    assert "100" in str(exc_info.value)  # 显示当前余额

def test_withdraw_exact_balance():
    """测试取款金额等于余额（应该成功）"""
    account = BankAccount(100)
    account.withdraw(100)
    assert account.get_balance() == 0


def test_withdraw_after_multiple_operations():
    """测试多次操作后的余额不足"""
    account = BankAccount(500)

    # 多次取款
    account.withdraw(100)  # 余额: 400
    account.withdraw(200)  # 余额: 200
    account.deposit(50)  # 余额: 250

    # 尝试取出300（超过当前余额250）
    with pytest.raises(InsufficientBalanceError) as exc_info:
        account.withdraw(300)

    assert "250" in str(exc_info.value)  # 显示当前余额













