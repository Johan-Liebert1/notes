class Direction:
    def __init__(self) -> None:
        self.__dict = {}

    @property
    def up(self):
        return self.__dict.get('up')

    @up.setter
    def up(self, value):
        self.__dict['up'] = value

    @property
    def down(self):
        return self.__dict.get('down')

    @down.setter
    def down(self, value):
        self.__dict['down'] = value

    @property
    def left(self):
        return self.__dict.get('left')

    @left.setter
    def left(self, value):
        self.__dict['left'] = value

    
    @property
    def right(self):
        return self.__dict.get('right')

    @right.setter
    def right(self, value):
        self.__dict['right'] = value


