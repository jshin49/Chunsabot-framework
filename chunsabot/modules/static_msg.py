# -*- coding: utf-8 -*-

from chunsabot.botlogic import brain, Botlogic


@brain.route(u"정보유출", no_params=True)
def fool():
    return u".정보유출은 만우절 장난입니다!"
    # return u"[{0}님의 정보 유출 확인]\r\n유출된 정보 내역은 다음과 같습니다. \r\n이름, 회원 ID, 그룹 내 회원수, 오늘의 날짜 (.오늘)\r\n유출되지 않은 정보 내역은 다음과 같습니다. \r\n대화 내역, 그룹 이름, 그룹 내 회원 이름".format(confirm)

@brain.route(u"더보기", no_params=True)
def message():
    return u"""현재 수호천사의 최대 동시 접속한 방이 10000 방을 넘었고, 1초에 100개가 넘는 메시지를 보내고 있습니다.
몇몇 메시지가 프로토콜상의 한계로 정상적으로 보내지지 않고 있습니다.(헤롱) 
봇 API가 정식으로 제공되지 전까지 계속 이 문제가 발생할 수 있습니다."""
    #현재 수호천사봇이 사용하는 pykakao 라이브러리의 쓰기 기능이 굉장히 불안정하여, 메시지 처리 후 메시지가 정상적으로 가지 않는 문제가 발생하고 있습니다. (눈물) \r\n라이브러리의 안정성이 개선되거나 봇 API가 정식으로 제공되지 전까지는 봇의 기능이 갑자기 정지될 수 있습니다."

@brain.route(u"계정", no_params=True)
def pm():
    return u"""이전에 사용하던 수호천사가 차단된 경우 말을 듣지 않습니다.
또한, 차단된 계정에 접근할 수 없기 때문에 방을 나갈 수도 없습니다.(눈물) 
계정이 차단된다면 다른 계정을 사용하여 다시 운영할 수 있습니다.
페이스북 페이지
http://fb.com/chunsab
를 통해서 계정 관련 정보를 전달해 드립니다."""
    #return u"안녕하세요! \r\n카카오톡 번호 관련 문제로, 제 번호에 연결된 카카오톡 계정은 실제 제가 쓰는 계정이 아닙니다.\r\n혹시 제 개인 계정인 줄 알고 이 계정에 톡을 보내셨다면, 저에게 문자를 남겨주세요. \r\n제가 쓰는 계정의 ID를 알려드리겠습니다."

@brain.route(u"달라진점", no_params=True)
def new():
    return u"""[달라진 점]
1. 내부 구조가 변경되었습니다."""
#1. 드디어 마피아가 추가되었습니다! (.마피아) \r\n2. .일정, .날씨 자동예보, .정시알림 기능이 추가되었습니다.(Scheduler 추가) 
#1. 배우기에 대한 많은 로직이 개선되었습니다! (.새로운배우기 참고) \r\n2. .조용히 모드의 버그를 수정하였습니다."
#0. .더보기가 안먹히던 문제를 해결하였습니다! (당황)\r\n1. 이제 단어에 대한 감정을 가르칠 수 있습니다! \r\n.감정 을 입력해 보세요.\r\n2. 배우기의 일부 내용이 차단, 삭제되었습니다."
#1. 메시지가 가끔 씹히는 문제를 해결 중입니다.\r\n2. 무작위, 주사위의 랜덤이 부정확한 문제를 해결했습니다. \r\n3. 업앤다운의 범위가 0부터 99까지로 변경되었습니다."

@brain.route([u"도움말", u"사용법", u"사용", u"명령어", u"", u"안녕"], no_params=True)
def info():
    return u"""
사용하는 법 : 마침표 (.) 으로 시작하는 단어만 인식합니다.
.감정 .나가 .날씨 .달라진점 .업앤다운 .무작위 .배우기 .오늘 .주사위 .조용히 .지우기 .짤배우기 .통계 .URL검증 .만든이 .유튜브 .짤 .짤리스트 .짤지우기
봇이 너무 시끄러우면 .조용히 를 입력해 보세요."""

@brain.route([u"만든이", u"만든놈", u"만든사람", u"제작자", u"제작"], no_params=True)
def about():
    return u"""수호천사 @ {0}
(내부 버전 {1})
made by 고려대학교 정보대학 이수호
me@suseme.me
""".format(Botlogic.__version__, Botlogic.__intversion__)
