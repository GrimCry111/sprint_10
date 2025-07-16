from bun import Bun

class TestBun:
    def test_initialization(self, bun):
        """Проверяет корректную инициализацию атрибутов"""
        assert bun.name == "Sesame Bun"  # assert 1
        assert bun.price == 1.2          # assert 2


    def test_get_name_returns_correct_value(self, bun):
        """Проверяет, что метод get_name возвращает правильное имя булочки"""
        assert bun.get_name() == "Sesame Bun"  # assert 3


    def test_get_price_returns_correct_value(self, bun):
        """Проверяет, что метод get_price возвращает правильную цену булочки"""
        assert bun.get_price() == 1.2  # assert 4


    def test_empty_name_is_allowed(self):
        """Проверяет, что имя булочки может быть пустой строкой"""
        empty_name_bun = Bun("", 1.0)
        assert empty_name_bun.get_name() == ""  # assert 5


    def test_price_can_be_zero(self):
        """Проверяет, что цена булочки может быть равна нулю"""
        zero_price_bun = Bun("Free Bun", 0.0)
        assert zero_price_bun.get_price() == 0.0  # assert 6


    def test_price_can_be_negative(self):
        """Проверяет, что цена булочки может быть отрицательной (например, для скидок)"""
        negative_price_bun = Bun("Discount Bun", -0.5)
        assert negative_price_bun.get_price() == -0.5  # assert 7


    def test_numeric_name_is_allowed(self):
        """Проверяет, что имя булочки может содержать цифры и символы"""
        numeric_name_bun = Bun("Bun_123", 0.99)
        assert numeric_name_bun.get_name() == "Bun_123"  # assert 8