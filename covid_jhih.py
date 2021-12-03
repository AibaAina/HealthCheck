import requests
import warnings
import random
import time
import sys

from bs4 import BeautifulSoup
from datetime import date, datetime

def post_survey ():
    """
    """
    survey_url = 'https://zh.surveymonkey.com/r/EmployeeHealthCheck'

    headers = {
        'authority' : 'zh.surveymonkey.com',
        'method' : 'GET',
        'path' : '/r/EmployeeHealthCheck',
        'schema' : 'https',
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding' : 'gzip, deflate, br',
        'accept-language' : 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-CN;q=0.5,la;q=0.4',
        'cookie' : 'attr_multitouch="C1y54DA0yYRZtu/ZS51q9++H4P0="; ep201="c2UOL6eBqn4OZqD1B+OtQi92BA0="; ep202="TN1ZSaDVj8jMCu9LNm9BlVUi23s="; ep203="yoQftnhGeBqj8TsFNk1pMqrcQIE="; cdp_seg="4ZxY0z4xmnzMqDXoXz8gAZzdkpw="; _ga=GA1.1.1280988135.1633523071; _gid=GA1.2.537719147.1633523071',
        'sec-ch-ua' : '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile' : '?0',
        'sec-fetch-dest' : 'document',
        'sec-fetch-mode' : 'navigate',
        'sec-fetch-site' : 'same-origin',
        'sec-fetch-user' : '?1',
        'upgrade-insecure-requests' : '1',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    # datetime
    dt = int(datetime.now().timestamp()*1000)
    dt_end = dt + 1290252

    r = requests.session()
    r.keep_alive = False
    r.trust_env = False # ignore global proxy setting

    # get url
    rep = r.get(survey_url, headers=headers, verify=False)

    # get input value
    soup = BeautifulSoup(rep.text, 'lxml')
    input_key = soup.find('input', {'id':'survey_data'}).get('value')
    print(r)

    # get cookie
    cookies = rep.headers['set-cookie'].split('Secure, ')
    parameter = ['attr_multitouch', 'ep201', 'ep202', 'ep203', 'cdp_seg']
    parm = {}
    for p in parameter:
        for c in cookies:
            if p in c:
                parm.setdefault(p, c.split(';')[0])
    print(parm)

    # remark content-type
    headers = {
        'authority' : 'zh.surveymonkey.com',
        'method' : 'POST',
        'path' : '/r/EmployeeHealthCheck',
        'schema' : 'https',
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding' : 'gzip, deflate, br',
        'accept-language' : 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-CN;q=0.5,la;q=0.4',
        'cache-control' : 'max-age=0',
        'content-length' : '5974',
        'cookie' : f'{parm["attr_multitouch"]}; {parm["ep201"]}; {parm["ep202"]}; {parm["ep203"]}; {parm["cdp_seg"]}; _ga=GA1.2.1264406460.1628572314; _gid=GA1.2.2017799933.1628572314',
        'origin' : 'https://zh.surveymonkey.com',
        'referer' : 'https://zh.surveymonkey.com/r/EmployeeHealthCheck',
        'sec-ch-ua' : '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile' : '?0',
        'sec-ch-ua-platform' : 'Windows',
        'sec-fetch-dest' : 'document',
        'sec-fetch-mode' : 'navigate',
        'sec-fetch-site' : 'same-origin',
        'sec-fetch-user' : '?1',
        'upgrade-insecure-requests' : '1',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    payload = {
        '715032623': '4702730653',
        '715032620': '116870',
        '715032625': '4702730655',
        '715032621': f"{random.uniform(36, 36.5):0.1f}",
        '715032636[]': '4702730736',
        '715032636_other': '',
        '715032630': '4702730680',
        '715032637': '4702730769',
        '715032622': '4702730645',
        'survey_data': f"{input_key}",
        'is_previous': 'false',
        'response_quality_data': '{"question_info":{"qid_715032638":{"number":-1,"type":"presentation_text","option_count":null,"has_other":false,"other_selected":null,"relative_position":null,"dimensions":null,"input_method":null,"is_hybrid":false},"qid_715032624":{"number":-1,"type":"presentation_text","option_count":null,"has_other":false,"other_selected":null,"relative_position":null,"dimensions":null,"input_method":null,"is_hybrid":false},"qid_715032623":{"number":1,"type":"single_choice_vertical","option_count":1,"has_other":false,"other_selected":null,"relative_position":[[0,0]],"dimensions":[1,1],"input_method":null,"is_hybrid":false},"qid_715032620":{"number":2,"type":"open_ended","option_count":null,"has_other":false,"other_selected":null,"relative_position":null,"dimensions":null,"input_method":"text_typed","is_hybrid":true},"qid_715032625":{"number":3,"type":"single_choice_vertical","option_count":3,"has_other":false,"other_selected":null,"relative_position":[[0,0]],"dimensions":[3,1],"input_method":null,"is_hybrid":false},"qid_715032621":{"number":4,"type":"open_ended","option_count":null,"has_other":false,"other_selected":null,"relative_position":null,"dimensions":null,"input_method":"text_typed","is_hybrid":true},"qid_715032626":{"number":-1,"type":"presentation_text","option_count":null,"has_other":false,"other_selected":null,"relative_position":null,"dimensions":null,"input_method":null,"is_hybrid":false},"qid_715032636":{"number":5,"type":"multiple_choice_vertical_three_col","option_count":13,"has_other":true,"other_selected":false,"relative_position":[[0,0]],"dimensions":[5,3],"input_method":null,"is_hybrid":false},"qid_715032630":{"number":6,"type":"single_choice_vertical","option_count":2,"has_other":false,"other_selected":null,"relative_position":[[1,0]],"dimensions":[2,1],"input_method":null,"is_hybrid":false},"qid_715032637":{"number":7,"type":"single_choice_vertical","option_count":2,"has_other":false,"other_selected":null,"relative_position":[[0,0]],"dimensions":[2,1],"input_method":null,"is_hybrid":false},"qid_715032622":{"number":8,"type":"single_choice_vertical","option_count":1,"has_other":false,"other_selected":null,"relative_position":[[0,0]],"dimensions":[1,1],"input_method":null,"is_hybrid":false}},"tooltip_open_count":0,"opened_tooltip":false,"start_time":1634075790177,"end_time":1634075813422,"time_spent":23245,"previous_clicked":false,"has_backtracked":false,"bi_voice":{}}',
        'disable_survey_buttons_on_submit': ''
    }

    r = requests.session()
    rep = r.post(survey_url, headers=headers, data=payload, verify=False)
    print(f"Response: {rep.status_code}")

post_survey()

today = date.today()
d4 = today.strftime("%b-%d-%Y")
# print("d4 =", d4)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

logfile = open("logfile.txt", "a")
logfile.write(d4 + " " + current_time + " : Trigger Send JHIH's form\n")
logfile.close()