class Default :
    POSITIVE_STRINGS = ['네.', '알겠습니다.']

class AskAgain :
    STRING_TV = "TV조작 어떤걸 할까요?"
    STRING_LAPTOP = "노트북에다가 뭘 할까요?"
    STRING_TIMER = "어떤것에 대한 타이머를 설정 할까요?"

class WeatherStrings :
    STRING_THUNDERSTORM = "천둥 번개가 치고있어요. "
    STRING_DRIZZLE = "이슬비가 내립니다. "
    STRING_RAIN = "비가 옵니다. "
    STRING_SNOW = "눈이 옵니다. "
    STRING_ATMOSPHERE = "좀 뿌얘요."
    STRING_CLEAR = "맑아요."
    STRING_COLD = "좀 추워요."
    STRING_HOT = "좀 더워요."
    STRING_WINDY = "바람이 조금 불어요."
    STRING_UNKNOWN = "잘 모르겠어요."

    RANDOM_STRINGS_THUNDERSTORM = ['후덜덜.', '어후 무서워라.', '무서워요.']
    RANDOM_STRINGS_DRIZZLE = ['이슬비 내리는 이른 아침에. 죄송합니다. 노래 불러보고 싶었어요.', '비는 역시 집 안에서 감상해야 좋은 법이죠.']
    RANDOM_STRINGS_RAIN = ['감상하기 좋군요.', '비는 역시 구경할때가 제일 좋아요.', '저는 빗소리 좋아해요.']
    RANDOM_STRINGS_SNOW = ['눈은 언제 봐도 예쁜 것 같아요.', '눈 밟는 소리를 들으면 졸려운 이유는 익숙하지 않은 소리라서 그렇대요.', '정말 춥겠어요.']

    def weather_status(self, temp) :
        return "현재 기온은 약 "+str(temp)+"도이며, "

class MealsStrings :
    STRING_NO_MEALS_TODAY = "오늘은 급식이 없습니다."

    def mealsToday(self, meal) :
        contents = "오늘의 급식은 "+meal+" 입니다."
        return contents

class DustsStrings :
    DUST_STATUS_STRINGS_GOOD = ["상쾌한 공기를 즐기세요!"]
    DUST_STATUS_STRINGS_NORMAL = ["나쁘진 않아요.", "문제가 될 정도는 아니에요.", "안심하게 숨 쉴만 하겠네요."]
    DUST_STATUS_STRINGS_BAD = ["마스크 쓰는것 잊지마세요!", "마스크는 필수 입니다!", "오늘은 꼭! 마스크 끼셔야해요!"]
    DUST_STATUS_STRINGS_VERY_BAD = ["오늘은 심각합니다. 마스크 꼭 쓰셔야 해요.", "마스크 없이는 많이 위험합니다.", "외출 시 마스크를 착용 하시는걸 매우 권장합니다."]
    
    def dusts_status(self, grade) :
        return "오늘 미세먼지의 농도는 "+grade+"입니다."

class Today :
    _WEEKDAY = ['월', '화', '수', '목', '금', '토', '일']
    def today(self, num_weekday, date_string) :
        return "오늘은 "+ date_string + " " + self._WEEKDAY[num_weekday]+"요일 입니다."

class Clock :
    def time_now(self, time):
        return "현재 시각은 "+str(time)+"입니다."

class BriefStrings(Today) :
    STRING_EXPER = "오늘도 아침 일기 작성하는 것 잊지 마세요!"
    STRING_SIR = "님."
    GREETING_STRINGS = ['안녕히 주무셨나요', '안녕히 주무셨습니까', '좋은 아침입니다', '즐거운 하루가 시작됬습니다']
    INFORMATION_DONE_STRINGS = ["오늘의 브리핑은 이정도로 끝내겠습니다.", "오늘의 브리핑은 이정도에서 마칠게요.", "오늘 브리핑은 여기까지 하겠습니다."]
    ADVICE_STRINGS = ["잠에 들기전 후회없는 하루를 만들기 위해 노력해봅시다!", "내일 생각했을때 후회 할 일을 하지 맙시다.", "스티브 잡스는 오늘을 늘 마지막날인것 처럼 살라고 했습니다.", "시간은 금입니다.", "어쩌면 오늘을 열심히 살다가 얻은 아이디어가 세상을 바꿀수도 있습니다.", "페이팔의 창립자이자 스페이스 X, 그리고 테슬라의 CEO인 엘론 머스크는 늘 5분 단위로 쪼개 생활 한다고 합니다."]
    BRIEF_DONE_STRINGS = ["즐거운 하루 되세요!", "뿌듯한 오늘을 만들어봐요!", "힘차게 하루를 보내봐요!", "즐겁게 보내봅시다!", "오늘도 행복한 하루를 보냅시다!", "열정적인 하루를 보내봅시다!"]

    def today(self, num_weekday, date_string) :
        return "오늘은 "+ date_string + " " + self._WEEKDAY[num_weekday]+"요일이며,"

class Tv :
    POWER_ON_STRINGS = ['TV 켰어요','TV를 켰어요', 'TV를 켰습니다.', 'TV 켰어요.']
    POWER_OFF_STRINGS = ['TV 껐어요.', 'TV를 껐어요', 'TV를 껐습니다.', 'TV 껐어요.']
    CHANNEL_UP_STRINGS = ['채널을 올렸어요.', '채널을 올렸어요.', '채널을 올렸습니다.']
    CHANNEL_DOWN_STRINGS = ['채널을 내렸어요.', '채널을 내렸어요.', '채널을 내렸습니다.']
    VOLUME_UP_STRINGS = ['볼륨을 올렸어요.', '볼륨을 올렸어요.', '볼륨을 올렸습니다.']
    VOLUME_DOWN_STRINGS = ['볼륨을 내렸어요.', '볼륨을 내렸어요.', '볼륨을 내렸습니다.']
    MUTE_STRINGS = ['무음모드 신호를 보냈습니다.', 'TV를 무음으로 만들었습니다.']
    HDMI1_STRINGS = ['HDMI1 신호를 보냈습니다', 'HDMI1로 변경하였습니다.']
    HDMI2_STRINGS = ['HDMI2 신호를 보냈습니다', 'HDMI2로 변경하였습니다.']
    def channel_specific(self, channel) :
        return str(channel)+"번을 틀었습니다."

class NotUnderstand :
    NOT_UNDERSTOOD_STRINGS = ['죄송합니다만, 제대로 이해하지 못했습니다.', '뭐라고 말하셨는지 못알아들었네요.', '이런. 못알아들었어요.']

class SelfIntroduce :
    INTRODUCE_STRINGS = ["저는 김비서입니다. 주인님의 명령을 받으면 여러가지 잡다한 일들을 대신 수행해드립니다.", "저는 김비서입니다. 티비키는 용도로도 사용하실 수 있고, 그것뿐만 아니라 여러 기능을 사용하실 수 있습니다. 예를들면, 급식을 물어보거나 버스정류장 정보를 조회 하실 수 있고, 공기질의 상태를 확인 하실 수 있습니다."]
    EASTER_EGG = "김연규님이 저를 개발 해 주셨어요."

class GoodNight :
    GOOD_DAY_STRINGS = ['오늘도 수고하셨습니다.', '좋은 하루 보내셨나요?', '좋은하루 되셨나요?', '즐거운 하루 보내셨나요?']
    STRING_GOOD_NIGHT = '안녕히 주무세요.'