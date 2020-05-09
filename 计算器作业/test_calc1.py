import pytest
import yaml

from 计算器作业.calc import Calc


class TestCalc:
    @pytest.mark.parametrize(("a", "b", "c"), yaml.safe_load(open("calc_add.yml")))
    def test_add(self, a, b, c):
        self.calc = Calc()
        result = self.calc.add(a, b)
        print(result)
        assert c == result

    @pytest.mark.parametrize(("a", "b", "c"), yaml.safe_load(open("calc_div.yml")))
    def test_div(self, a, b, c):
        self.calc = Calc()
        result = self.calc.div(a, b)
        print(result)
        assert c == result


if __name__ == '__main__':
    pytest.main()
