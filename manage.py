import pandas as pd
import requests
import json

#Definitions
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

#------------------------------------------------------------------------------------------------------------
#Extract data
def get_accounts():
    r_ids = requests.get(f'{sdw2023_api_url}/users')
    return r_ids.json() if r_ids.status_code == 200 else print('Não foi possivel acessar a API')

#------------------------------------------------------------------------------------------------------------
#Transform data
def transform_data(accounts):
    for data in accounts:
        if "news" in data and "features" in data:
            del data["news"]
            del data["features"]
    return accounts

#------------------------------------------------------------------------------------------------------------
#Load data
def update_users(user):
  users = []
  for id in filter:
        users.append(id['id'])
  response = requests.put(f"{sdw2023_api_url}/users/{users}", json=user)
  return True if response.status_code == 200 else False

def main():
    account_list = get_accounts()
    filter = transform_data(account_list)
    update_users(filter)
    df = pd.json_normalize(filter).to_excel('testado.xlsx')


if __name__ == '__main__':
    main()