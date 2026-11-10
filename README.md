# EcoStruxure Edge Load Balancer

## Summary

- **Problem:** Commercial buildings pay heavy demand charges when they draw grid power during peak price hours, and shifting load by hand is too slow.
- **For whom:** Commercial facility operations managers with on-site storage.
- **What was built:** A simulated edge engine that reads the price and battery level every cycle, chooses grid or internal power, and splits the load across battery, solar and generator when it goes internal. An operator page shows the source, battery level, money saved and percent saved.
- **Result:** In one simulated day the system saved 24.6% ($43.00 of $175.00) against a 15 to 20% target. The battery never went below 75% against a 30% floor, and each decision took far less than the 500 ms target.
- **Caveat:** The result comes from simulated prices and source sizes, so it shows the logic works, not what a real site would save.

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

## Decisions and tradeoffs

- **Cut hardware and SCADA wiring:** the core value is the switching logic, and hardware would not fit a 48-hour build.
- **Cut AI price forecasting:** a fixed threshold rule is simple to explain and test, but it reacts to prices instead of anticipating them.
- **Cut multi-facility management:** one building is enough to prove the idea.
- **Kept the 15 to 20% target and reported the actual 24.6%:** changing a target after seeing the result would make it meaningless.
- **Split the load by available energy:** it is simple and every source contributes, but the split ignores cost, so it is not the cheapest possible mix.
- **Simulated price data and a demo-only spike checkbox:** in a real deployment only the price function would be replaced and no manual step would remain.

## Next steps

1. Replace the simulated tariff function with a live utility or smart meter feed.
2. Choose how much each source carries by cost as well as available energy.
3. Validate the assumptions and savings estimate with a real facility manager.
4. Add price forecasting so the battery is ready before a spike.
5. Connect to real meters and controllers.
6. Manage several buildings from one place.

## Run it

```
pip3 install flask
python3 src/app.py
```

Then open http://127.0.0.1:5001.

Run the engine tests with `python3 src/test_engine.py`.