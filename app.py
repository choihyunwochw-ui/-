import streamlit as st
import time
import random

# 1. 페이지 설정 및 테마 입히기
st.set_page_config(page_title="프리미엄 AI 연애 코칭 리포트", page_icon="🔮", layout="centered")

st.title("🔮 프리미엄 AI 연애 코칭 시스템")
st.markdown("본 심층 진단은 사용자의 성향과 상대방의 행동 패턴을 교차 분석하여 정밀 리포트를 제공합니다.")
st.write("---")

# 2. 사이드바 - 사용자 기본 성향 입력 (디테일 추가)
st.sidebar.header("👤 내 프로필 설정")
my_mbti = st.sidebar.selectbox("나의 MBTI 성향은?", ["선택 안 함", "E형 (외향·적극)", "I형 (내향·신중)"])
attachment_style = st.sidebar.radio(
    "나의 연애 애착 유형은?",
    ["안정형 (차분하고 신뢰함)", "불안형 (연락에 집착하거나 불안함)", "회피형 (구속을 싫어하고 거리둠)"]
)

# 3. 메인 화면 - 상세 상황 입력
st.markdown("### 📝 STEP 1. 상대방과의 현주소")
col1, col2 = st.columns(2)

with col1:
    relation_period = st.selectbox(
        "알게 된(또는 만난) 기간",
        ["1주일 미만", "1개월 내외", "3개월~6개월", "6개월 이상 장기전"]
    )
with col2:
    meet_frequency = st.selectbox(
        "오프라인 만남 횟수 (최근 한 달)",
        ["만난 적 없음", "1~2회", "3~5회", "주 2회 이상 자주"]
    )

st.markdown("### 💬 STEP 2. 카톡 및 연락 패턴 딥다이브")
chat_speed = st.select_slider(
    "상대방의 평균 답장 속도는 어떤가요?",
    options=["빛보다 빠른 칼답", "30분 이내", "1~2시간 사이", "반나절 이상 걸림", "읽씹/안읽씹 속수무책"]
)

chat_length = st.radio(
    "상대방의 주로 보내는 말의 길이는?",
    ["질문과 이모티콘이 가득한 장문/다독형", "적당한 문장과 리액션형", "단답형 (ㅇㅇ, ㅋㅋ, 그랬구나)", "용건만 간단히 히치하이커형"]
)

st.markdown("### 🔬 STEP 3. 핵심 고민 키워드 (복수 선택)")
options = st.multiselect(
    "현재 가장 걱정되는 부분을 모두 골라주세요.",
    ["선톡이 전혀 안 와요", "약속을 잡으려고 하면 흐지부지돼요", "할 말이 고갈됐어요", "전 애인 이야기가 나왔어요", "상대방 주변에 이성 친구가 많아요"],
    default=["할 말이 고갈됐어요"]
)

