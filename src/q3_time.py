import json
import pandas as pd

def q3_time(file_path: str):
    """
    Process JSON data from a file containing tweet objects.

    Parameters:
    file_path (str): The path to a JSON file containing tweet objects.

    Returns:
    List[Tuple[str, int]]: A list of top 10 most mentioned users, with their respective count.

    This function reads JSON data from the specified file, processes the tweet objects,
    and returns the processed data as a list. Each tweet object should represent a tweet
    in JSON format.

    Example:
    q3_time('tweets.json')

    Note:
    The file specified by 'file_path' should contain one JSON object per line, each
    representing a tweet.
    The file is not a valid json file, as it is not an array with coma separated values.
    """

    json_data = []
    cols = ['mentionedUsername']

    with open(file_path,'r') as file:

        # El archivo json no tiene un formato válido, por lo que hay que leer linea a linea y formar un json válido
        for line in file:
                object = json.loads(line)

                if object.get('mentionedUsers'):
                    for mentioneduser in object['mentionedUsers']:
                        json_data.append(mentioneduser['username'])
                

    df = pd.DataFrame(json_data,columns=cols)

    top_10_mentioned_usernames = df.value_counts().head(10).reset_index()

    top_10_mentioned_usernames = [ tuple(values) for values in top_10_mentioned_usernames.values]


    return top_10_mentioned_usernames