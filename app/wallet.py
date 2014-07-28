from flask import Flask, render_template, redirect , session , url_for , escape , request, Markup
from flask_bootstrap import Bootstrap 
from flask_wtf import Form, RecaptchaField
from wtforms import TextField,   ValidationError,  SubmitField,  FormField, validators
from wtforms.validators import Required 
from iBitcoin import BTcoin 
import datetime
 
# Create the payment form to send coins 
class PaymentForm(Form):
    sentTo = TextField('Send to', 	description='Send to.', 	validators=[Required()])
    amount = TextField('Bitcoins', 	description='Bitcoins.',  	validators=[Required()]) 
    submit_button = SubmitField('Submit Form')  
		
# instance flask
app = Flask(__name__)
app.debug = True 
Bootstrap(app) 
app.config['SECRET_KEY'] = 'devkey' 
config = {
    "bt_account_id": "",
    "username": "whatever",
    "password": "whatever", 
    "hostname": "127.0.0.1", 
    "port": "7244" 
} 

# RPC Bitcoin object , use this as an wrapper of bitcoin class
# if there is changes in the bitcoin rpc JUST update the BTcoin class not this code.
BTwrapper	= BTcoin( config['bt_account_id'] , config['username'] , config['password'] , config['hostname'] ,config['port']    );
def getBitcoinAddress():
	return BTwrapper.getAddress() 
def getBitcoinBalance(): 
	return BTwrapper.getBalance()  
def getBitcoinNewAddress(): 
	return BTwrapper.getNewAddress()  
def doBitcoinPayment(toBTaddress,coins):
	return BTwrapper.doPayment(toBTaddress,coins)
def getListTransactions(): 
	return BTwrapper.getListTransactions()  
	
# Lets route the app to landpage tpl.
@app.route('/', methods = ['GET', 'POST'])
def landpage():  
	LastMsg = ''
	# get bitcoin address from session.
	if 'BitcoinAddress' in session:
		BTaddress = escape(session['BitcoinAddress']) 
	else: 
		# else lets create a new one.
		return redirect(url_for('refresh'))
		
	# last_msg contains last msg error or success of any action,once is used its deleted
	if 'last_msg' in session:
		LastMsg = escape(session['last_msg']) 
		session['last_msg'] =  ''
	
	BTbalance 	= getBitcoinBalance()
	BTtransactions= getListTransactions()  
	form 		= PaymentForm()
	return render_template('landpage.html' , BTbalance = BTbalance, BTaddress=BTaddress , form=form , LastMsg=Markup(LastMsg).unescape() , transactions=BTtransactions );
 
# refresh bitcoin address
@app.route('/refresh', methods = ['GET', 'POST'])
def refresh(): 
	session['BitcoinAddress'] =  getBitcoinNewAddress() 
	return redirect('/paybit') #url_for will take the route url param, but for this demo we are using /paybit alias apache hardcoded

# do bitcoin payment 
@app.route('/payment', methods = ['POST'])
def payment(): 
	if request.method == 'POST':
		sentTo = request.form['sentTo']
		amount = request.form['amount']
		result = doBitcoinPayment(sentTo,amount)
		session['last_msg'] =  result 
		return redirect('/paybit')
			
if __name__ == '__main__':
    app.run(host='0.0.0.0')
 