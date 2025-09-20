import requests
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List
from langchain.tools import tool


class CustomerResponse(BaseModel):
    cust_no: str = Field(..., description="고객 번호")
    cust_id: str = Field(..., description="고객 이메일 ID")
    cust_nm: str = Field(..., description="고객명")
    join_dttm: datetime = Field(..., description="가입일시")
    first_ord_dttm: Optional[datetime] = Field(None, description="첫 주문일시")
    grade_cd: str = Field(
        ..., description="고객 등급 코드 (S: 특급, A: 우수, B: 일반, C: 기본)"
    )
    cs_flag: str = Field(
        ..., description="고객 상태 플래그 (H: 높음, M: 중간, L: 낮음)"
    )


class MenuItem(BaseModel):
    food_nm: str = Field(..., description="음식명")
    food_price: int = Field(..., description="음식 단가")
    food_quantity: int = Field(..., description="음식 수량")
    food_amt: int = Field(..., description="음식 총액")


class OrderResponse(BaseModel):
    ord_no: str = Field(..., description="주문 번호")
    cust_no: str = Field(..., description="고객 번호")
    latest_dlvry_fee: int = Field(..., description="최신 배달비")
    gap_dlvry_fee: int = Field(..., description="배달비 차액")
    ord_amt: int = Field(..., description="주문 금액")
    expect_dlvry_fee: int = Field(..., description="예상 배달비")
    auto_cancel_avail_yn: bool = Field(..., description="자동 취소 가능 여부")
    auto_defense_avail_yn: bool = Field(..., description="자동 방어 가능 여부")
    ord_dttm: datetime = Field(..., description="주문일시")
    cancel_dttm: Optional[datetime] = Field(None, description="취소일시")
    expect_cook_cmplt_dttm: Optional[datetime] = Field(
        None, description="예상 조리완료일시"
    )
    cust_noti_dttm: Optional[datetime] = Field(None, description="고객 알림일시")
    dispatch_start_dttm: Optional[datetime] = Field(None, description="배차 시작일시")
    dispatch_cmplt_dttm: Optional[datetime] = Field(None, description="배차 완료일시")
    dispatch_wait_mncnt: Optional[int] = Field(None, description="배차 대기 분")
    cook_cmplt_dttm: Optional[datetime] = Field(None, description="조리 완료일시")
    food_wait_mncnt: Optional[int] = Field(None, description="음식 대기 분")
    arrived_shop_dttm: Optional[datetime] = Field(None, description="매장 도착일시")
    pickup_dttm: Optional[datetime] = Field(None, description="픽업일시")
    handover_dttm: Optional[datetime] = Field(None, description="전달일시")
    delay_mncnt: Optional[int] = Field(None, description="지연 분")
    status: str = Field(..., description="주문 상태")
    shop_nm: str = Field(..., description="매장명")
    shop_cate_nm: str = Field(..., description="매장 카테고리명")
    shop_addrs: str = Field(..., description="매장 주소")
    shop_phone_no: str = Field(..., description="매장 전화번호")
    handover_addrs: str = Field(..., description="배달 주소")
    handover_phone_no: str = Field(..., description="배달 전화번호")
    menu_items: List[MenuItem] = Field(..., description="주문 메뉴 목록")


class IssuedCouponResponse(BaseModel):
    issued_coupon_id: int = Field(..., description="발급된 쿠폰 ID")
    coupon_no: str = Field(..., description="쿠폰 번호")
    coupon_nm: str = Field(..., description="쿠폰명")
    cust_no: str = Field(..., description="고객 번호")
    coupon_type_cd: str = Field(..., description="쿠폰 유형 코드")
    issuance_type_cd: str = Field(..., description="발급 유형 코드")
    coupon_amt: Optional[int] = Field(None, description="쿠폰 금액")
    discount_limit_amt: Optional[int] = Field(None, description="할인 한도 금액")
    min_ord_amt: Optional[int] = Field(None, description="최소 주문 금액")
    issued_dttm: datetime = Field(..., description="발급일시")


@tool
def get_customer_info(cust_no: str) -> str:
    """고객 정보를 조회합니다.

    Args:
        cust_no: 조회할 고객 번호

    Returns:
        고객 정보 JSON 문자열
    """
    url = f"http://localhost:8080/api/customers/{cust_no}"

    response = requests.get(url)
    response.raise_for_status()

    customer = CustomerResponse(**response.json())
    return customer.model_dump_json()


@tool
def get_today_orders(cust_no: str) -> str:
    """고객의 오늘 주문 정보를 조회합니다.

    Args:
        cust_no: 조회할 고객 번호

    Returns:
        오늘 주문 목록 JSON 문자열
    """
    url = f"http://localhost:8080/api/orders/customers/{cust_no}/today"

    response = requests.get(url)
    response.raise_for_status()

    orders = [OrderResponse(**order) for order in response.json()]
    return str([order.model_dump() for order in orders])


@tool
def issue_coupon(cust_no: str) -> str:
    """고객에게 쿠폰을 발급합니다.

    Args:
        cust_no: 쿠폰을 발급할 고객 번호

    Returns:
        발급된 쿠폰 정보 JSON 문자열
    """
    url = f"http://localhost:8080/api/customers/{cust_no}/coupons"
    params = {"couponNo": "CPN001", "issuanceTypeCd": "AUTO"}

    response = requests.post(url, params=params)
    response.raise_for_status()

    coupon = IssuedCouponResponse(**response.json())
    return coupon.model_dump_json()