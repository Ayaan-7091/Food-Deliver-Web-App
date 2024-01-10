
import os
from twilio.rest import Client




def sms(order_msg):
    account_sid = "ACe4b1aa8729765d1802bf3b312e6de6bb"
    auth_token = "a7c092f54c57cbecca0e18d809ce9ac8"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=order_msg,
                        from_='+19045721420',
                        to='+919924253037'
                       
                    )
    # print("sms sent")
