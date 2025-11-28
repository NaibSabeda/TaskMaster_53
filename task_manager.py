import json
from datetime import datetime

class TaskMaster:
    def __init__(self, data_file="tasks.json"):
        self.data_file = data_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """加载本地任务数据"""
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        """保存任务到本地文件"""
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)

    def add_task(self, title, priority="medium", deadline=None, description="", category="默认", creator="未知"):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority.lower(),
            "deadline": deadline,
            "description": description,
            "category": category,  # 保留分类字段
            "creator": creator,    # 保留创建人字段
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def filter_tasks(self, priority):
        """按优先级筛选任务"""
        return [t for t in self.tasks if t["priority"] == priority.lower()]

    def complete_task(self, title):
        """标记任务为完成"""
        for task in self.tasks:
            if task["title"] == title:
                task["completed"] = True
                self.save_tasks()
                return True
        return False

    def delete_task(self, title):
        """删除任务"""
        original_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["title"] != title]
        if len(self.tasks) < original_len:
            self.save_tasks()
            return True
        return False

if __name__ == "__main__":
    tm = TaskMaster()
    tm.add_task("测试任务", "high", "2025-12-01", "这是测试内容")
    # 注意：原代码中调用了未定义的list_tasks()方法，这里注释掉以避免错误
    # tm.list_tasks()