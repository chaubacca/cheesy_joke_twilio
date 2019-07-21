'''
Carmen Chau
Jul 2019
Test project following CleverProgrammer's instructions

Used Git Bash to install twilio API using command 'pip install twilio'
The specific function 'Client' is imported from the twilio.rest API module
The credentials file includes sensitive personal information which I have saved separately from the source code
'''

from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

my_msg = "What did the cheese say to the bear behind it?"

message = client.messages.create(
                            to=my_cell,
                            from_=my_twilio,
                            body=my_msg)

print(message.sid)




