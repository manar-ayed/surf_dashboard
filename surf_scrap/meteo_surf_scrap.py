import requests
from bs4 import BeautifulSoup
import pandas as pd
def extract_meteo_surf(url) :
    
    """
    This function takes a  url an user_agent, scrapes surf forecast data from a given url page and stores 
    data points in a csv_file
    
    - output : pandas dataframe contaning the data extracted
    """
    
    #headers = {'User-Agent': user_agent}
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Initialize empty lists to hold the data needed :
    dates = []
    hours = []
    vagues = []
    wind_speeds = []
    wind_directions = []

    # Looping through each forecast-tab block (each block represents one day)
    forecast_tabs = soup.find_all('div', class_='forecast-tab')
    for tab in forecast_tabs:
        # Extracting the date for this tab
        date_div = tab.find('div', class_='title')
        forecast_date = date_div.find('b').text.strip() if date_div else 'N/A'

        # Extracting the hours, waves, wind speeds, and wind directions for this date
        time_divs = tab.find_all('div', class_='cell date with-border')
        for time_div in time_divs:
            hour = time_div.text.strip()
            hours.append(hour)
            dates.append(forecast_date)  # Repeat the date for each hour

        # Extracting waves (vagues)
        for wave_div in tab.find_all('div', class_='cell large waves with-border'):
            vague = wave_div.text.strip()
            vagues.append(vague)

        # Extracting wind speeds
        for wind_div in tab.select('div[class^="wind wind-color-"]'):
            wind_speed = wind_div.find('span').text.strip()
            wind_speeds.append(wind_speed)

        # Extracting wind directions
        for wind_dir_div in tab.find_all('div', class_='wind img'):
            wind_direction = wind_dir_div.find('img')['alt'] if wind_dir_div else 'N/A'
            wind_directions.append(wind_direction)

    # Creating a DataFrame with the extracted data
    df = pd.DataFrame({
        'Date': dates,
        'Hour': hours,
        'Vagues': vagues,
        'Wind Speed (km/h)': wind_speeds,
        'Wind Direction': wind_directions
    })

    df.to_csv('output.csv', index=False)
    print(df.head())
    return df