import pytest
from unittest.mock import Mock


class TestBurger:

    def test_set_buns_success(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_success(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_success(self, burger, mock_ingredient):
        mock_ingredient_2 = Mock()
        burger.ingredients = [mock_ingredient, mock_ingredient_2]

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_2

    # Параметризация: проверяем перемещение элементов в разных направлениях
    @pytest.mark.parametrize("index_from, index_to, expected_order", [
        (0, 2, [1, 2, 0]),  # Перемещение первого элемента в конец
        (2, 0, [2, 0, 1]),  # Перемещение последнего элемента в начало
        (1, 0, [1, 0, 2])  # Перемещение среднего элемента в начало
    ])
    def test_move_ingredient_success(self, burger, index_from, index_to, expected_order):
        mock_ingredients = [Mock(), Mock(), Mock()]
        burger.ingredients = mock_ingredients.copy()

        burger.move_ingredient(index_from, index_to)

        assert burger.ingredients == [mock_ingredients[i] for i in expected_order]

    # Параметризация: проверяем расчет стоимости с разными ценами
    @pytest.mark.parametrize("bun_price, ingredients_prices, expected_total", [
        (100, [50, 50], 300),  # Обычный бургер: 100*2 + 50 + 50 = 300
        (200, [], 400),  # Бургер без ингредиентов (только булки): 200*2 = 400
        (0, [100, 200], 300),  # Бесплатные булки, платные ингредиенты: 0*2 + 100 + 200 = 300
    ])
    def test_get_price_success(self, burger, bun_price, ingredients_prices, expected_total):
        # Настраиваем цену булки для конкретного теста
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        # Добавляем ингредиенты с нужными ценами
        for price in ingredients_prices:
            mock_ingr = Mock()
            mock_ingr.get_price.return_value = price
            burger.add_ingredient(mock_ingr)

        assert burger.get_price() == expected_total

    def test_get_receipt_success(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        # Формируем ожидаемый результат в соответствии с логикой метода get_receipt
        expected_receipt = (
            "(==== Флюоресцентная булка R2-D3 ====)\n"
            "= sauce Соус Spicy-X =\n"
            "(==== Флюоресцентная булка R2-D3 ====)\n\n"
            "Price: 250.0"
        )

        assert burger.get_receipt() == expected_receipt