from google_search import *
import time

def main():

    search_term_input = input("Enter excel file path: ")

    df = pd.read_excel(search_term_input)

    search_term_list = df["search term"].tolist()

    for search_term in search_term_list:

        print("search : " + str(search_term))

        #Please customize this according to your needs
        regex_string = search_term.split("+")[1]

        print("regex filter pattern : " + str(regex_string))

        # Define output filename
        output_filename = str(search_term) + ".xlsx"

        #Go to Google Search Module
        google_search(search_term, output_filename, regex_string)

        time.sleep(5)

if __name__ == "__main__":
    main()








