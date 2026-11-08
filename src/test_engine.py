from engine import decide_source


def test_expensive_and_full_battery():
    assert decide_source(0.30, 80) == "internal"


def test_battery_at_31_is_allowed():
    assert decide_source(0.30, 31) == "internal"


def test_battery_at_30_is_blocked():
    assert decide_source(0.30, 30) == "grid"


def test_battery_at_29_is_blocked():
    assert decide_source(0.30, 29) == "grid"


def test_price_at_threshold_stays_on_grid():
    assert decide_source(0.20, 80) == "grid"


def test_price_just_above_threshold_goes_internal():
    assert decide_source(0.21, 80) == "internal"


def test_cheap_price_stays_on_grid():
    assert decide_source(0.15, 80) == "grid"


def test_custom_threshold():
    assert decide_source(0.15, 80, threshold=0.10) == "internal"


if __name__ == "__main__":
    test_expensive_and_full_battery()
    test_battery_at_31_is_allowed()
    test_battery_at_30_is_blocked()
    test_battery_at_29_is_blocked()
    test_price_at_threshold_stays_on_grid()
    test_price_just_above_threshold_goes_internal()
    test_cheap_price_stays_on_grid()
    test_custom_threshold()
    print("All engine tests passed")