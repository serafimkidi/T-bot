import os

import datetime
from tinkoff.invest import Client, InstrumentStatus, InstrumentIdType, CandleInterval

import creds


if __name__ == '__main__':
    print("Hola\n")

    with Client(creds.Token) as client:
       # r = client.users.get_accounts().accounts

        # r = client.operations.get_operations(
        #     account_id=creds.Token,
        #     from_=datetime.datetime(2023,1,1),
        #     to=datetime.datetime.now()
        # )

        print (r)
