# 奥特曼打小怪兽
from abc import ABCMeta, abstractmethod
from random import randint

class Fighter(object, metaclass=ABCMeta):
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
        print('set hp %d 和 self_hp %d' % (hp, self._hp))
        self._hp = hp if hp >= 0 else 0

    @property
    def isAlive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    """ 奥特曼 """
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        # 初始化
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        # 普通攻击
        # 伤害在15～25区间
        dmg = randint(15, 25)
        other.hp -= dmg
        return dmg

    def huge_attack(self, other):
        # 必杀技  打掉对方至少50点或四分之三的血
        # 消耗 50 mp
        if self._mp >= 50:
            self._mp -= 50

            dmg = other.hp * 3 // 4
            dmg = dmg if other.hp >= 50 else 50 
            other.hp -= dmg
            return True, dmg
        else:
            return False, self.attack(other)

    def magic_attack(self, others):
        # 魔法群体攻击  被攻击的群体 10 ～ 15
        # 消耗 20 mp
        if self._mp >= 20:
            self._mp -= 20

            dmg = randint(10, 15)
            for temp in others:
                if temp.isAlive:
                    temp.hp -= dmg

            return True, dmg
        else:
            return False, 0

    def resume(self):
        # 回蓝 
        # 恢复 1～10mp
        rd_mp = randint(1, 10)
        self._mp += rd_mp 
        return rd_mp

    def __str__(self):
        # 自身信息
        return '%s奥特曼\n' % self._name + \
                '生命值： %s' % self._hp + \
                '魔法值： %s' % self._mp


class Monster(Fighter):
    # 怪兽 

    def attack(self, other):
        # 普通攻击
        # 伤害 10～20
        dmg = randint(10, 20)
        other.hp -= dmg
        return dmg


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
        print(monster)


def main():
    # 奥特曼60% 使用普攻，并恢复法力值
    # 30% 使用群体攻击
    # 10% 使用必杀技
    # 必杀技因为法力不足使用失败则普攻
    u  = Ultraman('艾迪', 1000, 300)
    m1 = Monster('卡布达', 250)
    m2 = Monster('皮卡超人', 500)
    m3 = Monster('咀嚼兽', 750)
    ms = [m1, m2, m3]


    round = 1

    while u.isAlive and is_any_alive(ms):
        print('--------第%d回合---------' % round)
        rd = randint(1, 10)
        if rd <= 5:
            monster = select_one_alive(ms)
            print('%s奥特曼对%s怪兽造成了%d点伤害' % (u.name, monster.name, u.attack(monster)))
            print('%s奥特曼回了%d点蓝' % (u.name, u.resume()))
        elif rd <= 8:
            mgc_atk = u.magic_attack(ms)
            if mgc_atk[0]:
                # print('%s奥特曼使用魔法攻击对怪兽们各造成了%d点伤害' % (u.name, rd))
                print('%s奥特曼使用魔法攻击对怪兽们造成了%d伤害' % (u.name, mgc_atk[1]))
            else:
                print('%s奥特曼使用魔法失败' % u.name)
                
        else:
            monster = select_one_alive(ms)
            huge_atk = u.huge_attack(monster)
            if huge_atk[0]:
                print('%s奥特曼对%s怪兽使用了必杀技造成了%d点伤害' % (u.name, monster.name, huge_atk[1]))
            else:
                print('%s奥特曼对%s怪兽造成了%d点伤害' % (u.name, monster.name, huge_atk[1]))
                print('%s奥特曼回了%d点蓝' % (u.name, u.resume()))

        for m in ms:
            if m.isAlive:
                print('%s怪兽对%s奥特曼造成了%d点伤害' % (m.name, u.name, m.attack(u)))
                
            
        display_info(u, ms)
        round += 1

    if u.isAlive:
        print('----------%s奥特曼胜利了----------' % u.name)
    else:
        print('----------小怪兽胜利了----------')
        # print('----------%s怪兽胜利了----------' % ms)

if __name__ == "__main__":
    main()