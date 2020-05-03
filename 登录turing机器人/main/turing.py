'''
文件说明 : turing机器人
编写作者 : Chenyg
编写时间 : 2020年4月6日
'''

import json
import  urllib.request

def turing():
    api_url = 'http://openapi.tuling123.com/openapi/api/v2'

    while 1:
        try:
            text_input = input('我: ')
            req = {
                "perception":
                {
                    "inputText":
                    {
                        "text": text_input
                    },

                    "selfInfo":
                    {
                        "location":
                        {
                            "city": "武汉",
                            "province": "湖北",
                            "street": "江汉路"
                        }
                    }
                },

                "userInfo":
                {
                    "apiKey": "38c1ffd1a04247288680e3017560ce53",
                    "userId": "OnlyUseAlphabet"
                }
            }
            req = json.dumps(req).encode('utf-8')
            http_post = urllib.request.Request(api_url,data=req)
            response = urllib.request.urlopen(http_post)
            response_str = response.read().decode('utf-8')
            response_dic = json.loads(response_str)
            intent_code = response_dic['intent']['code']
            result_text = response_dic['results'][0]['values']['text']
            print('Turing的回答:',result_text)
        except Exception as e:
            print ('您已关闭机器人')

