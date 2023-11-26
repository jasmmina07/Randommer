import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        headers={"X-Api-Key":api_key}
        url=self.get_url()+"Misc/Cultures"
        response=requests.get(url,headers=headers)
        return response.json()
        
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        headers={
            "X-Api-Key":api_key
        }
        params={
            "number":number,
            "culture":culture
        }

        url=self.get_url()+"Misc/Random-Address"
        resp=requests.get(url,headers=headers,params=params)

        return resp.json()

token="cada6da7cd4e41238712196daafaa11e"
v=Misc()
print(v.get_random_address(api_key=token,number=1))
