from dataclasses import dataclass
import re


@dataclass
class myLove:
    a: int

    def summ(self) -> int:
        return self.a * 2

    def helllo():
        print('32323')

    def __str__(self):
        return '32'


test = myLove(2)
print(test.summ())
