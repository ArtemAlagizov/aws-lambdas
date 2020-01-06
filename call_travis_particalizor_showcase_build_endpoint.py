import requests


def lambda_handler(event, context):
    travis_api_url = event['travis_api_url']
    github_branch_name = event['github_branch_name']
    token = event['token']
    travis_api_version = event['travis_api_version']

    response = requests.post(travis_api_url, data={'request': {'branch': github_branch_name}},
                             headers={'Authorization': token, 'Travis-API-Version': travis_api_version})

    print(response.status_code, response.reason)
