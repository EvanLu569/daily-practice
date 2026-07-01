import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))  # 先将src目录加入Python路径
import pytest
from weatherpredictor.core import predict_tomorrow
import json


# ---------------------- 1. 参数化测试（覆盖正常+异常场景） ----------------------
@pytest.mark.parametrize(
    "temp, humidity, expected",
    [
        (32.0, 75.0, "雷阵雨"),    # 正常：雷阵雨
        (26.0, 45.0, "晴转多云"),  # 正常：晴转多云
        (20.0, 60.0, "阴天"),     # 正常：湿度温度均不达标
        (30.0, 75.0, "阴天"),     # 边界：温度=30（不满足>30）
        (26.0, 50.0, "阴天"),     # 边界：湿度=50（不满足<50）
        (-5.0, 50.0, ValueError), # 异常：温度为负
        (25.0, -10.0, ValueError) # 异常：湿度为负
    ]
)
def test_predict_parametrize(temp, humidity, expected):
    if expected is ValueError:
        with pytest.raises(ValueError, match="温度和湿度不能为负数"):
            predict_tomorrow(temp, humidity)
    else:
        assert predict_tomorrow(temp, humidity) == expected


# ---------------------- 2. Fixture模拟外部气象API ----------------------
@pytest.fixture
def mock_weather_api():
    """模拟气象API返回的JSON数据（含今日温度、湿度）"""
    return {
        "temp_today": 32.5,
        "humidity": 72.3,
        "source": "mock_meteor_api"
    }


def test_predict_with_mock_api(mock_weather_api):
    """使用Fixture数据测试预测逻辑"""
    temp = mock_weather_api["temp_today"]
    humidity = mock_weather_api["humidity"]
    assert predict_tomorrow(temp, humidity) == "雷阵雨"