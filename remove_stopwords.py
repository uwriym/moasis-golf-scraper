really_bad_word_list = []
bad_word_list = []
word_list = []

def eliminate_stopwords(post_text_list):
    # 불용어 제거 5단계


    # 1단계 - 공백 기준 자르기
    for word in post_text_list:
        really_bad_word_list.append(word.split())

    # 2단계 - 마침표 기준 자르기
    for list in really_bad_word_list:
        for word in list:
            bad_word_list.append(word.split('.'))

    # 3단계 - 문장부호 제거 및 두 글자 이상 불용어 제거
    for word in bad_word_list:  # 제거가 필요한 두 글자 이상 불용어 제거
        word_list.append(word[0].replace('\'', '').replace('\"', '').replace('(', '').replace(')', '') \
                         .replace('<', '').replace('>', '').replace(',', '').replace('‘', '') \
                         .replace('’', '').replace('[', '').replace(']', '').replace('=', '') \
                         .replace('했다', '').replace('이하', '').replace('해나가고', '').replace('입니다', '') \
                         .replace('있다', '').replace('대비', '').replace('전년', '').replace('동기', '') \
                         .replace('지난', '').replace('위해', '').replace('통해', '').replace('기자', '') \
                         .replace('것으', '').replace('밝혔다', '').replace('이들', '').replace('특히', '') \
                         .replace('경우', '').replace('가장', '').replace('매우', '').replace('한다', '') \
                         .replace('모든', '').replace('또한', '').replace('따라', '').replace('가장', '') \
                         .replace('이다', '').replace('최근', '').replace('보다', '').replace('가진', '') \
                         .replace('다양한', '').replace('때문', '').replace('그런데', '').replace('으로', '') \
                         .replace('합니다', '').replace('아니라', '').replace('다른', '').replace('정도', '') \
                         .replace('하지만', '').replace('것이다', '').replace('따르면', '').replace('최대', '') \
                         .replace('있어', '').replace('있고', '').replace('어떤', '').replace('하고', '') \
                         .replace('것”이라고', '').replace('저도','').replace('ㅎㅎ','').replace('감사','') \
                         .replace('^^','').replace('공이','').replace('있습니다','').replace('너무','') \
                         .replace('같습니다','').replace('그냥','').replace('ㅠㅠ','').replace('쓰고','') \
                         .replace('같습니다','').replace('ㅋㅋ','').replace('있는데','').replace('지금','') \
                         .replace('이거','').replace('투어','').replace('씁니다','').replace('같습니다','') \
                         .replace('사서','').replace('같아요','').replace('그래서','') \
                         .replace('https://www','').replace('혹시','').replace('일단','').replace('근데','') \
                         .replace('이제','').replace('사실','').replace('그래도','').replace('알고','') \
                         .replace('보고','').replace('이런','').replace('해서','').replace('오늘','') \
                         .replace('같은데','').replace('ㅎㅎㅎ','').replace('분들','').replace('그리고','') \
                         .replace('했는데','').replace('이게','').replace('보니','').replace('ㅋㅋㅋ','') \
                         .replace('보면','').replace('z765','').replace('ㅜㅜ','').replace('어제','') \
                         .replace('어느','').replace('이렇게','').replace('싶네요','').replace('하네요','') \
                         .replace('않습니다','').replace('것도','').replace('나오','').replace('감사~','') \
                         .replace('그게','').replace('^^;','').replace('있었습니다','').replace('ㄷㄷㄷ','') \
                         .replace('나옵니다','').replace('ㅋㅋㅋㅋ','').replace('안','').replace('그렇게','') \
                         .replace('되면','').replace('않고','').replace('한데','').replace('까지','') \
                         .replace('감사!','').replace('있었는데','').replace('겁니다','').replace('수록','') \
                         .replace('https://mygolfspy','').replace('듯','').replace('ㅎ','') \
                         .replace('부탁드립니다','').replace('안녕하세요','').replace('되지','').replace('하면','') \
                         .replace('같아','').replace('주문했는데','').replace('주문했습니다','').replace('하구요','') \
                         .replace('거죠','').replace('감사드립니다','').replace('!!','').replace('에요','') \
                         .replace('에서','').replace('않아서','').replace('도움이','').replace('해요','') \
                         .replace('쪽지','').replace('듯','').replace('것이','').replace('라고','') \
                         .replace('하더군요','').replace('그렇군요','').replace('이라','').replace('않을까요','') \
                         .replace('모르겠네요','').replace('텔메','').replace('s200','').replace('얼마나','') \
                         .replace('지름','').replace('없는데','').replace('Z765','').replace('jpx900','') \
                         .replace('계속','').replace('쓰면','').replace('쳐보고','')\
                         .replace('구매했는데','').replace('말씀하신','').replace('한번도','').replace('워낙','')\
                         .replace('되네요','').replace('들고','').replace('나가서','').replace('주고','').replace('왔습니다','')\
                         .replace('ㅎㅎㅎㅎ','').replace('곳이','').replace('않아','').replace('써본','').replace('인데','')\
                         .replace('이후','').replace('오오','').replace('ㄷㄷ','').replace('하죠','').replace('있는지','')\
                         .replace('모르겠습니다','').replace('하였습니다','').replace('하기','').replace('감사드려요','').replace('싶은데','')\
                         .replace('써서','').replace('만드','').replace('싶어서','').replace('부탁','').replace('말씀','')\
                         .replace('허허','').replace('몇번','').replace('감사^^','').replace('가지','').replace('못하','')\
                         .replace('먼저','').replace('나중','').replace('나중','').replace('말이죠','').replace('있군요','')\
                         .replace('많았습니다','').replace('생각','').replace('한번','').replace('정말','').replace('요즘','')\
                         .replace('공도','').replace('이상','').replace('공들','').replace('볼이','')\
                         .replace('같네요','').replace('있네요','').replace('하나','').replace('진짜','').replace('다만','')\
                         .replace('다시','').replace('물론','').replace('가지고','').replace('약간','').replace('가끔','')\
                         .replace('실제','').replace('기준','').replace('사람','').replace('됩니다','').replace('모두','')\
                         .replace('봅니다','').replace('써보고','').replace('역시','').replace('아주','').replace('아닌','')\
                         .replace('항상','').replace('분들이','').replace('그런','').replace('하는데','').replace('다음','')\
                         .replace('했습니다','').replace('오히려','').replace('아니면','').replace('답변','').replace('다들','')\
                         .replace('해도','').replace('볼들','').replace('작년','').replace('생각이','').replace('있지만','')\
                         .replace('판매','').replace('완료','').replace('나온','').replace('공들이','').replace('이번','')\
                         .replace('이건','').replace('있으면','').replace('햔재','').replace('싶습니다','').replace('종종','')
                         .replace('많아서','').replace('가서','').replace('맞습니다','')\
                         .replace('어차피','').replace('사람이','').replace('우리','').replace('크게','').replace('받아서','')\
                         .replace('가면','').replace('만든','').replace('아마','').replace('분이','').replace('없이','')\
                         .replace('댓글','').replace('사용하','').replace('아래','').replace('고맙습니다','').replace('전혀','')\
                         .replace('쳐도','').replace('대체','').replace('치고','').replace('축하드립니다','').replace('살짝','')\
                         .replace('볼도','').replace('왼쪽','').replace('완료했습니다','').replace('몇개','').replace('생각했는데','')\
                         .replace('아닌데','').replace('기억','').replace('아닐까','').replace('얼마전','').replace('굉장히','')\
                         .replace('업체','').replace('이름','').replace('당연히','').replace('납니다','').replace('이야기','')\
                         .replace(';;','').replace('참고','').replace('기분','').replace('나서','').replace('있을까요','')\
                         .replace('아직도','').replace('아니고','').replace('써도','').replace('그렇지','').replace('않을까','')\
                         .replace('아닌가요','').replace('마지막','').replace('없고','').replace('이메일','').replace('그럼','')\
                         .replace('판매하','').replace('많습니다','').replace('말고','').replace('같아서','').replace('공이라고','')\
                         .replace('제대','').replace('요새','').replace('이미','').replace('공이라','').replace('하나도','')\
                         .replace('이것도','').replace('어떻게','').replace('19','').replace('저랑','').replace('아닙니다','')\
                         .replace('잃어버리','').replace('그렇고','').replace('봐도','').replace('같기도','').replace('잃어버리고','')\
                         .replace('치면','').replace('자기','').replace('의미','').replace('사이','').replace('갖고','')\
                         .replace('나오네요','').replace('주제','').replace('얘기','').replace('무슨','').replace('자리','')\
                         .replace('사람들','').replace('그건','').replace('저렇게','').replace('훨씬','').replace('아니지만','')\
                         .replace('그거','').replace('이라고','').replace('대해','').replace('공이나','').replace('하는거','')\
                         .replace('쓰시','').replace('거기서','').replace('메일이','').replace('과거','').replace('되요','')\
                         .replace('있는데요','').replace('부터','').replace('나와서','').replace('나네요','').replace('넘게','')\
                         .replace('같고','').replace('일부러','').replace('기억이','').replace('이래저래','').replace('봤습니다','')\
                         .replace('있을','').replace('가셔서','').replace('가시면','').replace('내일','').replace('하시면','')\
                         .replace('아님','').replace('평소','').replace('나가면','').replace('들었습니다','').replace('함께','')\
                         .replace('런이','').replace('개당','').replace('하더라구요','').replace('다닙니다','').replace('중에서','')\
                         .replace('갑니다','').replace('대략','').replace('주말','').replace('스폰지밥','').replace('빼고','')\
                         .replace('비교','').replace('죄송','').replace('제외','').replace('쓰던','').replace('하여','')\
                         .replace('관련','').replace('저번','').replace('있나요','').replace('마치','').replace('이젠','')\
                         .replace('모르지만','').replace('비행기','').replace('들어','').replace('없지만','').replace('여러','')\
                         .replace('내외','').replace('원하','').replace('먹고','').replace('치는데','').replace('어디','')\
                         .replace('우라','').replace('아마도','').replace('않지만','').replace('적이','').replace('시간이','')\
                         .replace('번창하세요','').replace('빨리','').replace('샀습니다','').replace('~~~','').replace('하겠습니다','')
                         .replace('되었습니다','').replace('했더니','').replace('구할','').replace('대해서','').replace('vs','')\
                         .replace('주셔서','').replace('11번','').replace('아무래도','').replace('가요','').replace('생각하면','')\
                         .replace('싶기도','').replace('1만원','').replace('있겠지만','').replace('않나요','').replace('만큼','')\
                         .replace('이러','').replace('암튼','').replace('꺼내서','').replace('55','').replace('45','').replace('10','')\
                         .replace('되세요','').replace('드립니','').replace('적게','').replace('최소','').replace('아버지','')\
                         .replace('부분','').replace('포장지나','').replace('잘받았습니','').replace('하겠습니','').replace('듭니','')\
                         .replace('완전','').replace('좀더','').replace('되어','').replace('등등','').replace('저런','').replace('계시면','')\
                         .replace('^^;;','').replace('or','').replace('http://www','').replace('신경써주셨으면',''))


    # 4단계 - 단어 끝 조사 제거
    word_list_count = 0
    for word in word_list:
        if len(word) != 0:
            if word[-1] in '을를가은는수의로있에것와한듯?!~다ㅠ-딱':  # 제거가 필요한 한 글자 조사 추가
                word_list[word_list_count] = word[:-1]
                # print(f"{word[-1]} replaced to {word[:-1]} at {word_list_count}")
        word_list_count += 1

    # 5단계 - 한 글자 이하 단어 제거
    for word in word_list:
        if len(word) == 1 or len(word) == 0:
            try:
                for w in word_list:
                    word_list.remove(word)
            except:
                pass

        if (word == '있') or (word == '이'):
            try:
                for w in word_list:
                    word_list.remove(word)  # 잘 안 없어지는 한 글자 제거
            except:
                pass