BATTERY_CAPACITY_KWH = 400  # how much energy the battery can hold
LOAD_KW = 50                # how much power the building uses
CHARGE_KW = 25              # how fast the grid can recharge the battery


def update_battery(soc, source, hours=1):
    """Return the new battery level (%) after running on a source for some hours."""
    if source == "battery":
        soc = soc - (LOAD_KW * hours / BATTERY_CAPACITY_KWH) * 100
    else:
        soc = soc + (CHARGE_KW * hours / BATTERY_CAPACITY_KWH) * 100

    soc = max(0, min(100, soc))
    return soc


if __name__ == "__main__":
    soc = 100
    for hour in range(4):
        soc = update_battery(soc, "battery")
        print("battery hour", hour + 1, soc)
    for hour in range(4):
        soc = update_battery(soc, "grid")
        print("grid hour", hour + 1, soc)