# Inteli-CS - Intelligent Customer Service

🤖 **AI-powered delivery customer support chatbot using LangGraph and Streamlit**

## 🎯 프로젝트 개요

배달 플랫폼을 위한 지능형 고객 서비스 챗봇 시스템입니다. LangGraph를 활용한 다중 에이전트 아키텍처로 고객의 다양한 문의를 효율적으로 처리합니다.

## ✨ 주요 기능

### 🔍 **선제적 고객 분석**
- 고객 진입 시 자동으로 상황 분석
- 5가지 케이스별 맞춤형 인사말 제공
- 실시간 주문 상태 기반 문제 예측

### 🤖 **다중 에이전트 시스템**
- **CustomerAnalysisAgent**: 고객 상황 분석 및 선제적 대응
- **OrderAgent**: 주문 관련 문의 처리
- **GeneralAgent**: 일반 서비스 안내
- **ClaimAgent**: 배달 완료 후 클레임 처리
- **EscalationAgent**: 상담원 연결 및 복잡한 문의 처리

### 📊 **5가지 고객 상황 케이스**
1. **주문 전 고객** - 메뉴/이벤트 안내
2. **배차 지연** (≥10분) - 사과 + 라이더 확인 + 쿠폰 발급
3. **정상 대기** (<10분) - 안심 메시지
4. **배달 중** - 현황 안내
5. **배달 완료** - 만족도/문제 확인

## 🛠️ 기술 스택

- **AI Framework**: LangGraph, LangChain
- **LLM**: OpenAI GPT-4
- **UI**: Streamlit
- **Data Validation**: Pydantic
- **Language**: Python 3.10+

## 📁 프로젝트 구조

```
src/
├── agent_tools.py          # AI 에이전트 도구 함수들
├── api_tools.py            # 실제 API 호출 도구들
├── agent_prompts.py        # 에이전트별 프롬프트 템플릿
├── nodes.py               # LangGraph 노드 정의
├── states.py              # 상태 클래스 정의
├── main.py               # 메인 애플리케이션 로직
├── streamlit_wrapper.py   # Streamlit UI 래퍼
└── customer_dummy_data.py # 테스트 데이터
```

## 🚀 실행 방법

1. **의존성 설치**
```bash
pip install -r requirements.txt
```

2. **환경 변수 설정**
```bash
cp .env.example .env
# .env 파일에 OpenAI API 키 설정
```

3. **애플리케이션 실행**
```bash
streamlit run src/main.py
```

## 🎨 주요 특징

### 🧠 **지능형 상황 분석**
- 고객 데이터와 주문 정보를 실시간 분석
- 배차 대기 시간, 주문 상태 등을 종합 판단
- 문제 상황 사전 감지 및 선제적 대응

### 🎯 **개인화된 서비스**
- 고객명, 메뉴명을 활용한 맞춤 응답
- 고객 등급별 차별화된 서비스
- 과거 이력 기반 상황 예측

### 🔧 **확장 가능한 아키텍처**
- 모듈화된 에이전트 구조
- 새로운 에이전트 쉽게 추가 가능
- API 기반 외부 시스템 연동 지원

## 📝 라이선스

MIT License

## 👥 기여자

HackaThon25 Team - GoLas25 프로젝트