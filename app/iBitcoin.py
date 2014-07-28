from bitcoinrpc.authproxy import AuthServiceProxy,  JSONRPCException
 
class BTcoin:  

	def __init__(self, bt_account_id , username, password, hostname, port ):
		self.bt_account_id = bt_account_id  
		self.coin_client = AuthServiceProxy("http://%s:%s@%s:%s" % (username, password, hostname, port)) 
		if not self.check_client_connection():
			print "Error: Failed to connect or authenticate with the  client. Please check it's running and configured correctly."  
			
	#  Verify client		
	def check_client_connection(self):
		try:
			test = self.coin_client.getinfo()
			return True
		except socket.error:
			return False
		except ValueError:
			return False
			
	# bitcoin listaccounts
	def getAccount(self):
		return self.bt_account_id
	
	# bitcoin getaccountaddress <bt_account_id>
	def getAddress(self):
		return self.coin_client.getaccountaddress( self.bt_account_id )	 

	# bitcoin getbalance
	def getBalance(self):  
		return self.coin_client.getbalance()	
		
	# bitcoin getnewaddress
	def getNewAddress( self):
		return self.coin_client.getnewaddress( self.bt_account_id  )
		
	# bitcoin listtransactions ""
	def getListTransactions( self):
		return self.coin_client.listtransactions( self.bt_account_id  )

	# bitcoin sendtoaddress <targetaddress> <amount> [comment] [comment-to]
	def doPayment(self,toBTaddress,coins): 
		if not toBTaddress:
			return  '<div class="alert alert-danger" style="   margin: 15px;" role="alert">Error - no payment address set</div>' 
		else: 
			try:
				transaction 	= self.coin_client.sendtoaddress( toBTaddress , float(coins)  ) 
				transaction_url = "http://lbw.blockprobe.com/index.php/search?q=%s" % transaction	 
				html 			= '<div class="alert alert-info" style="    margin: 15px;" role="alert"><b>Your transaction is complete:</b> <a href="http://lbw.blockprobe.com/index.php/search?q=%s" target="_blank">%s</a></div>' % (transaction,transaction	)
				return html
			except JSONRPCException as e:
				return '<div class="alert alert-danger" style="   margin: 15px;" role="alert">Error - %s</div>' % e.error['message']

			