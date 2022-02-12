
from server.horoscopes.enums import get_all_horoscope_signs


def test_get_all_horoscope_signs():
    """Check returning signs of horoscopes."""
    signs_of_horoscope = get_all_horoscope_signs()

    # check length of returned horoscopes
    assert len(signs_of_horoscope) == 12
    # check all signs are strings
    assert all(
        isinstance(sign, str) for sign in signs_of_horoscope
    )
