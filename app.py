from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    cost = 0
    message = ""

    if request.method == 'POST':
        instance = request.form['instance']
        hours = int(request.form['hours'])

        # Cost calculation
        if instance == "t2.micro":
            rate = 0.0116
        else:
            rate = 0.0464

        cost = rate * hours

        # Alerts
        if hours > 100:
            message += "High Usage Alert! "
        if cost > 500:
            message += "Billing Alert!"

    return render_template('index.html', cost=cost, message=message)

app.run(debug=True)