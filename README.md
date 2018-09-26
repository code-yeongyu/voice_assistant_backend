# voice-assistant : 직접 만드는 음성비서
# 사용법
원활한 작동을 위하여, python 3.6.5버전의 설치를 권장합니다.
위의 명령어를 사용하여, 본 프로젝트를 다운로드 받아주세요.
 > git clone https://github.com/kim-yeon-gyu-exlock/voice_assistant_backend

이후, 프로젝트가 있는 voice_assistant 디렉토리로 이동하여 주세요. 당신이 터미널을 다룰줄 모르는 사용자라면 :

> cd voice_assistant

명령어로 이동하실 수 있습니다.

## 0. 필요한 pip 모듈 설치
 당신은 아마 필요한 모듈들이 전부 설치 되어있지 않을 것 입니다.
 따라서 다음의 명령어로 필요한 모듈들을 전부 설치 하세요 :
 
 > pip install -r requirements.txt
 
 개발서버라면, 
 
 > python manage.py runserver
 
 명령어로 개발서버를 열 수 있습니다. Gunicorn과 같은 빌드용 서버는, 검색을 통하여 만들어주세요.
 
## 1. 명령어 추가하기
 당신이 django를 잘 다루지 못한다고 하여도, 본 프로젝트를 활용하는데에는 문제가 없습니다.
 [cmd_process.py](https://github.com/kim-yeon-gyu-exlock/voice_assistant_backend/blob/master/voice_assistant/app/command_process/cmd_process.py, "cmd_process.py") 파일에서, 당신이 필요한 명령어를 쉽게 추가하고 삭제 할 수 있습니다.
 > _is_contain(text, what)
 
 함수를 통해 [text] 에 [what] 이 있는지 확인 할 수 있습니다.
 
 본 프로젝트에서는 TV 조작을 위한 기본적인 템플릿도 제공합니다.
 
 [manageTV.py](https://github.com/kim-yeon-gyu-exlock/voice_assistant_backend/blob/master/voice_assistant/app/command_process/funcs/manageTV.py, "manageTV.py")
 이 파일에서는 pyfcm 모듈을 통해, 구글의 firebase cloud messaging 으로 또 다른 앱에 알림을 보내는 역할을 합니다.
 IR센서를 갖고있는 LG 기기의 경우 [클라이언트 프로젝트](https://github.com/kim-yeon-gyu-exlock/voice_assistant_clients, "클라이언트") 를 커스텀 함으로써, 다음과 같은 구조를 통하여 원하는 작업을 할 수 있게 됩니다.
 
 > 클라이언트 앱 -> 백엔드 서버 -> fcm 서버 -> IR앱을 가진 안드로이드 스마트폰 -> IR 센서
 
 django는 파이썬을 사용하는 프레임워크인 만큼, 원하는 작업은 무엇이든 추가하여 사용이 가능합니다.
