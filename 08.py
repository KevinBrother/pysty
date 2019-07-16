def main():

    class Clock(object):
        def __init__(self, hour, minute, second):
            self.hour = hour
            self.minute = minute
            self.second = second 
       
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
        clock = Clock(23, 59, 58)
        while True: 
            from time import sleep
            print(clock.show())
            sleep(1)
            clock.run()
    
   
   # show_clock()


    from math import sqrt

    class Point(object):

        def __init__(self, x=0, y=0):
            """初始化方法
            
            :param x: 横坐标
            :param y: 纵坐标
            """
            self.x = x
            self.y = y

        def move_to(self, x, y):
            """移动到指定位置
            
            :param x: 新的横坐标
            "param y: 新的纵坐标
            """
            self.x = x
            self.y = y

        def move_by(self, dx, dy):
            """移动指定的增量
            
            :param dx: 横坐标的增量
            "param dy: 纵坐标的增量
            """
            self.x += dx
            self.y += dy

        def distance_to(self, other):
            """计算与另一个点的距离
            
            :param other: 另一个点
            """
            dx = self.x - other.x
            dy = self.y - other.y
            return sqrt(dx ** 2 + dy ** 2)

        def __str__(self):
            return '(%s, %s)' % (str(self.x), str(self.y))

    def show_point():
       

    abc()

if __name__ == "__main__":
    main()