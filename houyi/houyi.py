from game.game import Game


class HouYi(Game):
    #如果在子类中重新定义了__init__，那么父类的__init__将会被覆盖
    def __init__(self):
        super().__init__(1000,100)
        self.defense = 88

    def houyi_fight(self,enemy_hp,enemy_power):
        while True:
            self.hp = self.hp+self.defense - enemy_power

            enemy_hp = enemy_hp - self.power
            print('我的血量{}'.format(self.hp))
            print('敌人血量{}'.format(enemy_hp))
            if self.hp <= 0:
                print('我太难了')
                break
            elif enemy_hp <= 0:
                print('wo赢了')
                break

hp = 1100
power = 200
houyi = HouYi()
houyi.houyi_fight(hp,power)

import pytest

class TestData:
    @pytest.mark.parametrize("a,b",[(10,20),(10,5),(3,9)])
    def test_data(self,a,b):
        print(a+b)
