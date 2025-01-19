# run_extraction.py

import argparse
from surf_scrap.meteo_surf_scrap import extract_meteo_surf

 
def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Extract surf forecast data from a given URL.')

    # Add the URL argument
    parser.add_argument('--input_url', type=str, help='The URL of the surf forecast page to scrape.')

    # Parse the arguments
    args = vars(parser.parse_args())
    extract_meteo_surf(url=args["input_url"])
    
    # Display a message indicating successful completion
    print("Data extracted and saved to output.csv")
    #print(df.head())  # Optionally print the first few rows of the DataFrame

if __name__ == "__main__":
    # Call the main function with the provided URL
    main()

