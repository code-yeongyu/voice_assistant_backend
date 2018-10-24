"""
str 타입의 데이터를 통해 액션을 수행시키는 코드입니다.
"""

import datetime, re
from app.command_process import actions
import app.command_process.answers as answers
import app.command_process.phone_action as phone_action


def _is_contain(text, what):
    if str(text).find(what) != -1:
        return True
    return False


def link_commands(cmd, user):
    user = str(user)
    content = _link_by_words(cmd, user)
    if not content:  #제대로 못 알아 들었을때
        return {'response': actions.notUnderstand(), 'action': ''}

    return {'response': content['response'], 'action': content['action']}


def _link_by_words(cmd, user):
    """단어를 통하여 액션과 연결시키는 함수
    
    Arguments:
        cmd {[str]} -- [사용자의 명령 값]
        user {[str]} -- [명령을 요쳥한 유저의 유저네임]
    
    Returns:
        [{'response':<response>, 'action':<action>}] -- [response: 기기에 전달할 응답 메시지,
                                                        action: 기기로 보낼 추가 메시지 (클라이언트 측의 코드 변경을 통하여 원하는 작업을 지시 할 수 있음)]
    """

    response = ""
    action = ""
    if _is_contain(cmd, "버스"):  #버스
        response = actions.BasicFeatures().bus_informations()
        return {'response': response, 'action': action}

    elif _is_contain(cmd, "누구"):  #자기소개
        response = actions.BasicFeatures().introduce()
        return {'response': response, 'action': action}

    elif _is_contain(cmd, "날씨"):  #날씨
        response = actions.BasicFeatures().weather()
        return {'response': response, 'action': action}

    elif _is_contain(cmd, "급식"):  #급식
        response = actions.BasicFeatures().meals(
            datetime.datetime.now().weekday(), user)
        return {'response': response, 'action': action}

    elif _is_contain(cmd, "티비") or _is_contain(cmd, "TV") or _is_contain(
            cmd, "tv"):  #티비 컨트롤
        #볼륨 조절
        if _is_contain(cmd, "소리") or _is_contain(cmd, "볼륨"):
            #볼륨 높이기
            if _is_contain(cmd, "키워") or _is_contain(cmd, "높") or _is_contain(
                    cmd, "올"):
                try:
                    level = int(re.findall('\d+', cmd)[0])
                    response = actions.TvSimpleControlRepeat().volume(
                        True, level)
                except:
                    response = actions.Tv().volume(True)
                return {'response': response, 'action': action}
            #볼륨 낮추기
            elif _is_contain(cmd, "줄여") or _is_contain(
                    cmd, "낮") or _is_contain(cmd, "내"):
                try:
                    level = int(re.findall('\d+', cmd)[0])
                    response = actions.TvSimpleControlRepeat().volume(
                        False, level)
                except:
                    response = actions.Tv().volume(False)
                return {'response': response, 'action': action}
        #채널 조절
        elif _is_contain(cmd, "채널"):
            #번호로 조작
            if _is_contain(cmd, "높") or _is_contain(cmd, "올") or _is_contain(
                    cmd, "낮") or _is_contain(cmd, "내"):  #단순 조작 모음
                #채널 up
                if _is_contain(cmd, "높") or _is_contain(cmd, "올"):
                    try:
                        level = int(re.findall('\d+', cmd)[0])
                        response = actions.TvSimpleControlRepeat(
                        ).channel_control(True, level)
                    except:
                        response = actions.Tv().channel_control(True)
                    return {'response': response, 'action': action}
                #채널 down
                elif _is_contain(cmd, "낮") or _is_contain(cmd, "내"):
                    try:
                        level = int(re.findall('\d+', cmd)[0])
                        response = actions.TvSimpleControlRepeat(
                        ).channel_control(False, level)
                    except:
                        response = actions.Tv().channel_control(False)
                    return {'response': response, 'action': action}
            elif _is_contain(cmd, "번") or _is_contain(
                    cmd, "틀어") or _is_contain(cmd, "돌려") or _is_contain(
                        cmd, "바꿔"):
                try:
                    channel = int(re.findall('\d+', cmd)[0])
                except:
                    return False
                response = actions.Tv().channel_control_specific(channel)
                return {'response': response, 'action': action}
        #전원 조작
        elif _is_contain(cmd, "켜") or _is_contain(cmd, "틀어"):
            response = actions.Tv().power(True)
            return {'response': response, 'action': action}
        elif _is_contain(cmd, "꺼"):
            response = actions.Tv().power(False)
            return {'response': response, 'action': action}
        #'TV'까지만 알아들었을때
        elif _is_contain(cmd, "무음") or _is_contain(cmd, "음소거"):
            response = actions.Tv().mute()
            return {'response': response, 'action': action}
        response = answers.AskAgain.STRING_TV
        action = phone_action.action().ask_again_in("TV")
        return {'response': response, 'action': action}
    #채널, 볼륨 변경시 서술어 필요 없음
    elif _is_contain(cmd, "소리") or _is_contain(cmd, "볼륨"):
        #볼륨 높이기
        if _is_contain(cmd, "키워") or _is_contain(cmd, "높") or _is_contain(
                cmd, "올"):
            try:
                level = int(re.findall('\d+', cmd)[0])
                response = actions.TvSimpleControlRepeat().volume(True, level)
            except:
                response = actions.Tv().volume(True)
            return {'response': response, 'action': action}
        #볼륨 낮추기
        elif _is_contain(cmd, "줄여") or _is_contain(cmd, "낮") or _is_contain(
                cmd, "내"):
            try:
                level = int(re.findall('\d+', cmd)[0])
                response = actions.TvSimpleControlRepeat().volume(False, level)
            except:
                response = actions.Tv().volume(False)
            return {'response': response, 'action': action}
    elif _is_contain(cmd, "채널"):
        #번호로 조작
        if _is_contain(cmd, "높") or _is_contain(cmd, "올") or _is_contain(
                cmd, "낮") or _is_contain(cmd, "내"):  #단순 조작 모음
            #채널 up
            if _is_contain(cmd, "높") or _is_contain(cmd, "올"):
                try:
                    level = int(re.findall('\d+', cmd)[0])
                    response = actions.TvSimpleControlRepeat().channel_control(
                        True, level)
                except:
                    response = actions.Tv().channel_control(True)
                return {'response': response, 'action': action}
            #채널 down
            elif _is_contain(cmd, "낮") or _is_contain(cmd, "내"):
                try:
                    level = int(re.findall('\d+', cmd)[0])
                    response = actions.TvSimpleControlRepeat().channel_control(
                        False, level)
                except:
                    response = actions.Tv().channel_control(False)
                return {'response': response, 'action': action}
        elif _is_contain(cmd, "번") or _is_contain(cmd, "틀어") or _is_contain(
                cmd, "돌려") or _is_contain(cmd, "바꿔"):
            try:
                channel = int(re.findall('\d+', cmd)[0])
            except:
                return False
            response = actions.Tv().channel_control_specific(channel)
            return {'response': response, 'action': action}
        elif cmd[0].isdigit() and _is_contain(cmd, "번"):  #채널 변경시 서술어 필요 없음
            try:
                channel = int(re.findall('\d+', cmd)[0])
            except:
                return False
            response = actions.Tv().channel_control_specific(channel)
            return {'response': response, 'action': action}
    elif cmd[0].isdigit() and _is_contain(cmd, "번"):
        try:
            channel = int(re.findall('\d+', cmd)[0])
        except:
            return False
        response = actions.Tv().channel_control_specific(channel)
        return {'response': response, 'action': action}

    elif _is_contain(cmd, "타이머"):  #타이머
        #약 타이머
        if _is_contain(cmd, "약"):
            response = actions.Timer().A_medicine_timer()
            return {'response': response, 'action': action}
        #'타이머'까지만 알아들었을때
        response = answers.AskAgain.STRING_TIMER
        action = phone_action.action()
        return {'response': response, 'action': action}

    elif _is_contain(cmd, "브리핑"):  #브리핑
        response = actions.Hello(user).brief()
        return {'response': response, 'action': action}

    elif _is_contain(cmd, "몇시") or _is_contain(cmd, "몇 시") or _is_contain(
            cmd, "시간"):  #시간
        response = actions.BasicFeatures().time_now()
        return {'response': response, 'action': action}

    elif _is_contain(cmd, "몇일") or _is_contain(cmd, "며칠") or _is_contain(
            cmd, "몇 일") or _is_contain(cmd, "날짜"):  #날짜
        response = actions.BasicFeatures().today()
        return {'response': response, 'action': action}

    #elif _is_contain(cmd, "미세먼지") or _is_contain(cmd, "미세 먼지"):#sk 플래닛 open api지원 중단으로 인한 임시 사용 중단
    #    response = actions.BasicFeatures().dusts()
    #    return {'response':response, 'action':action}

    else:  #이해 못했을 때
        return False

    return False
