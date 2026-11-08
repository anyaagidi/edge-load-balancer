from flask import Flask, render_template_string
from main import run_day

app = Flask(__name__)

PAGE = """
<h1>EcoStruxure Edge Load Balancer</h1>
<p>Cost without system: ${{ cost_without }}</p>
<p>Cost with system: ${{ cost_with }}</p>
<p>Money saved: ${{ saved }}</p>
<table border="1" cellpadding="6">
  <tr><th>Hour</th><th>Price ($/kWh)</th><th>Source</th><th>Battery (%)</th></tr>
  {% for r in rows %}
  <tr><td>{{ r.hour }}</td><td>{{ r.tariff }}</td><td>{{ r.source }}</td><td>{{ r.soc }}</td></tr>
  {% endfor %}
</table>
"""


@app.route("/")
def home():
    rows, cost_without, cost_with = run_day()
    return render_template_string(
        PAGE,
        rows=rows,
        cost_without=round(cost_without, 2),
        cost_with=round(cost_with, 2),
        saved=round(cost_without - cost_with, 2),
    )


if __name__ == "__main__":
    app.run(port=5001)