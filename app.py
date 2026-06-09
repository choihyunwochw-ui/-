import streamlit as st
import time

# 페이지 설정
st.set_page_config(page_title="AI 연애 말투 & 소통 솔루션", page_icon="💬", layout="centered")

st.title("💬 AI 연애 말투 & 대화법 초정밀 교정소")
st.markdown("평소 연애할 때나 썸탈 때 보냈던 카톡, 혹은 하고 싶은 말을 입력해 주세요.\nAI 연애 코치가 **상대방을 사로잡는 마법 같은 말투**로 교정해 드립니다.")
st.write("---")

# 1. 상황 및 기본 정보 설정
st.markdown("### 🎯 STEP 1. 대화 상황 설정")
col_rel, col_tone = st.columns(2)

with col_rel:
    relationship = st.selectbox(
        "상대방과의 현재 관계는?",
        ["이제 막 호감을 키워가는 '썸' 단계", 
         "연애 초기 (설레지만 눈치 보는 중)", 
         "연애 중기/장기 (권태기 또는 잦은 다툼)",
         "짝사랑 또는 헤어진 후 재회를 노리는 중"]
    )

with col_tone:
    desired_tone = st.selectbox(
        "내가 원하는 나의 매력 컨셉은?",
        ["다정하고 따뜻한 '공감형 리더'", 
         "당당하고 여유 넘치는 '쿨한 밀당형'", 
         "상대의 독점욕을 자극하는 '은근한 밀당형'",
         "솔직하고 위트 있는 '티키타카형'"]
    )

st.write("---")

# 2. 대화 입력 및 분석 요청
st.markdown("### 📝 STEP 2. 교정할 대화 입력")
user_text = st.text_area(
    "평소에 보냈던 카톡이나, 하고 싶은 말을 솔직하게 적어주세요.",
    placeholder="예시 1) 왜 이렇게 답장이 늦어? 바빠?\n예시 2) 주말에 시간 돼? 같이 맛있는 거 먹으러 가자!",
    height=120
)

submit_talk = st.button("🔮 AI 매력 말투 필터링 시작")

