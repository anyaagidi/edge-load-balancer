from flask import Flask, render_template_string, request
from main import run_day

app = Flask(__name__)

PAGE = """
<h1>EcoStruxure Edge Load Balancer</h1>
<form method="get">
  Price threshold ($/kWh): <input name="threshold" value="{{ threshold }}">
    <label><input type="checkbox" name="spike" value="1" {% if spike %}checked{% endif %}> Price spike</label>
  <button type="submit">Update</button>
</form>
<p>Cost without system: ${{ cost_without }}</p>
<p>Cost with system: ${{ cost_with }}</p>
<p>Money saved: ${{ saved }}</p>
<p>Percent saved: {{ percent }}%</p>
<table border="1" cellpadding="6">
  <tr><th>Hour</th><th>Price ($/kWh)</th><th>Source</th><th>Battery (%)</th></tr>
  {% for r in rows %}
  <tr><td>{{ r.hour }}</td><td>{{ r.tariff }}</td><td>{{ r.source }}</td><td>{{ r.soc }}</td></tr>
  {% endfor %}
</table>
"""


@app.route("/")
def home():
    threshold = float(request.args.get("threshold", 0.20))
    spike = request.args.get("spike") == "1"
    rows, cost_without, cost_with = run_day(spike=spike, threshold=threshold)
    return render_template_string(
        PAGE,
        rows=rows,
        threshold=threshold,
        spike=spike,
        cost_without=round(cost_without, 2),
        cost_with=round(cost_with, 2),
        saved=round(cost_without - cost_with, 2),
        percent=round((cost_without - cost_with) / cost_without * 100, 1),
    )


if __name__ == "__main__":
    app.run(port=5001)