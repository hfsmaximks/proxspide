 import requests
def get_proxy_list(proxy_type):
    if proxy_type == 'http':
        url = "https://www.proxy-list.download/api/v1/get?type=http"
    elif proxy_type == 'https':
        url = "https://www.proxy-list.download/api/v1/get?type=https"
    elif proxy_type == 'socks4':
        url = "https://www.proxy-list.download/api/v1/get?type=socks4"
    elif proxy_type == 'socks5':
        url = "https://www.proxy-list.download/api/v1/get?type=socks5"
    else:
        return "Invalid proxy type"
    response = requests.get(url)
    print(response.text)
get_proxy_list('http')
get_proxy_list('https')
get_proxy_list('socks4')
get_proxy_list('socks5')
