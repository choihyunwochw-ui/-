import streamlit as st
import time

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="초정밀 AI 연애 진단 시스템", page_icon="🕵️‍♂️", layout="centered")

st.title("🕵️‍♂️ 초정밀 AI 연애 진단 및 솔루션")
st.markdown("본 진단은 10가지 세부 문항을 통해 상대방의 심리와 관계를 다각도로 분석합니다. 신중하게 답변해 주세요.")
st.write("---")

# 사용자 기본 정보
name = st.text_input("당신의 닉네임", value="매력쟁이")

st.write("")
st.markdown("### 📊 영역별 세부 문항 입력")

# 탭을 나누어 많은 문항을 깔끔하게 정리
tab1, tab2, tab3, tab4 = st.tabs(["📱 1. 연락 패턴", "☕ 2. 만남과 태도", "💬 3. 대화 내용", "⚡ 4. 직감과 시그널"])

# 각 문항별 점수를 담을 딕셔너리 초기화
scores = {}

# --- TAB 1: 연락 패턴 (3문항) ---
with tab1:
    st.subheader("상대방과의 연락 스타일 분석")
    
    q1 = st.radio(
        "1. 상대방의 평균 답장 속도는 어떤가요?",
        ["활동 시간 기준, 대부분 10분 이내 칼답 (15점)", 
         "1시간 내외로 성의 있게 옴 (12점)", 
         "2~3시간 이상 불규칙하게 옴 (7점)", 
         "반나절 이상 걸리거나 읽씹/안읽씹이 잦음 (2점)"]
    )
    scores['q1'] = 15 if "10분" in q1 else (12 if "1시간" in q1 else (7 if "2~3시간" in q1 else 2))

    q2 = st.radio(
        "2. 선톡(먼저 보내는 연락)의 비율은 어떻게 되나요?",
        ["상대방이 먼저 보내는 경우가 더 많다 (15점)", 
         "반반 정도로 비슷하게 주고받는다 (12점)", 
         "대부분 내가 먼저 보내야 대화가 시작된다 (6점)", 
         "최근에는 선톡을 서로 거의 안 한다 (1점)"]
    )
    scores['q2'] = 15 if "더 많다" in q2 else (12 if "반반" in q2 else (6 if "내가 먼저" in q2 else 1))

    q3 = st.radio(
        "3. 밤이나 주말(공백기)에도 연락이 끊기지 않고 이어지나요?",
        ["자기 전이나 주말에도 끊김 없이 티키타카가 잘 된다 (10점)", 
         "낮에는 잘 되다가 밤이나 주말에는 뜸해진다 (7점)", 
         "용건이 끝나면 자연스럽게 대화가 종료된다 (4점)"]
    )
    scores['q3'] = 10 if "끊김 없이" in q3 else (7 if "밤이나 주말" in q3 else 4)


# --- TAB 2: 만남과 태도 (3문항) ---
with tab2:
    st.subheader("오프라인 만남의 질과 빈도 분석")
    
    q4 = st.radio(
        "4. 다음 데이트 약속을 잡을 때 상대방의 반응은?",
        ["적극적으로 날짜와 장소를 제안하거나 내 의견에 바로 맞춘다 (15점)", 
         "보자는 말에는 동의하지만 구체적인 계획은 흐지부지된다 (8점)", 
         "바쁘다는 핑계로 확답을 피하거나 미룬다 (3점)"]
    )
    scores['q4'] = 15 if "적극적으로" in q4 else (8 if "흐지부지" in q4 else 3)

    q5 = st.radio(
        "5. 만났을 때 상대방이 나에게 집중하는 정도는?",
        ["휴대폰을 거의 보지 않고 내 눈을 보며 대화에 몰입한다 (15점)", 
         "가끔 휴대폰을 확인하지만 대화는 무리 없이 이어진다 (10점)", 
         "휴대폰을 자주 보거나 주변 시선에 신경을 많이 쓴다 (4점)"]
    )
    scores['q5'] = 15 if "거의 보지 않고" in q5 else (10 if "가끔 휴대폰" in q5 else 4)

    q6 = st.radio(
        "6. 데이트 비용 지불이나 선물(기프티콘 포함) 성향은 어떤가요?",
        ["먼저 계산하려고 하거나, 내가 사면 다음에 꼭 본인이 산다 (10점)", 
         "눈치껏 번갈아 가며 내는 편이다 (8점)", 
         "주로 내가 더 많이 내고 상대는 대접받는 것에 익숙해 보인다 (2점)"]
    )
    scores['q6'] = 10 if "먼저 계산" in q6 else (8 if "눈치껏" in q6 else 2)


