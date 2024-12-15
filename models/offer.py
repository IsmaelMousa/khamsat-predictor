from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field


class CategoryName(str, Enum):
    """
    TODO
    """
    DESIGN = "تصميم"
    WRITING = "كتابة وترجمة"
    MARKETING = "تسويق رقمي"
    PROGRAMMING = "برمجة وتطوير"
    VIDEO = "فيديو وأنيميشن"
    ENGINEERING = "هندسة وعمارة"
    BUSINESS = "أعمال"
    AUDIO = "صوتيات"
    TRAINING = "تعليم عن بعد"
    DATA = "بيانات"
    STYLE = "أسلوب حياة"


class Duration(str, Enum):
    """
    TODO
    """
    DAY_1 = "يوم واحد"
    DAY_2 = "يومين"
    DAY_3 = "ثلاثة أيام"
    DAY_4 = "أربعة أيام"
    DAY_5 = "خمسة أيام"
    DAY_6 = "ستة أيام"
    WEEK_1 = "أسبوع"
    WEEK_2 = "أسبوعين"
    WEEK_3 = "ثلاثة أسابيع"
    MONTH = "شهر"


class OwnerLevel(str, Enum):
    """
    TODO
    """
    LEVEL_0 = "مستخدم جديد"
    LEVEL_1 = "مشتري جاد"
    LEVEL_2 = "مشتري جديد"
    LEVEL_3 = "بائع جديد"
    LEVEL_4 = "مشتري مميز"
    LEVEL_5 = "بائع نشيط"
    LEVEL_6 = "مشتري VIP"
    LEVEL_7 = "بائع موثوق"
    LEVEL_8 = "بائع مميز"

class Request(BaseModel):
    """
    TODO
    """
    category_name: CategoryName
    service_name: Annotated[str, Field(min_length=4)] = "أخرى"
    offer_stars: Annotated[float, Field(ge=0.0, le=5.0)]
    offer_raters: Annotated[int, Field(ge=0)]
    offer_response_time: Annotated[str, Field(min_length=5)] = "دقيقة"
    offer_buyers: Annotated[int, Field(ge=0)]
    pending: Annotated[int, Field(ge=0)]
    duration: Duration
    reviews: Annotated[int, Field(ge=0)]
    available_additions: Annotated[int, Field(ge=0)]
    additions_price: Annotated[float, Field(ge=0.0)]
    owner_verified: bool
    owner_level: OwnerLevel
    owner_stars: Annotated[float, Field(ge=0.0, le=5.0)]
    owner_raters: Annotated[int, Field(ge=0)]
    owner_completion_rate: Annotated[float, Field(ge=0.0, le=100.0)]
    owner_services: Annotated[int, Field(ge=0)]
    owner_customers: Annotated[int, Field(ge=0)]
    owner_response_time: Annotated[str, Field(min_length=5)] = "دقيقة"


class Response(BaseModel):
    """
    TODO
    """
    status: int
    message: str
