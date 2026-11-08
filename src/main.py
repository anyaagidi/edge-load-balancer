from tariff import get_tariff
from battery import update_battery, LOAD_KW
from engine import decide_source, TARIFF_THRESHOLD
from load_balancer import split_load, SOURCES


def run_day(spike=False, threshold=TARIFF_THRESHOLD):
    soc = 100
    cost_without = 0
    cost_with = 0
    rows = []

    for hour in range(24):
        tariff = get_tariff(hour, spike)
        source = decide_source(tariff, soc, threshold)

        cost_without = cost_without + LOAD_KW * tariff

        if source == "internal":
            shares = split_load(LOAD_KW, SOURCES)
            hour_cost = 0
            for name, kw in shares.items():
                hour_cost = hour_cost + kw * SOURCES[name]["cost_per_kwh"]
            soc = update_battery(soc, "battery", draw_kw=shares["battery"])
        else:
            hour_cost = LOAD_KW * tariff
            soc = update_battery(soc, "grid")

        cost_with = cost_with + hour_cost
        rows.append({"hour": hour, "tariff": tariff, "source": source, "soc": round(soc, 1)})
        print(hour, tariff, source, round(soc, 1))

    print("Cost without system:", round(cost_without, 2))
    print("Cost with system:", round(cost_with, 2))
    print("Money saved:", round(cost_without - cost_with, 2))

    return rows, cost_without, cost_with


if __name__ == "__main__":
    run_day()