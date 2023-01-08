import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
           'accept': 'application/json',
           }

s = requests.Session()
s.headers.update(headers)


class MSoneAPI:

    def __init__(self):
        print("init")

    @classmethod
    def get_results(cls, query):
        try:
            query = query.replace("/", "|")
        except:
            pass
        print(query)
        response = s.get(f'https://msoneapi.up.railway.app/{query}', headers=headers)
        results = response.json()
        return results

    @classmethod
    def get_synopsis(cls, query):
        response = s.get(f'https://msoneapi.up.railway.app/synopi/{query}', headers=headers)
        results = response.json()
        return results
