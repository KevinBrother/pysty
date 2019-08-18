# image

from PIL import Image

def suolue():
    image = Image.open('./static/desk.png')
    size = 128, 128
    image.thumbnail(size)
    image.show()

    # try:
    #     with open('./static/fromTest1.png', 'wb') as fs2:
    #         fs2.write(image.thumbnail(size))
    # except FileNotFoundError as e:
    #     print('无法打开指定的文件', e)


def main():
    suolue()


if __name__ == "__main__":
    main()