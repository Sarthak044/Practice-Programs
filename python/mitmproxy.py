import mitmproxy 

def request(flow):
    print('[+] This is the Request Flow')
    print(flow.request)

