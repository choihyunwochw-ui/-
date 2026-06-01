import streamlit as st
import time
import random

# 1. 페이지 설정
st.set_page_config(page_title="초정밀 AI 연애 성향 진단", page_icon="🔮", layout="centered")

st.title("🔮 초정밀 AI 연애 심층 진단 시스템")
st.markdown("본 진단은 질문의 점수가 공개되지 않으며, 무작위로 출제되는 문항과 성향 분석을 통해 정밀한 결과를 도출합니다.")
st.write("---")

# 2. 사용자 프로필 및 성향 입력
st.markdown("### 👤 STEP 1. 나의 성향 정보 입력")
name = st.text_input("당신의 닉네임을 적어주세요", value="매력쟁이")

col_mbti, col_type = st.columns(2)
with col_mbti:
    my_mbti = st.selectbox(
        "나의 MBTI 유형은?",
        ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", 
         "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
    )
with col_type:
    attachment_style = st.selectbox(
        "나의 연애 애착 유형은?",
        ["안정형 (불안감이 적고 신뢰를 바탕으로 연애)", 
         "불안형 (연락에 민감하고 상대의 변심을 쉽게 걱정)", 
         "회피형 (구속을 싫어하고 친밀해질수록 거리를 둠)",
         "공포회피형 (상처받기 두려워 마음을 쉽게 열지 못함)"]
    )

st.write("---")
st.markdown("### 📝 STEP 2. 연애 상황 심층 문항")
st.caption("답변에 따른 점수는 비공개이며, 질문 순서는 매번 무작위로 변경됩니다.")

# 3. 질문 데이터베이스 정의
all_questions = [
    {
        "id": "q1",
        "text": "💡 상대방의 평균 답장 속도는 어떤가요?",
        "options": ["활동 시간 기준, 대부분 10분 이내 칼답", "1시간 내외로 성의 있게 옴", "2~3시간 이상 불규칙하게 옴", "반나절 이상 걸리거나 읽씹/안읽씹이 잦음"],
        "scores": [15, 12, 7, 2],
        "category": "연락"
    },
    {
        "id": "q2",
        "text": "💡 선톡(먼저 보내는 연락)의 비율은 어떻게 되나요?",
        "options": ["상대방이 먼저 보내는 경우가 더 많다", "반반 정도로 비슷하게 주고받는다", "대부분 내가 먼저 보내야 대화가 시작된다", "최근에는 선톡을 서로 거의 안 한다"],
        "scores": [15, 12, 6, 1],
        "category": "연락"
    },
    {
        "id": "q3",
        "text": "💡 밤이나 주말(공백기)에도 연락이 끊기지 않고 이어지나요?",
        "options": ["자기 전이나 주말에도 끊김 없이 티키타카가 잘 된다", "낮에는 잘 되다가 밤이나 주말에는 뜸해진다", "용건이 끝나면 자연스럽게 대화가 종료된다"],
        "scores": [10, 7, 4],
        "category": "연락"
    },
    {
        "id": "q4",
        "text": "💡 다음 데이트 약속을 잡을 때 상대방의 반응은 어떤가요?",
        "options": ["적극적으로 날짜와 장소를 제안하거나 내 의견에 바로 맞춘다", "보자는 말에는 동의하지만 구체적인 계획은 흐지부지된다", "바쁘다는 핑계로 확답을 피하거나 미룬다"],
        "scores": [15, 8, 3],
        "category": "만남"
    },
    {
        "id": "q5",
        "text": "💡 만났을 때 상대방이 나에게 집중하는 정도는?",
        "options": ["휴대폰을 거의 보지 않고 내 눈을 보며 대화에 몰입한다", "가끔 휴대폰을 확인하지만 대화는 무리 없이 이어진다", "휴대폰을 자주 보거나 주변 시선에 신경을 많이 쓴다"],
        "scores": [15, 10, 4],
        "category": "만남"
    },
    {
        "id": "q6",
        "text": "💡 데이트 비용 지불이나 선물 성향은 어떤가요?",
        "options": ["먼저 계산하려고 하거나, 내가 사면 다음에 꼭 본인이 산다", "눈치껏 번갈아 가며 내는 편이다", "주로 내가 더 많이 내고 상대는 대접받는 것에 익숙해 보인다"],
        "scores": [10, 8, 2],
        "category": "만남"
    },
    {
        "id": "q7",
        "text": "💡 상대방이 나에 대한 '질문'을 얼마나 하나요?",
        "options": ["내 취향, 일상, 과거 등 나에 대한 질문을 끊임없이 던진다", "내가 물어보는 말에 대답하고 가끔 리액션성 질문을 한다", "주로 본인 이야기만 하거나 질문이 거의 없다"],
        "scores": [10, 7, 2],
        "category": "대화"
    },
    {
        "id": "q8",
        "text": "💡 내가 이전에 했던 사소한 말들을 기억하고 있나요?",
        "options": ["지나가듯 말한 음식, 취향, 스케줄을 놀라울 정도로 잘 기억한다", "큰 사건이나 중요한 약속 정도는 기억한다", "했던 말을 또 해야 하거나 자주 까먹는다"],
        "scores": [10, 7, 2],
        "category": "대화"
    },
    {
        "id": "q9",
        "text": "💡 은근한 칭찬이나 플러팅(호감 표현)이 있나요?",
        "options": ["'예쁘다/멋지다', '너 같은 사람 없다' 등 직설적인 편이다", "스타일이 좋다거나 성격이 좋다는 식의 간접적 칭찬을 한다", "칭찬보다는 장난을 치거나 친구 대하듯 편하게만 대한다"],
        "scores": [5, 4, 2],
        "category": "대화"
    },
    {
        "id": "q10",
        "text": "💡 나와 대화할 때 리액션과 웃음의 빈도는 어떤가요?",
        "options": ["별거 아닌 말에도 잘 웃어주고 리액션이 엄청나다", "적당히 미소를 지으며 무난하게 호응해 준다", "영혼 없는 리액션이거나 다소 건조하다"],
        "scores": [5, 4, 1],
        "category": "대화"
    }
]

