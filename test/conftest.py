import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def burger():
    """Возвращает чистый экземпляр бургера для каждого теста."""
    return Burger()

@pytest.fixture
def mock_bun():
    """Возвращает мок булочки с настроенными возвращаемыми значениями."""
    bun = Mock()
    bun.get_price.return_value = 100.0
    bun.get_name.return_value = "Флюоресцентная булка R2-D3"
    return bun

@pytest.fixture
def mock_ingredient():
    """Возвращает мок ингредиента с настроенными возвращаемыми значениями."""
    ingredient = Mock()
    ingredient.get_price.return_value = 50.0
    ingredient.get_name.return_value = "Соус Spicy-X"
    ingredient.get_type.return_value = "SAUCE"
    return ingredient