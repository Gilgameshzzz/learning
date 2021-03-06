"""__author__ = 余婷"""
import json

# 获取数据
def download_data():
    with open('./data.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
        return content['data']

class Data:
    """数据类"""
    def __init__(self):
        self.type = ''
        self.text = ''
        self.user_id = ''
        self.name = ''
        self.screen_name = ''
        self._width = 0
        self._height = 0
        self._themes = None

    #  _width的getter和setter
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        self._width = int(width)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = int(height)

    @property
    def themes(self):
        if not self._themes:
            return '无'
        return self._themes

    # 根据字典创建对象
    @classmethod
    def creat_data(cls, dict1):
        data = cls()
        for key in dict1:
            # 处理特殊情况
            if key == 'width':
                data.width = dict1[key]
                continue
            if key == 'height':
                data.height = dict1[key]
                continue
            if key == 'themes':
                data._themes = dict1[key]
                continue
            # 正常情况
            data.__setattr__(key, dict1[key])

        return data


if __name__ == '__main__':
    print(download_data())
    datas = []
    for dict1 in download_data():
        # 通过字典创建对象
        data = Data.creat_data(dict1)
        # 将创建的对象存起来
        datas.append(data)

    print(datas[1].user_id)
