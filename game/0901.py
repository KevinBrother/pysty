from abc import ABCMeta, abstractmethod
from random import randint

def Fighter(self, metaclass=ABCMeta):
    """ 战斗者 """
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def isAlive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


def Ultraman(Fighter):
    """ 奥特曼 """
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        # 初始化
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        # 普通攻击
        # 伤害在15～25区间
        other._hp -= randint(15, 25)

    def huge_attack(self, other):
        # 必杀技  打掉对方至少50点或四分之三的血
        # 消耗 50 mp
        if self._mp >= 50:
            self._mp -= 50

            injury = other._hp * 3 // 4
            injury = injury if other >= 50 else 50 
        else:
            attack(self, other)

    def magic_attack(self, others):
        # 魔法群体攻击  被攻击的群体 10 ～ 15
        # 消耗 20 mp
         if self._mp >= 20:
            self._mp -= 20

            for temp in others:
                if temp.isAlive():
                    attack(self, temp)

    def resume(self):
        # 回蓝 
        # 恢复 1～10mp
        self._mp += randint(1, 10)

    def __str__(self):
        # 自身信息
        return '%s奥特曼\n' % self._name + \
                '生命值： %s' % self._hp + \
                '魔法值： %s' % self._mp

""" def Monster(Fighter):
    # 怪兽 

    def attack(self, other):
        # 普通攻击
        # 伤害 10～20
         other._hp -= randint(10, 20)


    def __str__(self):
        # 自身信息
        return '%s怪兽\n' % self._name + \
            '生命值： %s' % self._hp

def is_any_alive(monsters):
    # '判断有没有活着的怪兽'
    for monster in monsters:
        if monster.isAlive:
            return True
    return False

def select_one_alive(monsters):
    # 选中一只活着的怪兽
    for monster in monsters:
        if monster.isAlive:
            return monster


def display_info(ultraman, monsters):
    # '显示怪兽和奥特曼的信息'
    print(ultraman)
    for monster in monsters:
        print(monster) """


def main():
    # 奥特曼60% 使用普攻，并恢复法力值
    # 30% 使用群体攻击
    # 10% 使用必杀技
    # 必杀技因为法力不足使用失败则普攻
    ultraman  = Ultraman('艾迪', 700, 100)


    pass


if __name__ == "__main__":
    main()