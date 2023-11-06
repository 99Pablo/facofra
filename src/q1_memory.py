import json
from datetime import datetime
from memory_profiler import profile

@profile
def q1_memory(file_path: str):
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
    q1_memory('tweets.json')

    Note:
    The file specified by 'file_path' should contain one JSON object per line, each
    representing a tweet.
    The file is not a valid json file, as it is not an array with coma separated values.
    """
    
    dates_users_count = {}

    with open(file_path,'r') as file:

        # El archivo json no tiene un formato válido, por lo que hay que leer linea a linea y formar un json válido
        for line in file:
            object = json.loads(line)
            date = object['date'][:10]
            username = object['user']['username']

            # Armo un dictionary con cada fecha, count por cada vez que aparece, y los usuarios con su count cada vez que se repitan dentro de esa fecha.
            if date in dates_users_count:
                if username in dates_users_count[date]['users']:
                    dates_users_count[date]['users'][username] += 1
                else:
                    dates_users_count[date]['users'][username] = 1
                dates_users_count[date]['count'] +=1
            else:
                dates_users_count[date] = {'count':1, 'users' : {username:1}}


    # Obtengo el top 10 de fechas con mayor count
    top_10_dates = []
    for date_key in dates_users_count:

        if top_10_dates:

            # Comparo el count de la fecha seleccionada, con los count de las fechas ya existentes en el top 10
            for index, top_10_date_object in enumerate(top_10_dates):
                
                if (dates_users_count[date_key]['count']) > (top_10_date_object['date_count']):
                    top_10_dates.insert(index,{'date':date_key,'date_count':dates_users_count[date_key]['count'],'users':dates_users_count[date_key]['users']})
                    
                    if len(top_10_dates) > 10:  # Si con el elemento insertado supero las 10 fechas, elimino la última ya que no formará parte del top 10
                        top_10_dates.pop(-1)
                    break

            else:   # si el count no era superior a alguna del top 10, pero todavía queda lugar en el top 10, la inserto al final
                if len(top_10_dates) < 10:
                    top_10_dates.append({'date':date_key,'date_count':dates_users_count[date_key]['count'],'users':dates_users_count[date_key]['users']})
                    
                    
        else:   # La primera fecha encontrada se inserta en el top 10
            top_10_dates.append({'date':date_key,'date_count':dates_users_count[date_key]['count'],'users':dates_users_count[date_key]['users']})

    
    # Formo resultado, mayor fecha con su mayor usuario
    top_10_dates_and_user = []
    for date_object in top_10_dates:
        
        max_user = max(date_object['users'].items(), key=lambda item: item[1])[0]
        top_10_dates_and_user.append((datetime.strptime(date_object['date'],'%Y-%m-%d').date(),max_user))

    return top_10_dates_and_user