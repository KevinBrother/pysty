import urllib.parse
import http.client
import json

def send_sms(mobile, text):
    host = '106.ihuyi.com'
    sms_send_uri = '/webservice/sms.php?method=Submit'

    params = urllib.parse.urlencode({
        'account': 'C64804591',
        'password': '2c99cfe4a6f37b52ee4c69ffc45115f1',
        'content': text,
        'mobile': mobile,
        'format': 'json'
    })

    headers = {
        "Content-type": 'application/x-www-form-urlencode',
        'Accept': 'text/plain'
    }

    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    rsp = conn.getresponse()
    rsp_str = rsp.read()
    conn.close()
    return rsp_str

if __name__ == "__main__":
    mobile = '13002107830'
    text = '互亿无线连接测试1111'
    print(send_sms(mobile, text))

    # b'<?xml version="1.0" encoding="utf-8"?>\n<SubmitResult xmlns="http://106.ihuyi.com/">\n<code>401</code>\n<msg>\xe5\xb8\x90\xe5\x8f\xb7\xe4\xb8\x8d\xe8\x83\xbd\xe4\xb8\xba\xe7\xa9\xba</msg>\n<smsid>0</smsid>\n</SubmitResult>\n'

    # jsonstr = rsp_str.decode('utf-8')
    # print(json.loads(jsonstr))