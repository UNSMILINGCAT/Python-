class Recipe:
    """

    """

    def __init__(self):
        self.__recipe_names = dict()
        self.__recipe_names["乳酪"] = {"鸡蛋": 2, "牛奶": 1, "乳酪": 1}
        self.__recipe_names["蘑菇"] = {"鸡蛋": 2, "牛奶": 1, "乳酪": 1, "蘑菇": 2}
        self.__recipe_names["洋葱"] = {"鸡蛋": 2, "牛奶": 1, "乳酪": 1, "洋葱": 1}

    def get_all_recipe(self):
        """
        获取所有的配方
        :return:
        """
        return self.__recipe_names

    def get(self, recipe_name):
        """
        根据传入的食谱名，获取食谱
        :param recipe_name:
        :return:
        """
        if recipe_name in self.__recipe_names:
            return self.__recipe_names[recipe_name]
        else:
            return False

    def add(self, recipe_name, ingredients):
        """
        添加新的菜谱进去，如何菜谱为原有的则抛出错误
        :param str recipe_name:配方名称
        :param dict ingredients:配方材料
        :return:
        """
        if not recipe_name  in self.__recipe_names:
            self.__recipe_names[recipe_name] = ingredients
        else:
            print("菜谱已经存在，无法进行添加")

    def rename(self, recipe_name, recipe_rename):
        """
        对食谱进行重命名
        :param recipe_name:
        :param recipe_rename:
        :return:
        """
        if recipe_name not in self.__recipe_names:
            print("不存在该食谱，无法重命名")
        else:
            self.__recipe_names[recipe_rename] = self.__recipe_names.pop(recipe_name)
            return True