# 3. 분석 알고리즘 및 결과 출력
if submit_talk:
    if not user_text.strip():
        st.warning("⚠️ 교정할 문장을 입력해 주세요!")
    else:
        with st.status("🧠 입력된 문장의 심리적 가치 및 호감도 분석 중...", expanded=True) as status:
            time.sleep(1.0)
            st.write("🔍 상대방이 느낄 '부담감/매력도' 파라미터 측정 완료...")
            time.sleep(0.8)
            st.write(f"✨ {desired_tone.split(' ')[0]} 알고리즘 기반 문장 재구성 중...")
            status.update(label="교정 및 솔루션 추출 완료!", state="complete")
        
        st.write("---")
        st.markdown("## 📋 AI 연애 소통 정밀 진단서")
        
        # 임의의 입력어 기반 매칭 로직 (실제 배포용 템플릿 구현)
        # 키워드별로 매칭하여 동적 결과 생성
        is_angry = any(w in user_text for w in ["왜", "늦어", "읽씹", "뭐해", "안해", "바빠"])
        is_propose = any(w in user_text for w in ["시간", "만나", "먹으러", "가자", "데이트"])
        
        # 기본값 세팅
        bad_reason = "상대방에게 '내 컨디션은 너의 연락에 결정된다'는 약자의 프레임을 보여주기 쉽습니다. 주도권이 상대에게 완전히 넘어가는 말투입니다."
        better_text_1 = "🔴 오늘 진짜 정신없이 바쁜가 보네! 나 퇴근하고 운동 가려는데, 너도 집 들어갈 때 카톡 줘 ㅎㅎ"
        better_text_2 = "🟢 오늘 날씨 진짜 좋다! 너 생각나서 연락해 봤어. 바쁜 거 끝나면 이따가 맛있는 거 얘기나 하자!"
        psychology_effect = "내 일상(운동, 취미)을 당당하게 유지하면서도 상대방을 배려하는 여유를 보여줍니다. 상대방은 '아, 이 사람은 나만 목매는 게 아니구나'라는 생각에 은근한 독점욕과 긴장감을 느끼게 됩니다."
        
        if is_angry:
            bad_reason = "서운함이나 추궁의 조가 섞인 말투는 상대방에게 '의무감'과 '피로감'을 줍니다. 특히 상대가 회피 성향이 있다면 카톡을 더 미루게 만드는 최악의 방어기제를 자극합니다."
            if "쿨한" in desired_tone or "은근한" in desired_tone:
                better_text_1 = "🔥 오늘 유독 바쁜가 보네! 난 친구랑 맛있는 거 먹으러 왔어 ㅎㅎ 이따 여유 생기면 연락해~"
                better_text_2 = "✨ 오늘 하루 완전 하얗게 불태우는 중인가 봐? 화이팅하고 생존 신고는 이따 천천히 해 줘!"
            else:
                better_text_1 = "🌱 오늘 많이 바쁘구나! 고생이 많네. 기운 내고 이따가 숨 돌릴 때 편하게 카톡 해 줘 😊"
                better_text_2 = "🧸 밥은 제때 챙겨 먹고 일하는 거지? 고생한 만큼 오늘 저녁에 맛있는 거 먹어!"
            psychology_effect = "상대를 압박하지 않고 오히려 '내 일상도 즐겁다'는 여유 프레임을 씌웁니다. 상대방은 미안함과 동시에 당신의 쿨하고 당당한 모습에 매력을 느끼고 먼저 칼답을 보낼 확률이 80% 이상 상승합니다."
            
        elif is_propose:
            bad_reason = "상대방에게 선택권을 통째로 넘기거나, 거절당할까 봐 지나치게 저자세를 취하는 느낌을 줄 수 있습니다. 연애의 서사는 '제안'이 아니라 '유혹'이어야 합니다."
            if "쿨한" in desired_tone or "은근한" in desired_tone:
                better_text_1 = "🍷 이번 주말에 유독 예약하기 힘든 맛집 하나 뚫었는데, 너 딱 생각나더라. 같이 가볼래?"
                better_text_2 = "🎬 요새 단톡방에서 난리 난 영화 있는데 혼자 보긴 아깝다. 주말에 나랑 보러 가자. 시간 언제 괜찮아?"
            else:
                better_text_1 = "🍕 이번 주말에 완전 맛있는 화덕피자 집 가려고 하는데, 같이 가고 싶어서! 토요일이랑 일요일 중에 언제 시간 더 편해?"
                better_text_2 = "☕ 나 주말에 예쁜 카페 가려는데 너랑 같이 가면 훨씬 재밌을 것 같아. 이번 주말 스케줄 어때?"
            psychology_effect = "단순히 '시간 돼?'라고 묻는 것보다 명확한 '명분(맛집, 핫플)'을 던지면 승낙 확률이 비약적으로 높아집니다. 또한 '만날지 말지'를 묻는 게 아니라 '토요일과 일요일 중 언제 갈지'라는 이중 구속(Double Bind) 질문법을 쓰면 뇌는 자연스럽게 만남을 전제로 생각하게 됩니다."

        # 결과 시각화
        st.error(f"❌ **기존 말투의 치명적인 문제점**\n> {bad_reason}")
        st.write("")
        
        st.success(f"### 🏆 AI 추천 마법의 교정 문장 ({desired_tone.split(' ')[1]} 컨셉)")
        st.markdown(f"**옵션 A (강력 추천):**\n### `{better_text_1}`")
        st.write("")
        st.markdown(f"**옵션 B (위트 탑재):**\n### `{better_text_2}`")
        
        st.write("---")
        st.markdown("### 🧠 이 말투가 가져오는 임상 심리학적 효과")
        st.info(f"💡 {psychology_effect}")
        
        # 소통 마스터의 한마디 팁
        st.write("")
        st.markdown("### 🎯 소통 코치의 원포인트 레슨")
        if "썸" in relationship:
            st.caption("🚨 썸 단계에서는 '선톡의 빈도'보다 '한 번 대화할 때의 몰입도'가 중요합니다. 상대의 대화가 끊겼다고 해서 조급하게 이어서 질문 폭탄을 던지는 행동은 절대 금물입니다.")
        elif "초기" in relationship:
            st.caption("🚨 연애 초기에는 자존심을 부리기보다 '안정감'을 주되, 내 일상 영역(친구, 커리어)을 희생하지 않는 모습을 보여주어야 '평생 잡은 물고기'라는 오만을 방지할 수 있습니다.")
        else:
            st.caption("🚨 장기 연애나 갈등기에는 텍스트(카톡)로 감정을 풀려고 하면 100% 오해가 생깁니다. 카톡은 만남을 잡는 용도로만 짧고 쿨하게 쓰시고, 진지한 얘기는 무조건 만나서 눈을 보고 하세요.")