# --- TAB 3: 대화 내용 (2문항) ---
with tab3:
    st.subheader("대화의 깊이와 관심도 분석")
    
    q7 = st.radio(
        "7. 상대방이 나에 대한 '질문'을 얼마나 하나요?",
        ["내 취향, 일상, 과거 등 나에 대한 질문을 끊임없이 던진다 (10점)", 
         "내가 물어보는 말에 대답하고 가끔 리액션성 질문을 한다 (7점)", 
         "주로 본인 이야기만 하거나 질문이 거의 없다 (2점)"]
    )
    scores['q7'] = 10 if "끊임없이" in q7 else (7 if "리액션성" in q7 else 2)

    q8 = st.radio(
        "8. 내가 이전에 했던 사소한 말들을 기억하고 있나요?",
        ["지나가듯 말한 음식, 취향, 스케줄을 놀라울 정도로 잘 기억한다 (10점)", 
         "큰 사건이나 중요한 약속 정도는 기억한다 (7점)", 
         "했던 말을 또 해야 하거나 자주 까먹는다 (2점)"]
    )
    scores['q8'] = 10 if "놀라울 정도로" in q8 else (7 if "중요한 약속" in q8 else 2)


# --- TAB 4: 직감과 시그널 (2문항) ---
with tab4:
    st.subheader("은밀한 호감 시그널 체크")
    
    q9 = st.radio(
        "9. 은근한 칭찬이나 플러팅(호감 표현)이 있나요?",
        ["'예쁘다/멋지다', '너 같은 사람 만나면 좋겠다' 등 직설적인 편이다 (5점)", 
         "스타일이 좋다거나 성격이 좋다는 식의 간접적 칭찬을 한다 (4점)", 
         "칭찬보다는 장난을 치거나 친구 대하듯 편하게만 대한다 (2점)"]
    )
    scores['q9'] = 5 if "직설적" in q9 else (4 if "간접적" in q9 else 2)

    q10 = st.radio(
        "10. 나와 대화할 때 리액션과 웃음의 빈도는 어떤가요?",
        ["별거 아닌 말에도 잘 웃어주고 리액션이 고래등 수준이다 (5점)", 
         "적당히 미소를 지으며 무난하게 호응해 준다 (4점)", 
         "영혼 없는 리액션이거나 다소 건조하다 (1점)"]
    )
    scores['q10'] = 5 if "고래등" in q10 else (4 if "무난하게" in q10 else 1)

st.write("---")

# 4. 종합 점수 계산 및 결과 도출
if st.button("🔮 10대 문항 초정밀 분석 리포트 발행"):
    
    # 총점 계산 (만점: 100점)
    total_score = sum(scores.values())
    
    with st.status("🧬 데이터 정밀 매칭 및 관계 시뮬레이션 가동 중...", expanded=True) as status:
        time.sleep(1.0)
        st.write("📈 연락-만남-대화 데이터 가중치 밸런싱 중...")
        time.sleep(1.0)
        st.write("🎯 맞춤형 행동 양식 도출 완료.")
        status.update(label="진단 완료!", state="complete")
        
    st.markdown(f"## 📝 {name}님의 초정밀 종합 진단서")
    
    # 점수 레이아웃 시각화
    col_score, col_status = st.columns(2)
    with col_score:
        st.metric(label="💘 최종 호감도 지수 (만점: 100점)", value=f"{total_score} 점")
    with col_status:
        if total_score >= 85:
            st.success("등급: 🟢 고백 직전 그린라이트 프리패스")
        elif total_score >= 60:
            st.info("등급: 🟡 호감 탐색 및 밀당 구간")
        elif total_score >= 40:
            st.warning("등급: 🟠 정체기 또는 단순 호의 구간")
        else:
            st.error("등급: 🔴 위험! 짝사랑 역주행 또는 어장 경보")

    st.progress(total_score / 100)
    
    # 하위 영역별 스코어 분석 서머리
    st.markdown("### 🔍 영역별 분석 요약")
    
    contact_score = scores['q1'] + scores['q2'] + scores['q3'] # 만점 40
    meet_score = scores['q4'] + scores['q5'] + scores['q6']    # 만점
