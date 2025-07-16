from ingredient import Ingredient

class TestIngredient:
    def test_initialization(self, ingredient):
        """Проверяет корректную инициализацию атрибутов"""
        assert ingredient.type == "filling"  # assert 1
        assert ingredient.name == "cheese"   # assert 2
        assert ingredient.price == 1.5       # assert 3


    def test_get_type_returns_correct_value(self, ingredient):
        """Проверяет, что метод get_type возвращает правильный тип ингредиента"""
        assert ingredient.get_type() == "filling"  # assert 4


    def test_get_name_returns_correct_value(self, ingredient):
        """Проверяет, что метод get_name возвращает правильное имя ингредиента"""
        assert ingredient.get_name() == "cheese"  # assert 5


    def test_get_price_returns_correct_value(self, ingredient):
        """Проверяет, что метод get_price возвращает правильную цену ингредиента"""
        assert ingredient.get_price() == 1.5  # assert 6


    def test_price_can_be_zero(self):
        """Проверяет, что цена может быть равна нулю"""
        zero_price_ingredient = Ingredient("sauce", "lettuce", 0.0)
        assert zero_price_ingredient.get_price() == 0.0  # assert 7


    def test_price_can_be_negative():
        """Проверяет, что цена может быть отрицательной (например, для скидок)"""
        negative_price_ingredient = Ingredient("filling", "discount", -0.5)
        assert negative_price_ingredient.get_price() == -0.5  # assert 8


    def test_empty_name_is_allowed():
        """Проверяет, что пустое имя допустимо"""
        empty_name_ingredient = Ingredient("sauce", "", 1.0)
        assert empty_name_ingredient.get_name() == ""  # assert 9


    def test_numeric_name_is_allowed():
        """Проверяет, что имя может содержать цифры"""
        numeric_name_ingredient = Ingredient("filling", "sauce_123", 0.99)
        assert numeric_name_ingredient.get_name() == "sauce_123"  # assert 10