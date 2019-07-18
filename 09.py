# utf-8
def main():
    class Person(object):

        def __init__(self, name, age):
            self._name = name
            self._age = age

        # 访问器 - getter方法
        @property
        def name(self):
            return self._name

        # 访问器 - getter方法
        @property
        def age(self):
            return self._age

        # 修改器 - setter方法
        @age.setter
        def age(self, age):
            self._age = age

        def play(self):
            if self._age <= 16:
                print('%s正在玩飞行棋.' % self._name)
            else:
                print('%s正在玩斗地主.' % self._name)

    def show_person1():
        person1 = Person('阿三', 10)
        person1.play()
        person1.age = 20
        person1.play()
        person1._age = 10
        person1.play()

 

    # show_person()

    class Per(object):

        # 限定Person对象只能绑定_name, _age和_gender属性
        __slots__ = ('_name', '_age', '_gender')

        def __init__(self, name, age):
            self._name = name
            self._age = age

        @property
        def name(self):
            return self._name

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, age):
            self._age = age

        def play(self):
            if self._age <= 16:
                print('%s正在玩飞行棋.' % self._name)
            else:
                print('%s正在玩斗地主.' % self._name)
    
    def show_per():
        person = Per('王大锤', 22)
        person.play()
        person._gender = '男'
        # AttributeError: 'Person' object has no attribute '_is_gay'
        # person._is_gay = True

    # show_per()

    from time import time, localtime, sleep


    class Clock(object):
        def __init__(self, hour=0,minute=0,second=0):
            self.hour = hour
            self.minute = minute
            self.second = second

        @classmethod
        def now(cls):
            ctime = localtime(time())
            print('time %s' % time())
            print(ctime)
            return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

        def run(self):
            self.second += 1
            if self.second == 60:
                self.second = 0
                self.minute += 1
                if self.minute == 60:
                    self.minute = 0
                    self.hour += 1
                    if self.hour == 24:
                        self.hour = 0

        def show(self):
            return '%02d:%02d:%02d' % \
            (self.hour, self.minute, self.second)


    def show_clock():
        clock = Clock.now()
        while True:
            print(clock.show())
            sleep(1)
            clock.run()
    
    # show_clock()

    # 继承
    class Student(Person):
        def __init__(self, name, age, grade):
            super().__init__(name, age)
            self._grade = grade

        @property
        def grade(self):
            return self.grade

        @grade.setter    
        def grade(self, grade):
            self._grade = grade

        def study(self, course):
            return ('%s的%s正在学习%s' % (self._grade, self._name, course))


    def show_BasePerson():
        student1 = Student('张三', 11, '三年级')
        student1.play()
        print(student1.study('历史'))

    # show_BasePerson()

    # 多态
    from abc import ABCMeta, abstractmethod
    class Pet(object, metaclass=ABCMeta):
        
        def __init__ (self, nickname):
            self._nickname = nickname

        @abstractmethod    
        def make_voice(self):
            # 发出声音
            pass

    class Dog(Pet):

        def make_voice(self):
            print('%s发出旺旺旺的叫声' % self._nickname)

    class Cat(Pet):
        def make_voice(self):
            print('%s发出喵喵喵的叫声' % self._nickname)

    def showPet():
        dog = Dog('大黄')
        cat = Cat('小橘')
        dog.make_voice()
        cat.make_voice()

    showPet()

if __name__ == "__main__":
    main()
