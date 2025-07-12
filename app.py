from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

expenses = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        category = request.form['category']
        amount = float(request.form['amount'])
        expenses.append({'description': description, 'category': category, 'amount': amount})
        return redirect(url_for('index'))

    total = sum(exp['amount'] for exp in expenses)

    # Calculate total per category
    category_data = {}
    for exp in expenses:
        if exp['category'] in category_data:
            category_data[exp['category']] += exp['amount']
        else:
            category_data[exp['category']] = exp['amount']

    return render_template('index.html', expenses=expenses, total=total, category_data=category_data)

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
