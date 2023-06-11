from proxy import *
import asyncio
import random
logo = """
███████╗██████╗ ███████╗███████╗███████╗███╗   ███╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝████╗ ████║██╔════╝
█████╗  ██████╔╝█████╗  █████╗  ███████╗██╔████╔██║███████╗
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██║╚██╔╝██║╚════██║
██║     ██║  ██║███████╗███████╗███████║██║ ╚═╝ ██║███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝
by csoftware                                                       
"""
print(logo)
print("Getting a list of proxies")
proxy_list = asyncio.run(get_proxy_list())
number = input("Number ~> ")
message = input("Message ~> ")
proxy_random = random.randint(0, len(proxy_list))
proxy_list = {"http": f'http://{proxy_list[proxy_random][0]}:{proxy_list[proxy_random][1]}', "https": f'http://{proxy_list[proxy_random][0]}:{proxy_list[proxy_random][1]}'}
try:
	print("Sending...")
	resp = requests.post('http://textbelt.com/text', {
	  'phone': number,
	  'message': message,
	  'key': 'textbelt',
	}, proxies=proxy_list)
	status = resp.json()
	if status["success"] == False:
		print(f"Error: {status['error']}")
	else:
		print("Success")
except:
	print("Error")
