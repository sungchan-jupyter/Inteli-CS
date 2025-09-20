from typing_extensions import TypedDict, Annotated, Sequence, Optional
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


# 그래프 상태 정의
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    next_agent: Annotated[str, "Next agent to route to"]  # 다음으로 라우팅할 에이전트
    customer_id: str  # 고객 ID
    is_first_entry: Annotated[bool, "Is first entry"]  # 첫 입장인지 구분
    uploaded_image: Annotated[Optional[bytes], "Uploaded image data"]  # 업로드된 이미지
    enable_image_upload: Annotated[
        bool, "Enable image upload button"
    ]  # 이미지 업로드 버튼 활성화
    enable_support_button: Annotated[
        bool, "Enable support connection button"
    ]  # 상담원 연결 버튼 활성화