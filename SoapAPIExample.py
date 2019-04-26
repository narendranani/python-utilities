import urllib3


def addition():
    url = "http://www.dneonline.com/calculator.asmx"
    headers = {'content-type': 'text/xml'}
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:Header/>   <soapenv:Body>      <tem:Add>
         <tem:intA>12</tem:intA>         <tem:intB>14</tem:intB>      </tem:Add>   </soapenv:Body></soapenv:Envelope>"""
    http = urllib3.PoolManager()
    response = http.request('POST', url, headers=headers, body=body)

    # body = json.loads(response.content)
    print("response.content", response.data)


addition()
