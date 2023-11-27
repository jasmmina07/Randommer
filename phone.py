import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        headers={
            "X-Api-Key":api_key
        }

        params={
            "CountryCode":CountryCode,
            "Quantity":Quantity
        }
        url=self.get_url()+"Phone/Generate"
        response=requests.get(url,headers=headers,params=params)
        return response.json()
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        headers={
            "X-Api-Key":api_key
        }

        params={
            "Quantity":Quantity
        }
        url=self.get_url()+"Phone/IMEI"
        response=requests.get(url,headers=headers,params=params)
        return response.json()
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        headers={
            "X-Api-Key":api_key
        }

        params={
            "telephone":telephone,
            "CountryCode":CountryCode,
        }
        url=self.get_url()+"Phone/Validate"
        response=requests.get(url,headers=headers,params=params)
        return response.json()
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        headers={
            "X-Api-Key":api_key
        }

        url=self.get_url()+"Phone/Countries"
        response=requests.get(url,headers=headers)
        return response.json()

token="cada6da7cd4e41238712196daafaa11e"
v=Phone()
print(v.is_valid(api_key=token,telephone="123456",CountryCode='Uz'))