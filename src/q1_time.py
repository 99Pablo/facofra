import json
import pandas as pd
from memory_profiler import profile

@profile
def q1_time(file_path: str):
    """
    Process JSON data from a file containing tweet objects.

    Parameters:
    file_path (str): The path to a JSON file containing tweet objects.

    Returns:
    List[Tuple[datetime.date, str]]: A list of top 10 most tweeted dates, with their respective top user, inside a tuple.

    This function reads JSON data from the specified file, processes the tweet objects,
    and returns the processed data as a list. Each tweet object should represent a tweet
    in JSON format.

    Example:
    q1_time('tweets.json')

    Note:
    The file specified by 'file_path' should contain one JSON object per line, each
    representing a tweet.
    The file is not a valid json file, as it is not an array with coma separated values.
    """
    json_data = []
    cols = ['date','username']

    with open(file_path,'r') as file:

        # El archivo json no tiene un formato válido, por lo que hay que leer linea a linea y formar un json válido
        for line in file:
            object = json.loads(line)
            data = [object['date'],object['user']['username']]
            json_data.append(data)
                

    df = pd.DataFrame(json_data,columns=cols)
    df['date'] = pd.to_datetime(df['date']).dt.date     # transformo campo fecha en formato YYYY-mm-dd

    top_10_dates = df['date'].value_counts().head(10).index     # Obtengo las 10 fechas más repetidas
    
    df['count_date'] = df.groupby('date')['date'].transform('count')    # A cada fecha le agrego un campo count, por la cantidad de veces que aparece

    # Genero un dataframe con top 10 fechas, junto a los usuarios que más aparecen en dichas fechas
    top_10_dates_and_user = df[df['date'].isin(top_10_dates)] \
        .groupby(['date','count_date','username'],as_index=False) \
        .size() \
        .sort_values(['count_date','size'],ascending=False) \
        .drop_duplicates(subset='date', keep='first')
    
    top_10_dates_and_user = [(row[0],row[2]) for row in top_10_dates_and_user.to_records(index=False)]

    return top_10_dates_and_user