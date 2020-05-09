import pytest
import yaml


class Calc:

    def add(self, a:float, b:float):
        return a + b

    def div(self, a:float, b:float):
        return (round(a / b,2))
