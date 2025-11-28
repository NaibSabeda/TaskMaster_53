from task_manager import TaskMaster

# 初始化任务管理器
tm = TaskMaster()

# 添加任务
print("=== 添加任务 ===")
tm.add_task(
    title="完成GitHub项目实践",
    priority="high",
    deadline="2025-12-10",
    description="包含分支管理、文档完善、功能开发"
)
tm.add_task(
    title="学习五看三定分析",
    priority="medium",
    deadline="2025-11-30"
)

# 列出所有任务
print("\n=== 所有任务 ===")
tm.list_tasks()

# 筛选高优先级任务
print("\n=== 高优先级任务 ===")
tm.filter_tasks("high")

# 标记任务完成
print("\n=== 标记任务完成 ===")
tm.complete_task("学习五看三定分析")
tm.list_tasks()

# 删除任务
print("\n=== 删除任务 ===")
tm.delete_task("测试任务")
tm.list_tasks()
