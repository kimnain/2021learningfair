print("안녕하세요 맞춤형 역사콘텐츠 추천 프로그램입니다.")
while True:

    sel=input("장르를 선택하세요(영화/드라마): ")
    if sel=="영화":
        time=input("시기를 선택하세요(병자호란/6.25): ")
        if time=="병자호란":
            print("")
            print("'남한산성'을 추천합니다.")
            print("나아갈 곳도 물러설 곳도 없는 고립무원의 남한산성")
            print("나라의 운명이 그곳에 갇혔다!")
            print("")
            ans=input("마음에 드시나요?(예/아니오): ")
            if ans=="예":
                print("프로그램을 종료합니다.")
                break

        
        else:
            print("")
            print("'태극기 휘날리며'를 추천합니다.")
            print('"우린 반드시 살아서 돌아가야 해"')
            print("세계 역사상 가장 끔직한 전쟁으로 평가되는 한국전쟁")
            print("하지만, 전쟁을 겪은 한 개인에게 중요한 것은 오직...")
            print("")
            ans=input("마음에 드시나요? (예/아니오): ")
            if ans=="예":
                print("프로그램을 종료합니다.")
                break
            
    else:
        time=input("시기를 선택하세요(조선시대/신미양요): ")
        if time=="조선시대":
            print("")
            print("'허준'을 추천합니다. ")
            print('"세상에서 의원을 높이 알아주건 안 알아주건 간에,')
            print('의원의 소임은 생명을 다루는 것이니, 그 어느 생업보다도 고귀한 일이다."')
            print("조선시대 최고의 명의이자, 동의보감의 저자 허준의 일대기")
            print("")
            ans=input("마음에 드시나요? (예/아니오): ")
            if ans=="예":
                print("프로그램을 종료합니다.")
                break
        else:
            print("")
            print("'미스터 션샤인'을 추천합니다. ")
            print("뜨겁고 의로운 이름, 의병(義兵)")
            print("역사는 기록하지 않았으나 우리는 기억해야 할,")
            print("무명의 의병들...")
            print("")
            ans=input("마음에 드시나요? (예/아니오): ")
            if ans=="예":
                print("프로그램을 종료합니다.")
                break
