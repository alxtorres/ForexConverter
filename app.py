from flask import Flask, render_template, request, redirect, url_for, flash
from utils import is_valid_currency, convert_currency, format_currency

app = Flask(__name__)
app.secret_key = 'a1b2c3'  # Replace 'your_secret_key' with a real secret key

@app.route('/', methods=['GET'])
def index():
    # Renders the initial form for currency conversion
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Extracts data from form submission
    from_currency = request.form['from_currency'].upper()
    to_currency = request.form['to_currency'].upper()
    amount = request.form['amount']

    try:
        # Validate currency codes and amount
        if not is_valid_currency(from_currency) or not is_valid_currency(to_currency):
            raise ValueError("Invalid currency code.")

        if not amount.replace('.', '', 1).isdigit():
            raise ValueError("Invalid amount")

        # Convert the amount
        amount = float(amount)
        converted_amount = convert_currency(from_currency, to_currency, amount)
        result = format_currency(converted_amount, to_currency)

        # Render result
        return render_template('result.html', result=result)
    except ValueError as e:
        flash(str(e))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
