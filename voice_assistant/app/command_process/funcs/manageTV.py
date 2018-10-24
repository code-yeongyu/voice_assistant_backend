#sends fcmNotification

import json
from time import sleep
from pyfcm import FCMNotification

api_key = "<api_key_here>"
registration_id = "<registration_id_here>"


def send_signal(functionCode):
    """functionCode를 FCM서버로 보내는 함수
    
    Arguments:
        functionCode {[int]} -- [IR센서의 명령 코드, signal_codes.py 참고]
    
    Returns:
        [True] -- [명령을 보내는 것을 성공하였음]
        [False] -- [명령을 보내는 것을 실패하였음]
    """

    push_service = FCMNotification(api_key=api_key)
    message_title = ""
    message_body = str(functionCode)
    result = push_service.notify_single_device(
        registration_id=registration_id,
        message_title=message_title,
        message_body=message_body)  # 기기로 티비와 관련된 명령어를 보냄
    if result['success'] == 1:
        return True
    return False