import sys
import json
import cgi
import cgitb
import stripe


cgitb.enable()
 
print 'Content-Type: Application/json'

stripe.api_key = 'pk_test_mjZsJALdxDNEccGVqWPBzX73'
 
#4
json_data = sys.stdin.read()
json_dict = json.loads(json_data)
 

stripeAmount = json_dict['stripeAmount']
stripeCurrency = json_dict['stripeCurrency']
stripeToken = json_dict['stripeToken']
stripeDescription = json_dict['stripeDescription']
 
#6
json_response = stripe.Charge.create(amount=stripeAmount, currency=stripeCurrency, card=stripeToken, description=stripeDescription)
 
print json_response

