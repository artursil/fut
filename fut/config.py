# chrome 53 @ win10
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    # 'Accept-Charset': 'utf-8, iso-8859-1, utf-16, *;q=0.1',
    'Connection': 'keep-alive',
    # 'Keep-Alive': '300',
    'DNT': '1',
}

# android 4.2 @ nexus
headers_and = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.2; en-us; Nexus 10 Build/JVP15I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'en-US',
    'Accept-Charset': 'utf-8, iso-8859-1, utf-16, *;q=0.7',
    'Connection': 'keep-alive',
    # 'Keep-Alive': '300',
    # 'DNT': '1',
    'X-Requested-With': 'com.ea.fifaultimate_row',  # ultimate app identifier?
}

# safari 7 (ios phone)
headers_ios = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'en-US',
    'Accept-Charset': 'utf-8, iso-8859-1, utf-16, *;q=0.7',
    'Connection': 'keep-alive',
    # 'Keep-Alive': '300',
    # 'DNT': '1',
    # 'X-Requested-With': 'com.ea.fifaultimate_row',  # ultimate app identifier?
}

flash_agent = 'ShockwaveFlash/24.0.0.186'

cookies_file = 'cookies.txt'
timeout = 15  # defaulf global timeout
delay = (0, 5)  # default mininum delay between requests (random range)
