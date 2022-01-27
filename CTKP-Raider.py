    import requests, os, time, ctypes, websocket, json, random, discum
    from concurrent.futures import ThreadPoolExecutor
    import colorama
    from colorama import Fore, Style
    import string, base64
    req = requests.Session()
    tokens = open('tokens.txt', 'r').read().splitlines()
    colorama.init(autoreset=True)
    with open('config.json', encoding='utf-8', errors='ignore') as (f):
        configdata = json.load(f, strict=False)
    config = configdata['BotConfig']
    tokens = open('tokens.txt', 'r').read().splitlines()
    proxies = open('proxies.txt', 'r').read().splitlines()
    proxies = [{'https': 'http://' + proxy} for proxy in proxies]
     
    def _count_generator(reader):
        b = reader(1048576)
        while b:
            yield b
            b = reader(1048576)
     
     
    with open('tokens.txt', 'rb') as (fp):
        c_generator = _count_generator(fp.raw.read)
        count = sum((buffer.count(b'\n') for buffer in c_generator))
    with open('proxies.txt', 'rb') as (bp):
        c_generator = _count_generator(bp.raw.read)
        lolz = sum((buffer.count(b'\n') for buffer in c_generator))
     
    class VERSION:
        __version__ = 1.2
     
     
    def random_string():
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 5))]
        return ''.join(randlst)
     
     
    def Setup():
        ctypes.windll.kernel32.SetConsoleTitleW(f"CTKP-Raider v{VERSION.__version__} | By 冥王サウロン")
        os.system('cls')
        print(Fore.GREEN + '\n\n     >>' + Fore.RESET + ' CTKP-Raiderへようこそ ' + Fore.GREEN + f"v{VERSION.__version__}", Fore.RESET)
        print(Fore.GREEN + f"     >> {Fore.GREEN}{count + 1}" + Fore.RESET + ' 個のTokenが読み込まれています')
        print(Fore.GREEN + f"     >> {Fore.GREEN}{lolz + 1}" + Fore.RESET + ' 個のProxyが読み込まれています')
        print(Fore.GREEN + '     >>' + Fore.RESET + ' Discord Link ' + Fore.GREEN + '>>' + Fore.CYAN + ' https://discord.gg/hzhajDR2CP', Fore.RESET)
        print(Fore.GREEN + '\n\n     1 >>' + Fore.RESET + ' 入室 (招待コード)' + Fore.RESET)
        print(Fore.GREEN + '     2 >>' + Fore.RESET + ' 退室 (サーバーID)' + Fore.RESET)
        print(Fore.GREEN + '     3 >>' + Fore.RESET + ' スパム (チャンネルID) (送信数) (メッセージ)' + Fore.RESET)
        print(Fore.GREEN + '     4 >>' + Fore.RESET + ' Webhook (WebhookURL) (送信数) (メッセージ)' + Fore.RESET)
        print(Fore.GREEN + '     5 >>' + Fore.RESET + ' メンション爆撃 (チャンネルID) (メッセージ)' + Fore.RESET)
        print(Fore.GREEN + '     6 >>' + Fore.RESET + ' ニックネーム変更 (サーバーID) (ニックネーム)' + Fore.RESET)
        print(Fore.GREEN + '     7 >>' + Fore.RESET + ' アバター変更 (画像URL)' + Fore.RESET)
        print(Fore.GREEN + '     8 >>' + Fore.RESET + ' プロフィール変更 (文章)' + Fore.RESET)
        print(Fore.GREEN + '     9 >>' + Fore.RESET + ' プロキシを探す (HTTP)' + Fore.RESET)
        print(Fore.GREEN + '     10 >>' + Fore.RESET + ' ツールについて' + Fore.RESET)
        print(Fore.GREEN + '     11 >>' + Fore.RESET + ' コンソールをリセット' + Fore.RESET)
     
     
    def toB64(file):
        with open("./images/"+file, "rb") as img_file:
            return base64.b64encode(img_file.read())
     
     
    def Join(invite):
        try:
            print(f"{Fore.GREEN}     >>{Fore.RESET} 入室中...{Fore.RESET}")
            inv = invite.replace('https://discord.gg/', '')
            if config['useproxy'] == True:
                for tok in tokens:
                    bot = discum.Client(token=tok)
                    proxy = random.choice(proxies)
                    r = req.post(f"https://discord.com/api/v9/invites/{inv}", headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}, proxies=proxy)
                    print(r)
     
            else:
                for tok in tokens:
                    r = req.post(f"https://discord.com/api/v9/invites/{inv}", headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'})
                    print(r)
     
            print(f"{Fore.GREEN}     >>{Fore.RESET} すべてのアカウントがサーバーに参加しました")
        except Exception as e:
            try:
                print(f"{Fore.RED}     [ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e
     
        else:
            Start()
     
     
    def Leave(serverid):
        try:
            print(f"{Fore.GREEN}     >>{Fore.RESET} 退室中...{Fore.RESET}")
            if config['useproxy'] == True:
                for tok in tokens:
                    proxy = random.choice(proxies)
                    r = req.delete(f"https://discord.com/api/v9/users/@me/guilds/{serverid}", headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}, proxies=proxy)
     
            else:
                for tok in tokens:
                    r = req.delete(f"https://discord.com/api/v9/users/@me/guilds/{serverid}", headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'})
     
            print(r)
            print(f"{Fore.GREEN}     >>{Fore.RESET} すべてのアカウントがサーバーから退室しました")
        except Exception as e:
            try:
                print(f"{Fore.YELLOW}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e
     
        else:
            Start()
     
     
    def Spam(channel, amount, message):
        try:
            print(f"{Fore.GREEN}     >>{Fore.RESET} 送信中...{Fore.RESET}")
            if config['useproxy'] == True:
                for _ in range(int(amount)):
                    for tok in tokens:
                        proxy = random.choice(proxies)
                        time.sleep(random.uniform(0.5, 1.3))
                        r = req.post(f"https://discordapp.com/api/v9/channels/{channel}/messages", headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}, json={'content':f"{message} {random_string()}",  'nonce':'',  'tts':False}, proxies=proxy)
     
            else:
                for _ in range(int(amount)):
                    for tok in tokens:
                        time.sleep(random.uniform(0.5, 1.3))
                        r = req.post(f"https://discordapp.com/api/v9/channels/{channel}/messages", headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}, json={'content':f"{message} {random_string()}",  'nonce':'',  'tts':False})
                        print(r)
                        if r.status_code != 200:
                            print(f"{Fore.GREEN}     >>{Fore.RESET} 完了!")
                            if r.status_code == 429:
                                print(f"レート制限を検知しました\n{r.headers['retry-after']}秒間スパムを停止します\n")
                                time.sleep(int(r.headers['retry-after']))
     
        except Exception as e:
            try:
                print(f"{Fore.YELLOW}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e
     
        else:
            Start()
     
     
    def Webhook(link, amount, message):
        try:
            for _ in range(int(amount)):
                time.sleep(0.1)
                _data = requests.post(link, json={'content': message})
     
            if _data.status_code == 204:
                print(f"{Fore.GREEN}[+] {Fore.RESET}{message} 送信完了")
                if r.status_code == 429:
                    print(f"レート制限を検知しました\n{_data.headers['retry-after']}秒間スパムを停止します\n")
                    time.sleep(int(_data.headers['retry-after']))
        except Exception as e:
            try:
                print(f"{Fore.YELLOW}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e
     
        else:
            Start()
     
     
    def Status(text):
        try:
            print(f"{Fore.GREEN}     >>{Fore.RESET} 送信中...{Fore.RESET}")
            if config['useproxy'] == True:
                for tok in tokens:
                    proxy = random.choice(proxies)
                    time.sleep(random.uniform(0.5, 2))
                    r = req.patch('https://discordapp.com/api/v9/users/@me', headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}, json={'bio': text}, proxies=proxy)
     
            else:
                for tok in tokens:
                    time.sleep(random.uniform(0.5, 2))
                    r = req.patch('https://discordapp.com/api/v9/users/@me', headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}, json={'bio': text})
                else:
                    print(r)
     
            if r.status_code != 200:
                print(f"{Fore.GREEN}     >>{Fore.RESET} 完了!")
        except Exception as e:
            try:
                print(f"{Fore.YELLOW}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e
     
        else:
            Start()
     
     
    def React():
        print(f"{Fore.RED}     [X]{Fore.RESET} 準備中...")
        Start()
     
     
    def Nick(server, nickname):
        try:
            print(f"{Fore.GREEN}     >>{Fore.RESET} 送信中...{Fore.RESET}")
            if config['useproxy'] == True:
                for tok in tokens:
                    proxy = random.choice(proxies)
                    r = req.patch(f"https://discordapp.com/api/v9/guilds/{server}/members/@me/nick", headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}, json={'nick': nickname}, proxies=proxy)
     
            else:
                for tok in tokens:
                    time.sleep(random.uniform(0.5, 2))
                    r = req.patch(f"https://discordapp.com/api/v9/guilds/{server}/members/@me/nick", headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}, json={'nick': nickname})
     
            print(r)
            if r.status_code != 200:
                print(f"{Fore.GREEN}     >>{Fore.RESET} 完了!")
        except Exception as e:
            try:
                print(f"{Fore.YELLOW}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e
     
        else:
            Start()
     
     
    def Avatar(image):
        try:
            image = toB64(image).decode('utf-8')
            print(f"{Fore.GREEN}     >>{Fore.RESET} 送信中...{Fore.RESET}")
            if config['useproxy'] == True:
                for tok in tokens:
                    proxy = random.choice(proxies)
                    r = req.patch('https://discordapp.com/api/v9/users/@me', headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}, json={'avatar': f"data:image/png;base64,{image}"}, proxies=proxy)
     
            else:
                for tok in tokens:
                    time.sleep(random.uniform(0.5, 2))
                    r = req.patch('https://discordapp.com/api/v9/users/@me', headers={'Authorization':tok,  'accept':'*/*',  'accept-language':'en-US',  'connection':'keep-alive',  'cookie':f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",  'DNT':'1',  'origin':'https://discord.com',  'sec-fetch-dest':'empty',  'sec-fetch-mode':'cors',  'sec-fetch-site':'same-origin',  'referer':'https://discord.com/channels/@me',  'TE':'Trailers',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',  'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}, json={'avatar': f"data:image/png;base64,{image}"})
     
            print(r)
            if r.status_code != 200:
                print(f"{Fore.GREEN}     >>{Fore.RESET} 完了!")
        except Exception as e:
            try:
                print(f"{Fore.YELLOW}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e
     
        else:
            Start()
     
     
    def Info():
        print(f"\n\n     {Fore.GREEN}>> {Fore.RESET}このツールはSkrunkly-Raiderを元に作られています\n     {Fore.GREEN}>> {Fore.RESET}コマンドは {Fore.RED}スペースで区切ります。{Fore.RESET}\n{Fore.YELLOW}     [!] {Fore.RESET}このツールを転載して儲けた場合 {Fore.RED}どんな場合でも{Fore.RESET} 返金を要求します")
        Start()
     
     
    def Reset():
        os.system('cls')
        Setup()
        Start()
     
     
    def Scrape():
        print(f"{Fore.GREEN}     >> {Fore.RESET}プロキシを探しています...")
        try:
            r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
            file = open('proxies.txt', 'a+')
            file.seek(0)
            file.truncate()
            proxies = []
            for proxy in r.text.split('\n'):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                for p in proxies:
                    file.write(p + '\n')
                else:
                    file.close()
                    print(f"{Fore.GREEN}     >>{Fore.RESET} 完了!")
     
        except Exception as e:
            try:
                print(f"{Fore.RED}     [ERROR]: {Fore.RESET}{e}")
            finally:
                e = None
                del e
     
        else:
            Start()
     
     
    def Start():
        command = list(input(Fore.GREEN + '\n\n     >> ' + Fore.RESET).split(' '))
        if command[0] == '1':
            invite = command[1]
            Join(invite)
        else:
            if command[0] == '2':
                serverid = command[1]
                Leave(serverid)
            else:
                if command[0] == '3':
                    channel = command[1]
                    amount = command[2]
                    message = command[3]
                    Spam(channel, amount, message)
                else:
                    if command[0] == '4':
                        link = command[1]
                        amount = command[2]
                        message = command[3]
                        Webhook(link, amount, message)
                    else:
                        if command[0] == '5':
                            React()
                        else:
                            if command[0] == '6':
                                server = command[1]
                                nickname = command[2]
                                Nick(server, nickname)
                            else:
                                if command[0] == '7':
                                    file = command[1]
                                    Avatar(file)
                                else:
                                    if command[0] == '8':
                                        text = command[1]
                                        Status(text)
                                    else:
                                        if command[0] == '9':
                                            Scrape()
                                        else:
                                            if command[0] == '10':
                                                Info()
                                            else:
                                                if command[0] == '11':
                                                    Reset()
                                                else:
                                                    print(f"{Fore.RED}     [ERROR]{Fore.RESET} Invalid Command!")
                                                    Start()
     
     
    if __name__ == '__main__':
        try:
            Setup()
            Start()
        except Exception as e:
            try:
                print(f"{Fore.RED}     [ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
                Start()
            finally:
                e = None
                del e