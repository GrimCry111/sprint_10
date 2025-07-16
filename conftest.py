import pytest
from ingredient import Ingredient
from bun import Bun
from burger import Burger

@pytest.fixture
def ingredient():
    return Ingredient("filling", "cheese", 1.5)

@pytest.fixture
def bun():
    return Bun("Sesame Bun", 1.2)

@pytest.fixture
def filling():
    return Ingredient("filling", "Cheese", 0.5)

@pytest.fixture
def sauce():
    return Ingredient("sauce", "Barbecue", 0.3)

@pytest.fixture
def burger_with_components(bun, filling, sauce):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(filling)
    burger.add_ingredient(sauce)
    return burger