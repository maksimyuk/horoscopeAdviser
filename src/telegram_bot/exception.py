class GeneralException(Exception):
    """Base exception"""


class LogicException(GeneralException):
    """Exception in business-logic ready for user notification"""
