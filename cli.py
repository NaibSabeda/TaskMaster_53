from task_manager import TaskMaster

def cli():
    tm = TaskMaster()
    print("=== TaskMaster 命令行工具 ===")
    while True:
        print("\n请选择操作：")
        print("1-添加任务 | 2-查看任务 | 3-标记完成 | 4-删除任务 | 0-退出")
        choice = input("> ")
        
        if choice == "0":
            print("退出程序...")
            break
        
        elif choice == "1":
            title = input("任务标题：")
            priority = input("优先级（high/medium/low）：") or "medium"
            deadline = input("截止日期（YYYY-MM-DD）：") or None
            desc = input("任务描述：") or ""
            tm.add_task(title, priority, deadline, desc)
            print("✅ 任务添加成功！")
        
        elif choice == "2":
            filter_priority = input("筛选优先级（all/high/medium/low）：") or "all"
            if filter_priority == "all":
                tm.list_tasks()
            else:
                tm.list_tasks(filter_priority)
        
        elif choice == "3":
            title = input("要完成的任务标题：")
            if tm.complete_task(title):
                print("✅ 任务标记为完成！")
            else:
                print("❌ 任务不存在！")
        
        elif choice == "4":
            title = input("要删除的任务标题：")
            if tm.delete_task(title):
                print("✅ 任务删除成功！")
            else:
                print("❌ 任务不存在！")
        
        else:
            print("❌ 无效选择，请重新输入！")

if __name__ == "__main__":
    cli()
