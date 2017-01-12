__author__ = 'Nick'


class Avatar:
    __image = None

    def __init__(self, image):
        self.__image = image | '/path/for/default/image'

    def set_image(self, image):
        self.__image = image

    def draw(self):
        #renders image
        print('draw image')

