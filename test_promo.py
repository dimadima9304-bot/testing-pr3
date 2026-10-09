# test_promo.py
import pytest
from promo import apply_promo

# 1. Счастливый путь
def test_student_promo_applies_ten_percent_discount():
    assert apply_promo(200.0, "STUDENT") == 180.0

# 2. Граничный случай (нижняя граница)
def test_sale50_promo_caps_at_zero():
    assert apply_promo(40.0, "SALE50") == 0.0

# 3. Пустой код
def test_empty_promo_code_returns_original_price():
    assert apply_promo(100.0, "") == 100.0

# 4. Отказ: неизвестный промокод
def test_unknown_promo_code_raises_value_error():
    with pytest.raises(ValueError, match="Неизвестный промокод"):
        apply_promo(100.0, "UNKNOWN")

# 5. Отказ: отрицательная цена
def test_negative_price_raises_value_error():
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        apply_promo(-50.0, "STUDENT")