import requests

def lambda_handler(event, context):
    skyscanner_clone_backend_url = event['skyscanner_clone_backend_url']
    number_of_flights = event['number_of_flights']

    response = requests.post(skyscanner_clone_backend_url, data={'numberOfFlights': number_of_flights})

    print(response.status_code, response.reason)