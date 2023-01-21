from json import dumps
import requests
import json
import os

# Load the contents of the .env file into the environment
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
BOOTSTRAP_SERVER = os.environ.get("BOOTSTRAP_SERVER")

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    print(response.json())
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):
    # You can adjust the rules if needed
    sample_rules = [
        {"value": "#australianopen2023"},
        {"value": "#australianopen"},
        {"value": "#AusOpen"}
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            # Send a message to the Kafka topic
            print(json.dumps({json_response['data']['id']: json_response['data']['text']}))


def broadcast_tweets():
    rules = get_rules()
    print(rules)
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    get_stream(set)


if __name__ == "__main__":
    broadcast_tweets()
   