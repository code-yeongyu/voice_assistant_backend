import random, datetime, threading
from time import sleep

from app.models import User

from app.command_process import answers
from app.command_process.signal_codes import signal_codes
from app.command_process.meals_code import MealsCode
from app.command_process.funcs import weathers, neispy, manageTV

def _is_contain(text, what) :
    if str(text).find(what) != -1 :
        return True
    return False
def _get_random_one(targetArray, addBlank=False) :
    if addBlank :
        targetArray.append('')
    return targetArray[random.randrange(0, len(targetArray))]
def _basic_answer(targetArray) :
    isAdd = random.choice([True, False])
    if isAdd :
        defaults = answers.Default.POSITIVE_STRINGS
        return _get_random_one(defaults) + " " + _get_random_one(targetArray)
    targetArray += answers.Default.POSITIVE_STRINGS
    return _get_random_one(targetArray)

class WeatherCondition(weathers.Weather) :
    def _code_to_string(self, weatherID) :
        weatherCode = int(weatherID / 100)
        if weatherCode >= 2 and weatherCode < 3 : #200대
            decoration = answers.WeatherStrings.RANDOM_STRINGS_THUNDERSTORM
            random_text = _get_random_one(decoration, True)
            weatherCondition = answers.WeatherStrings.STRING_THUNDERSTORM + random_text
        elif weatherCode >= 3 and weatherCode < 4 : #300대
            decoration = answers.WeatherStrings.RANDOM_STRINGS_DRIZZLE
            random_text = _get_random_one(decoration, True)
            weatherCondition = answers.WeatherStrings.STRING_DRIZZLE + random_text
        elif weatherCode >= 5 and  weatherCode < 6 : #500대
            decoration = answers.WeatherStrings.RANDOM_STRINGS_RAIN
            random_text = _get_random_one(decoration, True)
            weatherCondition = answers.WeatherStrings.STRING_RAIN + random_text
        elif weatherCode >= 6 and  weatherCode < 7 : #600대
            decoration = answers.WeatherStrings.RANDOM_STRINGS_SNOW
            random_text = _get_random_one(decoration, True)
            weatherCondition = answers.WeatherStrings.STRING_SNOW + random_text
        elif weatherCode >= 7 and weatherCode < 8 : #700대
            weatherCondition = answers.WeatherStrings.STRING_ATMOSPHERE
        elif weatherCode >= 8 and weatherCode < 9 : #800대
            weatherCondition = answers.WeatherStrings.STRING_CLEAR
        elif weatherID == 903 :
            weatherCondition = answers.WeatherStrings.STRING_COLD
        elif weatherID == 904 :
            weatherCondition = answers.WeatherStrings.STRING_HOT
        elif weatherID == 905 :
            weatherCondition = answers.WeatherStrings.STRING_WINDY
        else :
            weatherCondition = answers.WeatherStrings.STRING_UNKNOWN
        return weatherCondition

    def weather(self) :
        inform = self.getWeatherInformation()
        temp = inform['temperature']
        weatherID = inform['weatherID']
        return answers.WeatherStrings().weather_status(temp) + self._code_to_string(weatherID)
    def dusts(self) :
        grade = self.getDustsInformation()
        statusNow = answers.DustsStrings().dusts_status(grade)
        decoration = ""
        if grade == "좋음" :
            decoration = answers.DustsStrings.DUST_STATUS_STRINGS_GOOD
        elif grade == "보통" :
            decoration = answers.DustsStrings.DUST_STATUS_STRINGS_NORMAL
        elif grade == "나쁨" :
            decoration = answers.DustsStrings.DUST_STATUS_STRINGS_BAD
        elif grade == "매우나쁨" :
            decoration = answers.DustsStrings.DUST_STATUS_STRINGS_VERY_BAD

        return statusNow + " " + _get_random_one(decoration, True)

class Clock :
    def today(self) :
        date = datetime.datetime.now()
        num_weekday = date.weekday()
        date_string = date.strftime('%Y년 %m월 %d일')
        return answers.Today().today(num_weekday, date_string)
    def time_now(self) :
        date = datetime.datetime.now()
        sun = date.strftime('%p')
        if sun == 'AM':
            sun = "오전"
        elif sun == 'PM' :
            sun = "오후"
        date_string = sun+""+date.strftime('%l시 %M분')
        return answers.Clock().time_now(date_string)

class BasicFeatures(WeatherCondition, Clock) :
    def introduce(self) :
        return _get_random_one(answers.SelfIntroduce.INTRODUCE_STRINGS)
    def bus_informations(self) :#not yet
        pass
    def meals(self, day, user) :
        if user == "3xperse" :
            if day >= 0 and day <= 5 :
                meal = neispy.get_meals(day+7, MealsCode.MIDDLE_SCHOOL)
                if not meal == False :#false가 아닐경우
                    return answers.MealsStrings().mealsToday(meal)
            return answers.MealsStrings.STRING_NO_MEALS_TODAY#자연스레 false면 여기로 오겠지?
        return notUnderstand

