from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def my_job(i):
    print(i)


# 1. apscheduler 简单测试
# sched = BlockingScheduler()
# sched.add_job(my_job, 'interval', seconds=5, args=['学会了'], jitter=120)  # 每 5 秒钟运行一次，其中 interval 为固定时间间隔调度。jitter 振动参数，给每次触发添加一个随机浮动秒数，一般适用于多服务器，避免同时运行造成服务拥堵
# sched.start()

# 2. date 触发器定时执行
# scheduler = BlockingScheduler()
# # datetime类型（用于精确时间）
# scheduler.add_job(my_job, 'date', run_date=datetime(2024, 5, 19, 14, 27, 30), args=['测试任务'])
#
# scheduler.start()

# 3. corn 触发器
scheduler = BlockingScheduler()
"""
表达式\t参数类型\t描述
*\t所有\t通配符。例：minutes=*即每分钟触发
*/a\t所有\t可被a整除的通配符。
a-b\t所有\t范围a-b触发
a-b/c\t所有\t范围a-b，且可被c整除时触发
xth y\t日\t第几个星期几触发。x为第几个，y为星期几
last x\t日\t一个月中，最后的星期几触发
last\t日\t一个月最后一天触发
x,y,z\t所有\t组合表达式，可以组合确定值或上方的表达式
"""
# 在每年 1-3、7-9 月份中的每个星期一、二中的 00:00, 01:00, 02:00 和 03:00 执行 job_func 任务
scheduler.add_job(my_job, 'cron', month='1-3,7-9', day='0, tue', hour='0-3', args=['测试任务'])
scheduler.start()
