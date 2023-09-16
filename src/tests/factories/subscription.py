from factory.fuzzy import FuzzyChoice

from db.enums import HoroscopeSigns, Sources
from db.models.subscription import Subscription
from tests.factories.base import BaseFactory


class SubscriptionFactory(BaseFactory):
    sign = FuzzyChoice(tuple(HoroscopeSigns))
    source = FuzzyChoice(tuple(Sources))

    class Meta:
        model = Subscription
