import time
import tkinter
import tkinter.messagebox

from threading import Thread

class DownloadThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        # 做事
        time.sleep(10)
        tkinter.messagebox.showinfo('提示', '下载完成！')
        # 下载完成
        button1.config(state=tkinter.NORMAL)

def download():
    button1.config(state=tkinter.DISABLED)
    # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
    DownloadThread(daemon=True).start()


def show_about():
    tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')


def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()