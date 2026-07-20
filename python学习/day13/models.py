# student类
class Student:
    def __init__(self,name:str,subject:str,score:int)->None:
        self.name=name
        self.subject=subject
        self.score=score
    def __str__(self)->str:
        return f"{self.name}|{self.subject}|{self.score}"
# gradeManager类
class GradeManager:
    def __init__(self,filename:str)->None:
        self.filename=filename
    def add(self,student:Student)->None:
        with open(self.filename,"a",encoding="utf-8")as f:
            f.write(f"{student.name}|{student.subject}|{student.score}\n")
    def list_all(self):
        with open(self.filename,"r",encoding="utf-8")as f:
            context=f.read()
        print(context)
    def avg(self,subject:str)->None:
        with open(self.filename,"r",encoding="utf-8")as f:
            lines=f.readlines()
            scores=[]
            for line in lines:
                line=line.strip()
                name,subj,score_str=line.split("|")
                if subj==subject:
                    scores.append(int(score_str))
        return sum(scores)/len(scores)
    def top(self,n:int)->None:
        with open(self.filename,"r",encoding="utf-8")as f:
            lines=f.readlines()
            student_total={}
            for line in lines:
                name,subj,score_str=line.strip().split("|")
                score=int(score_str)
                if name in student_total:
                    student_total[name]+=score
                else:
                    student_total[name]=score
        sorted_students=sorted(student_total.items(),key=lambda x:x[1],reverse=True)
        for i,(name,total)in enumerate(sorted_students[:n],start=1):
            print(f"第{i}名:{name} - {total}分")




