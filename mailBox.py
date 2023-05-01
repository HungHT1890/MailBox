from requests import session



class Temp_Mail():# temp-mail.io/en
    ss = session()
    def new_mail(self):
        api = f'https://api.internal.temp-mail.io/api/v3/email/new'
        mail_length_min = 10
        mail_length_max = 20
        data = {"min_name_length":mail_length_min,"max_name_length":mail_length_max}
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        header = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'application-name': 'web',
            'application-version': '2.2.29',
            'content-length': '43',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://temp-mail.io',
            'referer': 'https://temp-mail.io/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua
            }
        try:
            mail = self.ss.post(url=api , headers= header , json= data).json()['email']
            return mail
        except Exception as error_msg:
            error_msg = str(error_msg)
            print(f"ERROR: {error_msg} | GET NEW MAIL AGAIN !")
            return Temp_Mail().new_mail(self)
        
    def read_mail(self,mail):
        api = f'https://api.internal.temp-mail.io/api/v3/email/{mail}/messages'
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        header = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'application-name': 'web',
            'application-version': '2.2.29',
            'origin': 'https://temp-mail.io',
            'referer': 'https://temp-mail.io/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua
            }
        try:
            return self.ss.get(url= api , headers= header).text
        except Exception as error_msg:
            error_msg = str(error_msg)
            return Temp_Mail().read_mail(self,mail)
        