from abc import ABC
from collections.abc import Iterable
from typing import Iterable as itertype


class Summable(Iterable, ABC):

    @property
    def sum(self):
        return self.__sum()

    def __sum(self):
        total = 0
        for values in self:
            if isinstance(values, itertype):
                total += Summable.__sum(values)

            else:
                total += values

        return total


class SingleValue(Summable):

    def __init__(self, value):
        self._value = value

    def __iter__(self):
        yield self._value


class ManyValues(list, Summable):
    pass


if __name__ == '__main__':

    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)
    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    all_values.append(12) #accept plain values too

    print(all_values.sum)
