from aiogram.dispatcher.filters.state import State, StatesGroup


class AddSubscriptionStates(StatesGroup):
    """States for adding subscription"""

    waiting_for_sign = State()
    waiting_for_source = State()
    waiting_for_period = State()
    # waiting_for_approve = State()
