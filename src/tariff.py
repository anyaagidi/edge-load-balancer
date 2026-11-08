def get_tariff(hour, spike=False):
    """Return the electricity price in $/kWh for an hour of the day (0 to 23)."""
    if 17 <= hour < 21:
        price = 0.30  # evening peak
    elif 7 <= hour < 17:
        price = 0.15  # daytime
    else:
        price = 0.08  # overnight

    if spike:
        price = price * 2  # simulated price spike

    return price


if __name__ == "__main__":
    for hour in range(24):
        print(hour, get_tariff(hour))