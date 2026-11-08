# EcoStruxure Edge Load Balancer

A simulation of an edge logic engine that moves a commercial building's power draw from the grid to internal sources (battery, solar, generator) when electricity prices spike.

## How it works

1. The tariff simulator gives a price ($/kWh) for each hour of the day.
2. The decision engine chooses grid or internal power: internal when the price is above the threshold and the battery is above 30%.
3. The load balancer splits the building's load across battery, solar and generator in proportion to the energy each has available.
4. The operator page shows the source, battery level, money saved and percent saved.

## Assumptions (all simulated)

- Tariff: 0.08 overnight, 0.15 daytime, 0.30 from 5 PM to 9 PM.
- Building load: constant 50 kW.
- Battery: 400 kWh, recharged from the grid at 25 kW.
- Internal sources: battery 200 kWh at 0.05 $/kWh, solar 100 kWh at 0.00, generator 100 kWh at 0.12.
- Price data is simulated. The "Price spike" checkbox is a demo control only. In a real deployment the price would come from a live utility feed.

## Results (one simulated day)

- Cost without system: $175.00
- Cost with system: $132.00
- Saved: $43.00 (24.6%), against a target of 15 to 20%
- Lowest battery level: 75%, above the 30% floor
- Decision latency: far under the 500 ms target (see decision_log.csv)

## Run it

```
pip3 install flask
python3 src/app.py
```

Then open http://127.0.0.1:5001.

Run the engine tests with `python3 src/test_engine.py`.