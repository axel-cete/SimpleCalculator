def calculate_import_cost(lcd_price, kurs, ship_size, piece):
    modal = lcd_price * kurs

    if ship_size == 20:
        ship_price = 11000
        ppjk = 12_500_000
    elif ship_size == 40:
        ship_price = 15000
        ppjk = 15_000_000
    else:
        raise ValueError("Invalid ship size")

    price_per_piece = ship_price / piece
    rupiah_price_per_piece = price_per_piece * kurs
    ppjk_per_piece = ppjk / piece

    pib = 0.21 * (modal + rupiah_price_per_piece)
    final_modal = modal + pib + ppjk_per_piece

    return {
        "modal": modal,
        "shipping_per_piece": rupiah_price_per_piece,
        "ppjk_per_piece": ppjk_per_piece,
        "pib": pib,
        "final_modal": final_modal
    }