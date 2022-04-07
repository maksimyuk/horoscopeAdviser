from server.horoscopes.enums import (
    HoroscopeSigns,
    get_all_horoscope_signs,
    get_horoscope_sign_enum_by_value,
)


def test_get_all_horoscope_signs():
    """Check returning signs of horoscopes."""
    signs_of_horoscope = get_all_horoscope_signs()

    # check length of returned horoscopes
    assert len(signs_of_horoscope) == 12
    # check all signs are strings
    assert all(isinstance(sign, str) for sign in signs_of_horoscope)


def test_get_horoscope_sign_enum_by_value():
    """Check get enum by any value."""
    sign = HoroscopeSigns.LEO

    assert get_horoscope_sign_enum_by_value(sign.value.lower()) == sign
