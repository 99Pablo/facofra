import json
import pandas as pd
import emoji

def q2_time(file_path: str):
    """
    Process JSON data from a file containing tweet objects.

    Parameters:
    file_path (str): The path to a JSON file containing tweet objects.

    Returns:
    List[Tuple[str, int]]: A list of top 10 most used emojis, with their respective count.

    This function reads JSON data from the specified file, processes the tweet objects,
    and returns the processed data as a list. Each tweet object should represent a tweet
    in JSON format.

    Example:
    q2_time('tweets.json')

    Note:
    The file specified by 'file_path' should contain one JSON object per line, each
    representing a tweet.
    The file is not a valid json file, as it is not an array with coma separated values.
    """
    json_data = []
    cols = ['emojis']

    with open(file_path,'r') as file:

        # El archivo json no tiene un formato válido, por lo que hay que leer linea a linea y formar un json válido
        for line in file:
            object = json.loads(line)
            data = object['content']
            
            found_emojis = emoji.emoji_list(data)

            for emoji_object in found_emojis:
                json_data.append([emoji_object['emoji']])

    df = pd.DataFrame(json_data,columns=cols)

                

    top_10_emojis = df.value_counts().reset_index().head(10).values
    top_10_emojis = [tuple(top_emoji) for top_emoji in top_10_emojis]

    return top_10_emojis