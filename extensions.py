import json
import requests
from config import keys
class ConverterException(Exception):
    pass

class Convertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        base = 'Rubel'
        quote = 'Dollar'

        if quote == base:
            raise ConverterException(f'Gleiche Währung wird nicht konvertiert!{base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConverterException(f'Konvertirung ist nicht möglich!{quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConverterException(f'Konvertirung ist nicht möglich!{base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConverterException(f'Der Betrag kann nicht bearbeiten werden! {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote_ticker]}&tsyms={keys[base_ticker]}')
        total_base=(json.loads(r.content)[quote_ticker][base_ticker])

        return total_base