import requests

user_name = input("\n Please provide github username whose public repo you would like to see\n")

url_part1 = 'https://api.github.com/search/repositories?q=user:'
url = url_part1 + user_name
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
try:
    r.raise_for_status()
    #Store API response in a variable. API returns information in JSON format
    response_dict = r.json()
    print(f"\n\n\nTotal repositories: {response_dict['total_count']}")

    #Exploring information stored in 'items' keys regarding repositories
    repo_dicts = response_dict['items']

    #Examine teh first repositories
    print("\nPlease see below the names of each repository accessible by:" , user_name)
    for repo_dict in repo_dicts:
        print(f"{repo_dict['name']}")
except requests.exceptions.HTTPError as e:
    print ("\nError: " + str(e))
