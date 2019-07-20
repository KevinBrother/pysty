# 工资结算系统
"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta, abstractmethod 

class Emp(object, metaclass=ABCMeta):
    # 员工
    def __init__(self, name, position):
        self._name = name
        self._position = position
        self._salary = 0
    
    @abstractmethod
    def comp_salary(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    def __str__(self):
        return '%s职位的%s，这个月的工资为%d' % (self._position, self._name, self.salary)


class Manager(Emp):
    def __init__(self, name):
        super().__init__(name, '部门经理')

    # 部门经理
    def comp_salary(self):
        self._salary = 15000


class Programmer(Emp):

    # 程序员
    def __init__(self, name, hour=0):
        """ 
        :param hour: 工作小时数
        """
        super().__init__(name, '程序员')
        self._hour = hour

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour):
        self._hour = hour

    def comp_salary(self):
        self._salary = self._hour * 150


class Saler(Emp):
    # 销售员
    def __init__(self, name, salared=0):
        """ 
        :param salared: 销售额 
        """
        super().__init__(name, '销售员')
        self._salared = salared

    @property
    def salared(self):
        return self._salared

    @salared.setter
    def salared(self, salared):
        self._salared = salared

    def comp_salary(self):
        self._salary = 1200.0 + self._salared * 0.05

def main():
    emps = [Manager('张三'), Programmer('李四', 160), Saler('王五', 1000000),
            Programmer('赵六'),
            Saler('钱七')
        ]

    for emp in emps:
        if isinstance(emp, Programmer) and emp.hour == 0:
            emp.hour = int(input('%s该月的工作时间为：' % emp.name))
        elif isinstance(emp, Saler) and emp.salared == 0:
            emp.salared = float(input('%s该月的销售额为：' % emp.name))

        emp.comp_salary()
        print(emp)

if __name__ == "__main__":
    main()