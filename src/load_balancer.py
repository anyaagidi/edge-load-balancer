SOURCES = {
    "battery": {"available_kwh": 200, "cost_per_kwh": 0.05},
    "solar": {"available_kwh": 100, "cost_per_kwh": 0.00},
    "generator": {"available_kwh": 100, "cost_per_kwh": 0.12},
}


def split_load(load_kw, sources):
    """Split the building's power use across sources by how much energy each has."""
    total = sum(s["available_kwh"] for s in sources.values())
    if total == 0:
        return {}

    shares = {}
    for name, s in sources.items():
        shares[name] = load_kw * s["available_kwh"] / total

    return shares


if __name__ == "__main__":
    shares = split_load(50, SOURCES)
    for name, kw in shares.items():
        print(name, kw)