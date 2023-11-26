import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        headers={"X-Api-Key":api_key}
        url=self.get_url()+"Finance/CryptoAddress/Types"
        response=requests.get(url,headers=headers)
        return response.json()

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        params={
            "cryptoType":crypto_type
        }
        headers={
            "X-Api-Key":api_key
        }
        url=self.get_url()+"Finance/CryptoAddress"
        resp=requests.get(url,params=params,headers=headers)

        return resp.json()

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        headers={
            "X-Api-Key":api_key
        }
        url=self.get_url()+"Finance/Countries"
        resp=requests.get(url,headers=headers)

        return resp.json()

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        headers={
            "X-Api-Key":api_key
        }
        params={
            "countryCode":country_code
        }

        url=self.get_url()+f"Finance/Iban/{country_code}"
        resp=requests.get(url,headers=headers,params=params)

        return resp.json()
token="cada6da7cd4e41238712196daafaa11e"
v=Finance()
print(v.get_iban_by_country_code(country_code="AL",api_key=token))