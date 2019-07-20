# 工资结算系统
"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

class Emp(object):
    # 员工
    pass

class Manager(Emp):
    # 部门经理
    pass

class Programmer(Emp):
    # 程序员
    pass

class Saler(Emp):
    # 销售员
    pass