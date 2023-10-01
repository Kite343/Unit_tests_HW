
class ListComparison:
    def __init__(self, list_1: list[int | float], list_2: list[int | float]):
        self.list_1 = self.__checking_arg(list_1)
        self.list_2 = self.__checking_arg(list_2)

    def __checking_arg(self, list_arg):
        if not isinstance(list_arg, list):
            raise TypeError(f'Argument {list_arg} must be a list type')
        for item in list_arg:
            if not isinstance(item, (int, float)):
                raise ValueError(f'Element {item} in {list_arg} not int or float')
        return list_arg

    def get_average_lists(self):
        return (self.__find_average(self.list_1), self.__find_average(self.list_2))

    def __find_average(self, lst):
        if len(lst):
            return sum(lst) / len(lst)
        return 0.0

    def list_comparison(self):
        average_1, average_2 = self.get_average_lists()
        if average_1 > average_2:
            return "Первый список имеет большее среднее значение"
        elif average_2 > average_1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"

# if __name__ == '__main__':
    # a = ListComparison([1, 4, 7, "f"], 4)
    # a = ListComparison([1, 4, 7], 4)
    # a = ListComparison([1, 4, 7], [4, 2])
    # print(a.get_average_lists())
    # print(a.list_comparison())
