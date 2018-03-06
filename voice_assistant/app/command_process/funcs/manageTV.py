#sends fcmNotification

import json
from time import sleep
from pyfcm import FCMNotification

api_key = "<api_key_here>"
registration_id = "<registration_id_here>"

def send_signal(functionCode) :
    push_service = FCMNotification(api_key=api_key)
    message_title = ""
    message_body = str(functionCode)
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    if result['success'] == 1 :
        return True
    return False