import pathlib

import pytest_asyncio

from tests.factories.user import UserFactory

_CURRENT_PATH = pathlib.Path(__file__).resolve()
_EXAMPLES_PATH = _CURRENT_PATH.parent.joinpath("examples")


# @pytest.fixture(scope="session")
@pytest_asyncio.fixture(scope="session")
async def horo_mail_today_page() -> str:
    path = _EXAMPLES_PATH.joinpath("mail_horo_today_example.html")

    with open(path, "r") as file:
        return file.read()


@pytest_asyncio.fixture(scope="session")
async def thousand_and_one_today_page() -> str:
    path = _EXAMPLES_PATH.joinpath("1001horo_today_example.html")

    with open(path, "r", encoding="windows-1251") as file:
        return file.read()


@pytest_asyncio.fixture(scope="session")
async def horo_mail_today() -> str:
    return (
        "День будет насыщенным и едва ли обойдется без неожиданностей. "
        "Но даже если абсолютно все пойдет не по плану, "
        "вы сохраните спокойствие, не пойдете на поводу у эмоций и примете верные решения. "
        "Возможны напряженные моменты в общении с окружающими, небольшие разногласия. "
        "Но и тут нет причин для тревоги, ведь вы быстро найдете способ сгладить острые углы. "
        "Хорошо сложатся поездки. Даже если они займут немало времени, вы не устанете, "
        "получите массу ярких впечатлений. Вдали от дома возможны встречи, которые запомнятся вам надолго."
    )


@pytest_asyncio.fixture(scope="session")
async def thousand_and_one_today() -> str:
    return (
        "Сегодня в голову Овна придут интересные идеи, которые могут благоприятно сказаться как на его карьере,"
        " так и на жизни вообще. А может быть, вместо полезной идеи завяжется некое не менее полезное знакомство. "
        "Романтичным оно будет едва ли, а вот в материальном смысле окажется перспективным. "
        "В любом случае, сегодня Овну очень не помешает держать нос по ветру – может запахнуть деньгами!"
    )


@pytest_asyncio.fixture(scope="session")
async def base_user(async_db_session):
    return await UserFactory.create(session=async_db_session)
