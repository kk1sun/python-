import pytest
import yaml

from calcTask1.calc import Calc


class TestCalc:
    @pytest.mark.parametrize(("a", "b", "c"), yaml.safe_load(open("calcTask1/calc_add.yml")))
    def test_add(self, a, b, c):
        self.calc = Calc()
        result = self.calc.add(a, b)
        print(result)
        assert c == result

    def test_div(self):
        self.calc = Calc()
        result = self.calc.div(2, 2)
        print(result)
        assert 1 == result


if __name__ == '__main__':
    pytest.main()
