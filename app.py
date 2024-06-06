from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "NPV": 10000,
        "IRR": 12,
        "MIRR": 10,
        "Payback Period": 5,
        "Scenario Analysis": "Details...",
        "Sensitivity Analysis": "Details...",
        "Monte Carlo Simulation": "Details...",
        "Decision Tree Analysis": "Details...",
        "Dynamic Reporting": "Details..."
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
