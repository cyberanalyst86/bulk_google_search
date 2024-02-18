from googleapiclient.discovery import build
from google_console_search import *
import yaml
from yaml import SafeLoader

def get_api_key():

    with open(
            "google_search_api_key.yaml") as f:
        conf = yaml.load(f, Loader=SafeLoader)

    api_key1 = conf['google_api']['api_key1']
    api_id1 = conf['google_api']['api_id1']
    api_key2 = conf['google_api']['api_key2']
    api_id2 = conf['google_api']['api_id2']
    api_key3 = conf['google_api']['api_key3']
    api_id3 = conf['google_api']['api_id3']
    api_key4= conf['google_api']['api_key4']
    api_id4 = conf['google_api']['api_id4']

    return api_key1, api_id1, api_key2, api_id2, api_key3, api_id3, api_key4, api_id4

def google_search(search_term, output_filename, regex_string):

    #-----------------------------------Definition-----------------------------------#

    NUM_RESULTS = 100
    MY_SEARCH = search_term

    # -----------------------------------API Key and Search ID Throttle-----------------------------------#
    # -----------------------------------Remove the code necessarily if you only have 1 set of api key-----------------------------------#

    api_key1, api_id1, api_key2, api_id2, api_key3, api_id3, api_key4, api_id4 = get_api_key()

    MY_API_KEY = api_key1
    MY_CSE_ID = api_id1

    MY_API_KEY2 = api_key2
    MY_CSE_ID2 = api_id2

    MY_API_KEY3 = api_key3
    MY_CSE_ID3 = api_id3

    MY_API_KEY4 = api_key4
    MY_CSE_ID4 = api_id4

    # -----------------------------------Start Search-----------------------------------#
    print("google search " + str(MY_SEARCH))

    try:
    #-----------------------------------Searching Google-----------------------------------#
        results = google_console_search(MY_SEARCH, MY_API_KEY, MY_CSE_ID, num=NUM_RESULTS)

        #-----------------------------------Getting Google Result-----------------------------------#


        get_google_result(results, output_filename, regex_string)

    except Exception as e:

        print("exception #1")

        try:

            results = google_console_search(MY_SEARCH, MY_API_KEY2, MY_CSE_ID2, num=NUM_RESULTS)

            get_google_result(results, output_filename, regex_string )

        except Exception as e:

            print("exception #2")

            try:

                results = google_console_search(MY_SEARCH, MY_API_KEY3, MY_CSE_ID3, num=NUM_RESULTS)

                get_google_result(results, output_filename, regex_string)

            except Exception as e:

                print("exception #3")

                try:

                    results = google_console_search(MY_SEARCH, MY_API_KEY4, MY_CSE_ID4, num=NUM_RESULTS)

                    get_google_result(results, output_filename, regex_string)

                except Exception as e:

                    print(str(MY_SEARCH) + " error in google search")

    return
