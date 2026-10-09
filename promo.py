def apply_promo(price: float | int, code: str | None = None) -> float:
    """Вычисляет итоговую цену с учетом промокода."""
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")

    if not code:
        return float(price)

    code_clean = code.strip().upper()

    if code_clean == "STUDENT":
        return float(price * 0.9)
    elif code_clean == "SALE50":
        return float(max(0.0, price - 50))
    else:
        raise ValueError(f"Неизвестный промокод: {code}")