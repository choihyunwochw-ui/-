import streamlit as st
import time

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="AI 연애 코칭 센터", page_icon="💖", layout="centered")

st.title("💖 AI 연애 코칭 챗봇")
st.subheader("당신의 썸과 연애, 시원하게 진단해 드립니다.")
st.write("---")

# 2. 사용자 정보 및 상황 입력 받기
st.markdown("### 📋 현재 나의 상황 체크")

# 이름 입력
name = st.text_input("당신의 닉네임을 입력해 주세요", value="인생은타이밍")

# 상황 선택 (라디오 버튼)
status = st.radio(
    "현재 어떤 단계인가요?",
    ("짝사랑 중 (그 사람의 마음을 모르겠어요)", 
     "썸 타는 중 (고백 타이밍을 잡고 싶어요)", 
     "연애 중 (최근 자꾸 싸워서 고민이에요)", 
     "이별 후 (재회를 바라고 있어요)")
)

# 최근 주고받은 카톡 스타일 (셀렉트 박스)
chat_style = st.selectbox(
    "그 사람의 카톡 답장 스타일은 어떤가요?",
    [
        "칼답에 질문도 자주 온다",
        "답장은 오는데 주로 단답형이다 (ㅇㅇ, ㅋㅋ, 그랬구나)",
        "읽씹이나 안읽씹이 잦다 (몇 시간 뒤에 옴)",
        "용건이 있을 때만 연락한다"
    ]
)

# 3. 코칭 로직 및 결과 출력 버튼
if st.button("💘 연애 코칭 결과 보기"):
    
    # 로딩 애니메이션
    with st.spinner("연애 세포 분석 중... 잠시만 기다려주세요..."):
        time.sleep(1.5)
        
    st.success("🎯 분석이 완료되었습니다!")
    st.write("---")
    
    # 변수 초기화
    score = 50
    advice = ""
    
    # 상황별 & 카톡 스타일별 맞춤형 조언 알고리즘 (간단한 규칙 기반)
    if "짝사랑" in status:
        if "칼답" in chat_style:
            score = 85
            advice = f"**[{name}님을 위한 조언]** 상대방도 당신에게 호감이 있을 확률이 매우 높습니다! 명확한 약속(단둘이 맛집 가기 등)을 잡아 자연스럽게 단계를 올려보세요."
        elif "단답형" in chat_style or "몇 시간" in chat_style:
            score = 40
            advice = f"**[{name}님을 위한 조언]** 현재 상대방의 관심도가 다소 낮을 수 있습니다. 선톡을 조금 줄이고, 상대방이 흥미를 느낄 만한 공통 관심사(취미, 맛집)를 먼저 파악해 보세요."
        else:
            score = 30
            advice = f"**[{name}님을 위한 조언]** 지금 몰아붙이면 부담을 느낄 수 있습니다. 한 걸음 물러나 나만의 매력을 키우며 타이밍을 다시 노리세요."

    elif "썸" in status:
        if "칼답" in chat_style:
            score = 95
            advice = f"**[{name}님을 위한 조언]** 골대가 비었습니다! 슛을 차세요! 이번 주말 분위기 좋은 곳에서 진심을 담아 고백하는 것을 강력 추천합니다."
        elif "단답형" in chat_style:
            score = 60
            advice = f"**[{name}님을 위한 조언]** 카톡보다는 '만남'에 집중해야 합니다. 만나서 대화할 때 리액션을 아끼지 말고, 상대방의 진짜 성향을 파악해 보세요."
        else:
            score = 45
            advice = f"**[{name}님을 위한 조언]** 썸이 길어지면 지치기 마련입니다. 약간의 '밀당(연락 빈도 조절)'을 통해 상대방의 반응을 살펴보세요."

    elif "연애 중" in status:
        score = 70
        if "칼답" in chat_style:
            advice = f"**[{name}님을 위한 조언]** 다투더라도 소통의 끈은 이어져 있네요. 서운한 점을 말할 때는 '너 왜 그래?'가 아니라 '네가 그러니까 내 마음이 속상했어(I-Message)' 화법을 써보세요."
        else:
            advice = f"**[{name}님을 위한 조언]** 대화의 온도 차가 느껴집니다. 자존심 싸움은 내려놓고, 따뜻한 포옹이나 진솔한 사과로 감정의 앙금을 먼저 풀어주는 것이 우선입니다."

    elif "이별 후" in status:
        score = 20
        advice = f"**[{name}님을 위한 조언]** 지금 당장 장문의 카톡을 보내는 것은 금물! 감정이 격해진 상태에서는 역효과가 납니다. 최소 2주~한 달간 이성적으로 생각할 시간을 가진 뒤 가볍게 안부를 물으세요."

    # 4. 결과 시각화 (점수 및 조언)
    st.markdown(f"### 📊 {name}님의 연애 성공/관계 지수")
    
    # 점수에 따른 프로그레스 바 및 텍스트 색상 변경
    st.progress(score)
    
    if score >= 80:
        st.balloons() # 축하 효과
        st.subheader(f"🟢 그린라이트! 점수: {score}점")
    elif score >= 50:
        st.subheader(f"🟡 주의 요망 (옐로우라이트), 점수: {score}점")
    else:
        st.subheader(f"🔴 경고 (레드라이트), 점수: {score}점")
        
    # 처방전 박스 형태로 출력
    st.info(advice)

# 5. 하단 푸터
st.write("---")
st.caption("⚠️ 본 코칭은 재미로 보는 인공지능 진단이며, 실제 연애는 타이밍과 진심이 가장 중요합니다! 🍀")
