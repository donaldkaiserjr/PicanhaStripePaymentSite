# Great CSS styling info here:  https://www.developerdrive.com/how-to-create-a-css-grid-step-by-step/#:~:text=To%20make%20an%20element%20into,to%20an%20inline%2Dlevel%20grid.&text=In%20the%20CSS%2C%20we%20use,a%20block%2Dlevel%20CSS%20Grid.

from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

public_key = 'pk_test_6pRNASCoBOKtIshFeQd4XMUh'

stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

@app.route('/')
def index():
    return render_template('index.html', public_key=public_key)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')
    

@app.route('/payment', methods=['POST'])
def payment():

    # CUSTOMER INFORMATION
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                      source=request.form['stripeToken'])

    # CHARGE/PAYMENT INFORMATION
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=1999,
        currency='usd',
        description='Donation'
    )

    return redirect(url_for('thankyou'))

if __name__ == '__main__':
    app.run(debug=True)
