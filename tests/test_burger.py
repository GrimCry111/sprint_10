from burger import Burger
import pytest
import re

class TestBurger:
    def test_initialization(self):
        """Проверяет начальное состояние Burger"""
        burger = Burger()
        assert burger.bun is None  # assert 1
        assert burger.ingredients == []  # assert 2


    def test_set_buns(self, bun):
        """Проверяет установку булочки"""
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun  # assert 3


    def test_add_ingredient(self, burger_with_components, filling, sauce):
        """Проверяет добавление ингредиентов"""
        assert len(burger_with_components.ingredients) == 2  # assert 4
        assert burger_with_components.ingredients[0] == filling  # assert 5
        assert burger_with_components.ingredients[1] == sauce  # assert 6


    def test_remove_ingredient(self, burger_with_components, sauce):
        """Проверяет удаление ингредиента по индексу"""
        burger_with_components.remove_ingredient(0)
        assert len(burger_with_components.ingredients) == 1  # assert 7
        assert burger_with_components.ingredients[0] == sauce  # assert 8


    def test_move_ingredient(self, burger_with_components, filling, sauce):
        """Проверяет перемещение ингредиента"""
        burger_with_components.move_ingredient(0, 1)  # Перемещаем Cheese на позицию 1
        assert burger_with_components.ingredients == [sauce, filling]  # assert 9


    def test_get_price(self, burger_with_components):
        """Проверяет корректный расчет цены"""
        # Цена: (булочка * 2) + (сыр + соус) = (1.2 * 2) + (0.5 + 0.3) = 2.4 + 0.8 = 3.2
        assert burger_with_components.get_price() == pytest.approx(3.2)  # assert 10


    def test_get_receipt(self, burger_with_components):
        """Проверяет формат чека"""
        receipt = burger_with_components.get_receipt()

        # Проверяем структуру чека через регулярное выражение
        pattern = re.compile(r"""
            $====\ Sesame\ Bun\ ====$                # Первая булочка
            \n= filling Cheese =                      # Ингредиент 1
            \n= sauce Barbecue =                      # Ингредиент 2
            \n$====\ Sesame\ Bun\ ====$              # Вторая булочка
            \nPrice:\ 3\.?2\d?                        # Цена (например, 3.2 или 3.199999...)
        """, re.VERBOSE)

        assert pattern.search(receipt) is not None  # assert 11


    def test_empty_ingredients_list(self, bun):
        """Проверяет поведение при пустом списке ингредиентов"""
        burger = Burger()
        burger.set_buns(bun)
        assert burger.get_price() == pytest.approx(2.4)  # assert 12

        receipt = burger.get_receipt()

        # Проверяем структуру чека через регулярное выражение
        pattern = re.compile(r"""
            $====\ Sesame\ Bun\ ====$                # Первая булочка
            \n$====\ Sesame\ Bun\ ====$              # Вторая булочка
            \nPrice:\ 2\.?4\d?                        # Цена (например, 2.4 или 2.400000...)
        """, re.VERBOSE)

        assert pattern.search(receipt) is not None  # assert 13