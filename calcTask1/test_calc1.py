import pytest
import yaml
import allure

from calcTask1.calc import Calc


class TestCalc:
    # @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.first
    @pytest.mark.parametrize(("a", "b", "c"), yaml.safe_load(open("calc_add.yml")))
    def test_add(self, a, b, c):
        # self.calc = Calc()
        result = Calc().add(a, b)
        print(result)
        assert c == result

    @pytest.mark.parametrize(("a", "b", "c"), yaml.safe_load(open("calc_jian.yml")))
    def test_jian(self, a, b, c):
        self.calc = Calc()
        result = self.calc.jian(a, b)
        print(result)
        assert c == result

    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize(("a", "b", "c"), yaml.safe_load(open("calc_div.yml")))
    def test_div(self, a, b, c):
        self.calc = Calc()
        result = self.calc.div(a, b)
        print(result)
        assert c == result

    @pytest.mark.parametrize(("a", "b", "c"), yaml.safe_load(open("calc_chen.yml")))
    def test_chen(self, a, b, c):
        self.calc = Calc()
        result = self.calc.chen(a, b)
        print(result)
        assert c == result


if __name__ == '__main__':
    pytest.main()
