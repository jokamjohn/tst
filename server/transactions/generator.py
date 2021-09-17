from typing import List, Optional
import datetime
import itertools

from faker import Faker
from faker.providers import BaseProvider, company
from pydantic import BaseModel

# You shouldn't need to change the following code
DEFAULT_SEED = 1234
DEFAULT_LOCALE = "en_US"


class Transaction(BaseModel):
    transaction_id: str
    user_id: str
    account_id: str
    amount: float
    date: datetime.date
    iso_currency_code: str
    merchant_name: Optional[str]
    pending: bool


class TransactionIdProvider(BaseProvider):
    def transaction_id(self):
        return f"tx_{self.random_number(digits=6):06}"


class UserAndAccountProvider(BaseProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_ids = self._init_user_ids()
        self.account_ids_dict = {
            user_id: self._init_account_ids() for user_id in self.user_ids
        }

    def _init_user_ids(self, n_max_users=100):
        return [f"user_{self.random_number(digits=3):03}" for _ in range(n_max_users)]

    def _init_account_ids(self, n_max_accounts=10):
        return [
            f"account_{self.random_number(digits=5):05}" for _ in range(n_max_accounts)
        ]

    def user_and_account(self):
        user_id = self.random_element(self.user_ids)
        account_id = self.random_element(self.account_ids_dict[user_id])
        return user_id, account_id


def generate_random_transaction(
        seed: int = DEFAULT_SEED, locale: str = DEFAULT_LOCALE
) -> Transaction:
    while True:
        # Faker.seed(seed)
        fake = Faker(locale)
        fake.add_provider(TransactionIdProvider)
        fake.add_provider(UserAndAccountProvider)
        fake.add_provider(company.Provider)

        user_id, account_id = fake.user_and_account()

        tx = Transaction(
            transaction_id=fake.unique.transaction_id(),
            user_id=user_id,
            account_id=account_id,
            amount=round(fake.random.uniform(0.0, 1000.0), 2),
            date=fake.date_time_between_dates(
                datetime.date(2000, 1, 1), datetime.date(2020, 12, 1)
            ),
            iso_currency_code="USD",
            merchant_name=fake.company(),
            pending=False,
        )
        yield tx


def generate_transactions_for_api(count: int) -> List[Transaction]:
    generator = generate_random_transaction()
    transactions = list(itertools.islice(generator, count))
    return transactions