# 4. 분석 및 정밀 리포트 생성
if st.button("📊 심층 연애 코칭 리포트 발행하기"):
    
    with st.status("🔮 연애 데이터 알고리즘 가동 중...", expanded=True) as status:
        st.write("🔄 입력된 성향 데이터 매칭 중...")
        time.sleep(1.0)
        st.write("💬 카톡 텍스트 및 연락 빈도 가중치 계산 중...")
        time.sleep(1.0)
        st.write("⚖️ 종합 해결 대책 및 솔루션 수립 중...")
        time.sleep(0.8)
        status.update(label="✅ 분석 완료! 아래 리포트를 확인하세요.", state="complete")
        
    st.write("---")
    st.markdown("## 📋 AI 종합 연애 진단 리포트")
    
    # 가상 점수 산출 로직 (디테일화)
    base_score = 50
    if "칼답" in chat_speed: base_score += 25
    elif "30분" in chat_speed: base_score += 15
    elif "반나절" in chat_speed: base_score -= 15
    elif "속수무책" in chat_speed: base_score -= 25
    
    if "장문" in chat_length: base_score += 20
    elif "단답" in chat_length: base_score -= 10
    
    if "주 2회" in meet_frequency: base_score += 15
    elif "만난 적 없음" in meet_frequency: base_score -= 15
    
    # 점수 바운더리 제한 (0~100)
    final_score = max(5, min(base_score, 100))
    
    # 3대 지수 세부 분석 (UI 시각화 업그레이드)
    st.markdown("### 📊 3대 관계 지수")
    c1, c2, c3 = st.columns(3)
    
    # 점수에 따른 서브 점수 무작위성+보정 반영
    interest_rate = min(final_score + random.randint(5, 10), 100) if final_score > 40 else max(final_score - 10, 5)
    green_light = final_score
    danger_rate = 100 - final_score
    
    c1.metric(label="❤️ 상대방의 호감도", value=f"{interest_rate}%")
    c2.metric(label="🟢 그린라이트 확률", value=f"{green_light}%")
    c3.metric(label="⚠️ 관계 위험도", value=f"{danger_rate}%")
    
    st.progress(final_score / 100)
    
    # 5. 맞춤형 심층 솔루션 처방전
    st.markdown("### 💊 AI 맞춤형 행동 지침")
    
    # 애착 유형별 경고
    if "불안형" in attachment_style:
        st.warning(f"⚠️ **{my_mbti if my_mbti != '선택 안 함' else '사용자'}님을 위한 애착 팁:** 현재 불안형 성향이 발동하여 상대방의 답장 속도에 과도하게 의미부여를 하고 있을 가능성이 큽니다. 휴대폰을 잠시 내려놓고 개인 취미에 집중하여 '연락의 도파민'을 분산시키세요.")
    
    # 종합 분석 결과 문구
    if final_score >= 80:
        st.balloons()
        st.success(
            "🏆 **[현재 상태: 고백 직전 프리패스]**\n\n"
            "상대방은 이미 당신에게 마음의 문을 활짝 열었습니다. 카톡 스타일과 만남 횟수 모두 긍정적 신호를 가리키고 있습니다.\n\n"
            "**💡 다음 행동 지침:**\n"
            "1. 카톡으로 시시콜콜한 이야기를 길게 늘어뜨리지 마세요. 대화의 핵심은 오프라인 만남이어야 합니다.\n"
            "2. 다음 만남에서 정적(Silent)이 흐르는 타이밍에 지긋이 눈을 맞추며 진심 어린 칭찬을 건네보세요. 분위기가 무르익었을 때 고백해도 좋습니다."
        )
    elif final_score >= 50:
        st.info(
            "⚖️ **[현재 상태: 밀고 당기기 안개 정국]**\n\n"
            "호감은 분명히 있으나, 확신이 부족하거나 상대방이 연애보다 다른 일(학업, 업무)로 바쁜 상태일 수 있습니다.\n\n"
            "**💡 다음 행동 지침:**\n"
            f"1. 선택하신 고민 중 **'{', '.join(options)}'** 문제를 해결하기 위해서는 억지로 텐션을 올리기보다, 상대방의 일상 템포에 맞춰주는 센스가 필요합니다.\n"
            "2. '뭐해?' 대신 상대방이 좋아하는 주제(예: 좋아하는 유튜버, 최근 유행하는 밈)의 링크를 툭 던지며 자연스럽게 대화를 유도하세요."
        )
    else:
        st.error(
            "🚨 **[현재 상태: 관계 재정비 및 인내 필요]**\n\n"
            "현재 상대방의 에너지가 당신을 향하고 있지 않거나, 다소 부담을 느끼고 있는 차가운 상태입니다.\n\n"
            "**💡 다음 행동 지침:**\n"
            "1. **선톡 금지령:** 당분간 3일 동안은 먼저 절대 연락하지 마세요. 상대방에게 당신의 빈자리를 느낄 시간적 여유를 주어야 합니다.\n"
            "2. 프로필 사진을 너무 감정적인 글귀나 우울한 사진으로 바꾸지 마세요. 오히려 잘 지내고 있는 당당한 일상 사진을 올리는 것이 호기심을 유발하는 데 좋습니다."
        )

    # 6. 미니 게임/시뮬레이션 기능 추가
    st.write("---")
    st.markdown("### 🎮 돌발 상황 대처 능력 테스트")
    st.write("만약 데이트 도중 상대방이 **'저 오늘 좀 피곤한 것 같아요'**라고 말한다면, 당신의 답변은?")
    
    test_choice = st.radio(
        "선택지를 골라보세요:",
        ["1. 아 진짜요? 그럼 얼른 집 들어가서 쉬셔야겠어요! (보내주기)", 
         "2. 에휴, 제가 재미없게 해 드려서 피곤한가 봐요... (자책하기)", 
         "3. 어쩐지 안색이 안 좋아 보였어요. 근처에 조용한 카페 가서 잠깐 쉴까요? (배려하기)"]
    )
    
    if st.button("정답 확인"):
        if "1." in test_choice:
            st.warning("🟡 절반의 정답! 배려심은 있어 보이지만, '나랑 있는 게 귀찮나?'라는 오해를 살 수도 있어요. 가벼운 아쉬움은 표현해 주는 것이 좋습니다.")
        elif "2." in test_choice:
            st.error("🔴 오답! 상대방에게 감정적 부채감(미안함)을 주어 기분을 더 무겁게 만드는 최악의 답변입니다.")
        else:
            st.success("🟢 대정답! 상대방의 컨디션을 챙기면서도 함께 시간을 보내고 싶다는 호감을 동시에 전달하는 센스 만점 답변입니다.")

# 7. 하단 푸터
st.write("---")
st.caption("🔮 AI 연애 코칭 Ver 2.0 • 데이터 기반 행동 교정 프로그램")
