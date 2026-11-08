TARIFF_THRESHOLD = 0.20  # switch to battery when price is above this ($/kWh)
MIN_SOC = 30             # never use the battery below this level (%)


def decide_source(tariff, soc, threshold=TARIFF_THRESHOLD):
    """Return "battery" or "grid" based on the price and battery level."""
    if tariff > threshold and soc > MIN_SOC:
        return "battery"
    return "grid"


if __name__ == "__main__":
    print(decide_source(0.30, 80))
    print(decide_source(0.30, 30))
    print(decide_source(0.15, 80))
    print(decide_source(0.30, 31))