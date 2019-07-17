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
        
       
        # 4.打印自己的距离
        def __init__(self, x=0, y=0):
            """  
            1. 初始化
                ：param x:横坐标
                ：param y: 纵坐标
            """
            self.x = x
            self.y = y

        def move_to(self, dx, dy):
            """  
            #2.移动的增量
                ：param x:移动的x轴方向的值
                ：param y:移动的y轴方向的值
            """
            self.x += dx 
            self.y += dy 

        def distance(self, other):
            """  
            #3. 计算到另一个点的距离
                ：param x:移动的x轴方向的值
                ：param y:移动的y轴方向的值
            """
            dx = self.x - other.x 
            dy = self.y - other.y 

            return sqrt(dx ** 2 + dy ** 2)

        def __str__(self):
            return '(%s, %s)' % (str(self.x), str(self.y))

    def show_point():
        point1 = Point(1, 2)
        print('point1的坐标为：%s' % point1)
        point2 = Point(3, 5)
        dis = point1.distance(point2)
        print('p1和p2的距离为：%.2f' % dis)

    # show_point()

if __name__ == "__main__":
    main()