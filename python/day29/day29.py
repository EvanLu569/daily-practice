from pyecharts.charts import Line
from pyecharts import options as opts

# 数据准备
months = ["1月", "2月", "3月", "4月", "5月", "6月"]
sales_a = [120, 135, 148, 162, 175, 190]
sales_b = [80, 90, 105, 115, 130, 155]

# 折线图
line=(
    Line()
    .add_xaxis(months)
    .add_yaxis("产品A",sales_a,is_smooth=True)
    .add_yaxis("产品B",sales_b,is_smooth=True)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="上半年销售额趋势"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
    )
)
line.render("line_chart.html")

# 柱状图
from pyecharts.charts import Bar

bar = (
    Bar()
    .add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
    .add_yaxis("销售额", [120, 135, 148, 162, 175, 190])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="月度销售额"),
        xaxis_opts=opts.AxisOpts(name="月份"),
    )
)
bar.render("bar_chart.html")

# 饼图
from pyecharts.charts import Pie

data = [("Python", 40), ("Java", 25), ("JavaScript", 20), ("C++", 10), ("Go", 5)]

pie = (
    Pie()
    .add("", data, radius=["30%", "55%"])    # 环形图
    .set_global_opts(title_opts=opts.TitleOpts(title="编程语言使用比例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)
pie.render("pie_chart.html")

# 散点图
from pyecharts.charts import Scatter

x = [161, 165, 170, 172, 175, 178, 180, 182, 185, 188]
y = [53, 57, 60, 62, 65, 70, 72, 75, 80, 85]

scatter = (
    Scatter()
    .add_xaxis(x)
    .add_yaxis("身高体重分布", y)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="身高体重散点图"),
        xaxis_opts=opts.AxisOpts(name="身高(cm)"),
        yaxis_opts=opts.AxisOpts(name="体重(kg)"),
    )
)
scatter.render("scatter_chart.html")

# 组合图表 — 多图叠加
from pyecharts.charts import Bar, Line
from pyecharts.charts import Grid

bar = (
    Bar()
    .add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
    .add_yaxis("销售额", [120, 135, 148, 162, 175, 190])
)

line = (
    Line()
    .add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
    .add_yaxis("增长率(%)", [0, 12.5, 9.6, 9.5, 8.0, 8.6])
)

bar.overlap(line)    # 折线叠加到柱状图上
bar.render("combined_chart.html")

# 数据大屏 — Tab 多图表
from pyecharts.charts import Tab, Bar, Line, Pie

tab = Tab()
tab.add(bar, "柱状图")
tab.add(line, "折线图")
tab.add(pie, "饼图")
tab.render("dashboard.html")

# 完整数据可视化案例
from pyecharts.charts import Bar, Line, Pie
from pyecharts import options as opts
import pandas as pd

# 数据准备
df = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月", "6月"],
    "销售额": [120, 135, 148, 162, 175, 190],
    "成本": [80, 85, 92, 98, 105, 110],
    "客流量": [1200, 1350, 1500, 1650, 1800, 2000],
})

# 计算利润和利润率
df["利润"] = df["销售额"] - df["成本"]
df["利润率"] = (df["利润"] / df["销售额"] * 100).round(1)

# 图1：销售额 vs 成本 vs 利润（分组柱状图）
bar = (
    Bar()
    .add_xaxis(df["月份"].tolist())
    .add_yaxis("销售额", df["销售额"].tolist())
    .add_yaxis("成本", df["成本"].tolist())
    .add_yaxis("利润", df["利润"].tolist())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="月度经营数据"),
        yaxis_opts=opts.AxisOpts(name="金额（万元）"),
    )
)

# 图2：利润率趋势（折线图）
line = (
    Line()
    .add_xaxis(df["月份"].tolist())
    .add_yaxis("利润率(%)", df["利润率"].tolist(), is_smooth=True, color="red")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="利润率趋势"),
    )
)

bar.render("business_bar.html")
line.render("profit_rate_line.html")
print("图表已生成，用浏览器打开 HTML 文件查看")