# 4. 세션 상태를 이용해 최초 1회만 질문 무작위 셔플하도록 고정
if 'shuffled_questions' not in st.session_state:
    shuffled = all_questions.copy()
    random.shuffle(shuffled)
    st.session_state['shuffled_questions'] = shuffled

# 5. 데이터 안전성을 위해 폼(Form) 구조 도입
with st.form(key='coaching_form'):
    user_selections = {}
    
    # 셔플된 질문 출력 및 사용자 선택값 임시 저장
    for i, q in enumerate(st.session_state['shuffled_questions']):
        st.markdown(f"#### Q{i+1}. {q['text']}")
        # 각 라디오 버튼이 충돌하지 않도록 고유한 key 부여
        choice = st.radio(
            label=f"Q{i+1}_label", 
            options=q['options'], 
            label_visibility="collapsed", 
            key=f"radio_key_{q['id']}"
        )
        user_selections[q['id']] = choice
        st.write("")
        
    # 폼 내부의 제출 버튼
    submit_button = st.form_submit_button(label="🔮 초정밀 심층 리포트 열람하기")

# 6. 버튼 클릭 시 결과 연산 및 출력 (Form 외부가 아니라 이 조건 안에서 완결)
if submit_button:
    with st.status("🧬 MBTI 및 애착 유형 분석 엔진 가동 중...", expanded=True) as status:
        time.sleep(0.8)
        st.write(f"📊 {my_mbti} 성향의 인지 필터 적용 중...")
        time.sleep(0.8)
        st.write(f"⚖️ {attachment_style.split(' ')[0]}에 따른 인지 왜곡 가중치 보정 중...")
        time.sleep(0.4)
        status.update(label="진단 완료!", state="complete")
        
    st.write("---")
    st.markdown(f"## 📋 {name}님의 성향 기반 종합 진단서")
    
    # 실제 점수 및 카테고리 누적 계산
    base_score = 0
    contact_score = 0
    meet_score = 0
    talk_score = 0
    
    for q in all_questions:
        user_choice = user_selections[q['id']]
        idx = q['options'].index(user_choice)
        score_value = q['scores'][idx]
        
        base_score += score_value
        if q['category'] == "연락":
            contact_score += score_value
        elif q['category'] == "만남":
            meet_score += score_value
        elif q['category'] == "대화":
            talk_score += score_value

    # 성향 보정치 계산
    mbti_comment = ""
    attachment_comment = ""
    
    if "F" in my_mbti:
        mbti_comment = "감정(F) 성향이 강해 상대방의 사소한 행동이나 말투 변화에 에너지를 많이 쓰고 계실 수 있습니다. 때로는 너무 깊은 의미 부여보다 단순하게 생각하는 것이 관계에 도움이 됩니다."
    else:
        mbti_comment = "이성(T) 성향이 강해 상대방의 행동을 지나치게 인과관계나 논리로만 분석하려 할 수 있습니다. 연애는 논리가 아닌 감정의 영역임을 기억해 주세요."
        
    if "불안형" in attachment_style:
        base_score = min(base_score + 5, 100)
        attachment_comment = "현재 '불안형' 애착이 발동하면 상대방의 답장이 조금만 늦어져도 '나한테 식었나?'하고 오해하기 쉽습니다. 객관적 데이터보다 본인의 불안감이 신호를 왜곡할 수 있으니 한 템포 쉬어가세요."
    elif "회피형" in attachment_style:
        base_score = max(base_score - 3, 0)
        attachment_comment = "상대방과 너무 가까워지면 본능적으로 구속감을 느껴 거리를 두려고 할 수 있습니다. 상대방의 호감을 귀찮음으로 오해하고 있지 않은지 점검해 보세요."
    else:
        attachment_comment = "안정적인 애착 성향을 가지고 계시므로 상대방의 시그널을 비교적 가장 객관적이고 정확하게 파악하고 계십니다."

    # 최종 시각화 및 등급 출력
    st.markdown("### 📊 AI 종합 판단 점수")
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="❤️ 보정 후 최종 호감 지수", value=f"{base_score}점")
    with c2:
        if base_score >= 85:
            st.success("등급: 🟢 그린라이트 프리패스")
        elif base_score >= 60:
            st.info("등급: 🟡 밀당 및 호감 탐색 단계")
        elif base_score >= 40:
            st.warning("등급: 🟠 정체기 또는 단순 호의")
        else:
            st.error("등급: 🔴 관계 재정비 필요 (위험)")

    st.progress(base_score / 100)
    
    st.write("")
    st.markdown("### 🔍 세부 영역별 스코어")
    rc1, rc2, rc3 = st.columns(3)
    rc1.markdown(f"**📱 연락 지수:** {contact_score}/40점")
    rc2.markdown(f"**☕ 만남 지수:** {meet_score}/40점")
    rc3.markdown(f"**💬 대화 지수:** {talk_score}/20점")
    
    st.write("---")
    st.markdown("### 🧠 성향 크로스 분석 결과")
    st.info(f"🧬 **{name}님의 성향 맞춤 분석:**\n\n* **MBTI 가이드:** {mbti_comment}\n* **애착 유형 가이드:** {attachment_comment}")
    
    st.markdown("### 💡 종합 행동 지침")
    if base_score >= 85:
        st.balloons()
        st.markdown(f"상대방은 이미 {name}님께 푹 빠져 있습니다. 본인의 성향({my_mbti})대로 솔직하게 직진하셔도 좋습니다. 고백 타이밍을 잡으세요!")
    elif base_score >= 60:
        st.markdown(f"서로에게 호감은 있으나 확신이 부족합니다. 카톡보다는 **만남 지수**를 높일 수 있는 단둘만의 스케줄을 잡는 데 집중하세요.")
    elif base_score >= 40:
        st.markdown(f"상대방이 당신을 단순 지인으로 생각할 확률이 높습니다. {name}님의 매력을 새롭게 어필할 수 있는 '반전 타이밍'이 필요합니다. 연락을 조금 줄여보세요.")
    else:
        st.markdown(f"현재 관계의 비대칭이 심각합니다. 마음은 아프지만 한 걸음 물러나 혼자만의 시간을 가지며 상대방의 반응을 기다리는 것이 최선입니다.")
