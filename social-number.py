import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        headers={
            "X-Api-Key":api_key
        }

        url=self.get_url()+"SocialNumber"
        response=requests.get(url,headers=headers)
        return response.json()

token="cada6da7cd4e41238712196daafaa11e"
v=SocialNumber()
print(v.get_SocialNumber(api_key=token))