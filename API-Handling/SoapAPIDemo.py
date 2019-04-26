import json
import requests
from pprint import pprint

import requests
from suds.client import Client
from googleads import adwords
import boto3


def calculator_api_using_requests():
    url = "http://www.dneonline.com/calculator.asmx?WSDL"
    # headers = {'content-type': 'application/soap+xml'}
    headers = {'content-type': 'text/xml'}
    num1, num2 = 10, 30
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:Add>
         <tem:intA>{0}</tem:intA>
         <tem:intB>{1}</tem:intB>
      </tem:Add>
   </soapenv:Body>
</soapenv:Envelope>""".format(num1, num2)
    headers = {"key": "value"}
    response = requests.post(url, data=body, headers=headers)
    print(response.content)


def calculator_api_using_suds():
    url = "http://www.dneonline.com/calculator.asmx?WSDL"
    # url = "http://www.webservicex.net/country.asmx?wsdl"
    client = Client(url)
    num1, num2 = 30, 10
    print(client)
    # print("ConvertTemp: ", client.service.GetCountries())
    # print("Add: ", client.service.Add(num1, num2))
    # print("Subtract: ", client.service.Subtract(num1, num2))
    # print("Add: ", client.service.Multiply(num1, num2))
    # print("Multiply: ", client.service.Divide(num1, num2))


def sample():
    # url = "http://www.dneonline.com/calculator.asmx?WSDL"
    url = "https://adwords.google.com/api/adwords/ch/v201802/CustomerSyncService?wsdl"
    client = Client(url)
    num1, num2 = 30, 10
    print(client)
    # print("ConvertTemp: ", client.service.GetCountries())


def get_adwords_campaigns():
    url = "https://adwords.google.com/api/adwords/cm/v201802/CampaignService?wsdl"
    suds_client = Client(url)
    # print(suds_client)
    PAGE_SIZE = 100
    offset = 0

    _version = 'v201708'
    # _SOAP_HEADER_CLASS = ('{https://adwords.google.com/api/adwords/cm/%s}SoapHeader')
    _SOAP_HEADER_CLASS = ('{https://adwords.google.com/api/adwords/cm/%s}RequestHeader')
    from suds.sax.element import Element
    from suds.sax.attribute import Attribute
    developer_token = Element('developerToken').setText('amMTJYUbjPRmEbCQjq8t9w')
    client_customer_id = Element('clientCustomerId').setText('787-554-4940')
    user_agent = Element('userAgent').setText('Python Session Demo')
    validate_only = Element('validateOnly').setText(False)
    partial_failure = Element('partialFailure').setText(False)
    header_list = [developer_token, client_customer_id, user_agent, validate_only, partial_failure]
    suds_client.set_options(soapheaders=header_list)

    selector = {
        'fields': ['Id', 'Name', 'Date', 'StartDate', 'EndDate', 'Status'],
        'paging': {
            'startIndex': str(offset),
            'numberResults': str(PAGE_SIZE)
        }
        , 'dateRange': {'min': '2018-02-27', 'max': '2018-02-27'}
    }
    print(suds_client.service.get(selector))


if __name__ == '__main__':
    # calculator_api_using_requests()
    calculator_api_using_suds()
    # get_adwords_campaigns()
    # sample()
