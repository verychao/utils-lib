from datetime import datetime, date


def format_date(dt: datetime, fmt: str = "%Y-%m-%d") -> str:
    """将 datetime 对象格式化为字符串，fmt 缺省值为 ISO 日期格式"""
    return dt.strftime(fmt)


def days_between(start: date, end: date) -> int:
    """返回两个日期之间的自然天数差（end - start 的绝对值）"""
    return abs((end - start).days)


def is_weekday(dt: date) -> bool:
    """判断给定日期是否为工作日（周一到周五返回 True，周六日返回 False）"""
    return dt.weekday() < 5
