import abc

from db.enums import HoroscopeSigns


class BaseSource(abc.ABC):
    @classmethod
    def get_today_by_sign(cls, sign: HoroscopeSigns, *args, **kwargs) -> str:
        return f"you are the best, dear {sign}"
