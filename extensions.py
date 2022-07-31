import json
import requests
from config import exchanges

class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена")

        try:
            quote_key = exchanges[quote.lower()]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена")

        if base_key == quote_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')
        
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        
        r = f"https://api.apilayer.com/fixer/convert?to={quote_key}&from={base_key}&amount={amount}"
        payload = {}
        headers = {
            "apikey": "ZL0ZzmY85164sXtwgJdISYnnT0Ak7gQc"
        }

        response = requests.get(r, headers=headers)
        new_value = response.json()
        new_value = new_value['result']
        new_value = round(new_value, 3)
        message =  f"Цена {amount} {base} в {quote} : {new_value}"
        return message
