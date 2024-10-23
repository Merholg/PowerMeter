#!/usr/bin/env python3
from dataclasses import dataclass


class SomeClass:
    def __init__(self, variable):
        super().__init__()
        self.variable = variable


@dataclass(frozen=True)
class DetalVolumes:
    D = {'classname': SomeClass, 'volvar': 10}


if __name__ == '__main__':
    s1 = SomeClass('081111h')
    s2 = DetalVolumes.D['classname'](DetalVolumes.D['volvar'])
    print(s1.variable)
    print(s2.variable)
    print(type(s2))