class Hello(BasicFeatures) :
    greeting = ""
    weekday = ""
    inform_done = ""
    advice = ""
    brief_done = ""
    personalized = ""
    user = ""
    
    def __init__(self, user) :
        self.user = user
        self.greeting = _get_random_one(answers.BriefStrings.GREETING_STRINGS)
        self.weekday = datetime.datetime.now().weekday()
        self.informDone = _get_random_one(answers.BriefStrings.INFORMATION_DONE_STRINGS)
        self.advice = _get_random_one(answers.BriefStrings.ADVICE_STRINGS, True)
        self.brief_done = _get_random_one(answers.BriefStrings.BRIEF_DONE_STRINGS)
        if self.user == "3xperse" :
            self.personalized = answers.BriefStrings.STRING_EXPER
    
    #overloaded
    def today(self) :
        date = datetime.datetime.now()
        num_weekday = date.weekday()
        date_string = date.strftime('%Y년 %m월 %d일')
        return answers.BriefStrings().today(num_weekday, date_string)
    #overloaded
    def meals(self) :
        if self.user == "3xperse" :
            if self.weekday >= 0 and self.weekday <= 5 :
                meal = neispy.get_meals(self.weekday+7, MealsCode.MIDDLE_SCHOOL)
                if not meal == False :#false가 아닐경우
                    return answers.MealsStrings().mealsToday(meal)
            return answers.MealsStrings.STRING_NO_MEALS_TODAY#자연스레 false면 여기로 오겠지?
        return ""
    
    def brief(self) :
        result = (self.greeting + " " +
                self.user + " " + answers.BriefStrings.STRING_SIR + " " +
                self.today() + " " + self.time_now() + " " + self.weather() + " " +
                self.dusts() + " " + self.meals() +
                self.informDone + " " + self.advice +
                self.brief_done + " " + self.personalized)
        return result
    def _good_night_string(self, targetArray) :
        return (_basic_answer(answers.GoodNight.GOOD_DAY_STRINGS) +
                answers.GoodNight.STRING_GOOD_NIGHT)
    def good_night(self) :
        pass

class Tv :
    def _send_signal_thread(self, functionCode) :
        threading.Thread(target=manageTV.send_signal, args=(functionCode,)).start()
    def power(self, isRequestTurn) :
        if isRequestTurn :
            self._send_signal_thread(signal_codes.power_on.value)
            return _basic_answer(answers.Tv.POWER_ON_STRINGS)
        self._send_signal_thread(signal_codes.power_off.value)
        return _basic_answer(answers.Tv.POWER_OFF_STRINGS)
    def volume(self, isUp) :
        if isUp :
            self._send_signal_thread(signal_codes.volume_up.value)
            return _basic_answer(answers.Tv.VOLUME_UP_STRINGS)
        self._send_signal_thread(signal_codes.volume_down.value)
        return _basic_answer(answers.Tv.VOLUME_DOWN_STRINGS)
    def channel_control(self, isUp) :
        if isUp :
            self._send_signal_thread(signal_codes.channel_up.value)
            return _basic_answer(answers.Tv.CHANNEL_UP_STRINGS)
        self._send_signal_thread(signal_codes.channel_down.value)
        return _basic_answer(answers.Tv.CHANNEL_DOWN_STRINGS)
    def channel_control_specific(self, channel) :
        channel = str(channel)
        for i in range(0, len(channel)) :
            if channel[i] == '0' :
                self._send_signal_thread(18)
            else :
                self._send_signal_thread(int(channel[i])+8)
            sleep(0.01)#신호 충돌 방지
        self._send_signal_thread(42)#OK button
        return _basic_answer([answers.Tv().channel_specific(channel)])
    def mute(self) :
        self._send_signal_thread(signal_codes.mute.value)
        return _basic_answer(answers.Tv.MUTE_STRINGS)

class TvSimpleControlRepeat(Tv) :
    #all overloaded
    def _send_signal_thread(self, functionCode, level) :
        if level > 1 :
            for i in range(0, level) :
                threading.Thread(target=manageTV.send_signal, args=(functionCode,)).start()
                sleep(0.0000001)
        else :
            threading.Thread(target=manageTV.send_signal, args=(functionCode,)).start()
    def volume(self, isUp, level) :
        if isUp :
            self._send_signal_thread(signal_codes.volume_up.value, level)
            return _basic_answer(answers.Tv.VOLUME_UP_STRINGS)
        self._send_signal_thread(signal_codes.volume_down.value, level)
        return _basic_answer(answers.Tv.VOLUME_DOWN_STRINGS)
    def channel_control(self, isUp, level) :
        if isUp :
            self._send_signal_thread(signal_codes.channel_up.value, level)
            return _basic_answer(answers.Tv.CHANNEL_UP_STRINGS)
        self._send_signal_thread(signal_codes.channel_down.value, level)
        return _basic_answer(answers.Tv.CHANNEL_DOWN_STRINGS)

class Timer :
    def A_ramen_timer(self, ramenName) :#returns action
        pass
    def A_medicine_timer(self) :#returns action
        pass
def notUnderstand() :
    return _get_random_one(answers.NotUnderstand.NOT_UNDERSTOOD_STRINGS)
