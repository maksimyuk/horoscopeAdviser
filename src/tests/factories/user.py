import factory

from db.models.user import User
from tests.factories.base import BaseFactory


class UserFactory(BaseFactory):
    telegram_user_id = factory.Sequence(lambda n: n)

    class Meta:
        model = User
