# 1. 用 pyecharts 画一个折线图：展示你最近 30 天的学习时长变化（造数据）
import numpy as np
import pandas as pd
from pyecharts.charts import Line,Bar,Pie,Tab
from pyecharts import options as opts
days=[f"第{i}天"for i in range(1,31)]
hours=np.random.randint(2,8,30).tolist()
line_study = (
    Line()
    .add_xaxis(days)
    .add_yaxis("学习时长", hours, is_smooth=True)
    .set_global_opts(

        title_opts=opts.TitleOpts(title="最近30天学习时长"),
        xaxis_opts=opts.AxisOpts(name="天数"),
        yaxis_opts=opts.AxisOpts(name="小时"),
    )
)
line_study.render(r"G:\代码\PythonProject\daily_pratice\day29\study_hours.html")

# 2. 用 pandas 读取一组数据（自行创建 CSV），用 pyecharts 画柱状图展示不同类别的占比
# 造数据存 CSV
data = {
    "类别": ["电子产品", "服装", "食品", "家居", "图书"],
    "销售额": [35000, 28000, 42000, 19000, 15000],
}
df_sales = pd.DataFrame(data)
df_sales.to_csv(r"G:\代码\PythonProject\daily_pratice\day29\sales.csv", index=False,encoding="utf-8-sig")
# 读回来（模拟真实场景）
df = pd.read_csv(r"G:\代码\PythonProject\daily_pratice\day29\sales.csv")
print("读取的 CSV 数据：")
print(df)

bar = (
  Bar()
  .add_xaxis(df["类别"].tolist())
  .add_yaxis("销售额", df["销售额"].tolist())
  .set_global_opts(
      title_opts=opts.TitleOpts(title="各类别销售额"),
      xaxis_opts=opts.AxisOpts(name="类别"),
      yaxis_opts=opts.AxisOpts(name="销售额（元）"),
  )
)
bar.render(r"G:\代码\PythonProject\daily_pratice\day29\bar_chart.html")

# 3. 画一个饼图，展示你每天时间分配（学习、吃饭、睡觉、娱乐、运动）
time_data = [
      ("学习", 8),
      ("睡觉", 7),
      ("吃饭", 2),
      ("娱乐", 4),
      ("运动", 1),
      ("其他", 2),
  ]
pie = (
  Pie()
  .add("", time_data, radius=["30%", "55%"])
  .set_global_opts(title_opts=opts.TitleOpts(title="每日时间分配"))

.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
)
pie.render(r"G:\代码\PythonProject\daily_pratice\day29\pie_chart.html")
# 4. 把两张图放到一个 Tab 里，生成 dashboard.html

tab = Tab(page_title="数据看板")
tab.add(bar, "销售额柱状图")
tab.add(pie, "时间分配饼图")
tab.render(r"G:\代码\PythonProject\daily_pratice\day29\dashboard.html")
# 5. 模拟一家公司 12 个月的销售数据，画组合图（柱状图+折线图）
months = ["1月", "2月", "3月", "4月", "5月", "6月",
        "7月", "8月", "9月", "10月", "11月", "12月"]
sales = [120, 135, 148, 162, 175, 190, 210, 195, 220, 240,
260, 280]
profit_rate = [8.5, 9.2, 10.1, 11.0, 12.3, 13.5,
             14.0, 13.2, 14.8, 15.5, 16.1, 17.0]

bar2 = (
  Bar()
  .add_xaxis(months)
  .add_yaxis("销售额（万元）", sales)
  .set_global_opts(

title_opts=opts.TitleOpts(title="全年销售额与利润率"),
      yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
  )
)

line2 = (
  Line()
  .add_xaxis(months)
  .add_yaxis("利润率（%）", profit_rate, is_smooth=True,
             yaxis_index=1)  # 使用右侧 y 轴
)

bar2.overlap(line2)
bar2.render(r"G:\代码\PythonProject\daily_pratice\day29\combined_chart.html")

















