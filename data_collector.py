
import requests
# from datetime import datetime, timedelta
# import os
# import json
import pandas as pd

# To set your environment variables in your terminal run the following line:


# Set the Bearer Token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAN%2FhlQEAAAAAA3KWaOM4ynnWjSNqd%2BH4ncV6mvU%3DRG5HSsW7lgy9kJakzkn67aBPzmfnAHCELtudRJisaeeNUHlkojj"
# headers = {"Authorization": f"Bearer {bearer_token}"}
# 

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
# query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}
# query_params = {'query': '(from:business -is:retweet) OR #business','tweet.fields': 'author_id'}
query_params = {'query': '(from:OttawaPolice -is:retweet) OR #OttawaPolice','tweet.fields': 'author_id'}

#lavienrosye michaeljburry

# query_params = {"query": "from:OttawaPolice", "max_results": 100, "tweet.fields": "public_metrics",  
                # "start_time":'2023-01-01T00:00:00.000Z', "end_time":'2023-02-02T12:00:00.000Z'}

# query_params = {"query": "from:OttawaPolice", "max_results": 100, "tweet.fields": "public_metrics"}
query_params = {"query": "from:business", "max_results": 100, "tweet.fields": "public_metrics"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    
    tweets_df = pd.DataFrame(json_response['data'])
    print(tweets_df[0:1])
    print(tweets_df[0:100]['text'])
    
    tweets_df.to_csv("tweets.csv", index=False)
    # tweets_df.info()
    # print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
    
    
