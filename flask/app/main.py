from flask import Flask 
from flask import render_template, redirect, url_for
from flask import request
from block import check_integrity, write_block


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        lender = request.form.get('lender')
        amount = request.form.get('amount')
        borrower = request.form.get('borrower')
        
        write_block(lender, amount, borrower)
        
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/checking', methods=['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', res=results)


if __name__ == '__main__':
    app.run(debug=True)