import re, requests
import app.models


def _findAndRemove(text, target):
    text = str(text)
    return text.replace(target, "", text.count(target))


def _removeTrashes(meals, day):
    trashes = [
        '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '⑪', '⑫', '⑬'
    ]  # 영양 성분을 의미하는 특수문자 제거
    for t in trashes:
        meals[day] = _findAndRemove(meals[day], t)
    meals[day] = meals[day].replace("<br />", ", ",
                                    meals[day].count("<br />") - 1)
    meals[day] = _findAndRemove(meals[day], "<br />")
    meals[day] = re.sub('[1234567890.]', '', meals[day])
    return meals[day]


def get_meals(day, schoolcode):
    meals = requests.get(
        "http://stu.goe.go.kr/sts_sci_md01_001.do?schulCode=" + schoolcode +
        "&schulCrseScCode=3&schulKndScCode=03&schMmealScCode=2"
    ).text  # 급식을 파싱 해 옴
    meals = re.findall('<td class="textC">(.+)</td>', meals)
    day = day
    if not meals == []:
        if not meals[day] == ' ':
            return _removeTrashes(meals, day)  # 급식 리턴
    return False
