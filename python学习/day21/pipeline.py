import requests
from collections import defaultdict,Counter
import csv
from pathlib import Path

# 文章数据分析器
class PostAnalyzer:
    def __init__(self,url:str):
        self.url=url
        self.posts:list[dict]=[]
    # 从API获取数据
    def fetch_data(self)->list[dict]:
        response=requests.get(self.url,timeout=5)
        response.raise_for_status()
        self.posts=response.json()
        return self.posts
    # 筛选标题>min_length的文章
    def filter_long_titles(self,min_length:int=30)->list[dict]:
        return [p for p in self.posts if len(p["title"])>min_length]
    # 按userId分组
    def group_by_user(self,posts:list[dict])->dict[int,list[dict]]:
        grouped:dict[int,list[dict]]=defaultdict(list)
        for p in posts:
            grouped[p["userId"]].append(p)
        return dict(grouped)
    def count_by_user(self,posts:list[dict])->None:
        return Counter(p["userId"]for p in posts)
    # 导出为csv
    def export_csv(self,posts:list[dict],filepath:Path)->None:
        filepath.parent.mkdir(parents=True,exist_ok=True)
        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["userId", "id", "title"], extrasaction='ignore')
            writer.writeheader()
            writer.writerows(posts)
    # 一键运行
    def run(self, output_path: Path) -> None:
        """一键执行全流程"""
        print("1. 获取数据...")
        self.fetch_data()
        print(f"   共 {len(self.posts)} 篇文章")

        print("2. 筛选标题 > 30...")
        long_posts = self.filter_long_titles(30)
        print(f"   符合条件：{len(long_posts)} 篇")

        print("3. 按用户分组...")
        grouped = self.group_by_user(long_posts)
        for uid, items in grouped.items():
            print(f"   用户 {uid}：{len(items)} 篇")

        print("4. 统计...")
        counter = self.count_by_user(long_posts)
        for uid, count in counter.most_common():
            print(f"   用户 {uid}：{count} 篇")

        print("5. 导出 CSV...")
        self.export_csv(long_posts, output_path)
        print(f"   已导出到 {output_path}")

if __name__ == "__main__":
    analyzer = PostAnalyzer("https://jsonplaceholder.typicode.com/posts")
    analyzer.run(Path("day21/output.csv"))
