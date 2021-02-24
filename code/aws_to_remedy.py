# pylint: disable=E1101
import zeep
from lxml import etree
from requests import Session
from zeep import Client
from zeep.transports import Transport
from zeep.wsse.username import UsernameToken
import json
import urllib3
import boto3
from boto3.dynamodb.conditions import Key


#=================================================================================================
# Function: alarm_to_remedy
# Purpose:  Lambda funtion used to integrate  CloudWatch Alarmns with a SOAP Web Services
# Author : Leonardo Solano 
# This function has the ability to send a cloudwatch alarm using SOAP cliente 
#==================================================================================================


def lambda_handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    Corporate_ID = message['AWSAccountId']
    Customer_ID = int(Corporate_ID)
    account = query_account(Customer_ID)
    customer = account[0]['Empresa']
    Alarm = message['AlarmDescription']
    Alarm_Summary = message['AlarmName']
    instanceid = message['Trigger']['Dimensions'][0]['value']
    wsdl = 'your wsdl enpoint'
    session = Session()
    session.verify = False
    transport = Transport(session=session)
    client = zeep.Client(wsdl=wsdl,transport=transport)
    auth_ele = client.get_element('ns0:AuthenticationInfo') 
    auth = auth_ele(userName='<username>', password='<password>')

    print (client.service.<your method>(Corporate_ID, customer, Alarm, Alarm_Summary,instanceid,_soapheaders=[auth]))

def query_account(account, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('<table nale>')
    response = table.query(
        KeyConditionExpression=Key('Account_ID').eq(account)
    )
    return response['Items']

    return reservations
