import json


def q3_memory(file_path: str):
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
    q3_memory('tweets.json')

    Note:
    The file specified by 'file_path' should contain one JSON object per line, each
    representing a tweet.
    The file is not a valid json file, as it is not an array with coma separated values.
    """

    users_count = {}
    with open(file_path,'r') as file:

        # El archivo json no tiene un formato válido, por lo que hay que leer linea a linea y formar un json válido
        for line in file:
                object = json.loads(line)

                if object.get('mentionedUsers'):
                    for mentioneduser in object['mentionedUsers']:
                        if mentioneduser['username'] in users_count:
                            users_count[mentioneduser['username']] += 1
                        else:
                            users_count[mentioneduser['username']] = 1
                
    top_10_mentioned_usernames = sorted(users_count.items(), key=lambda x: x[1], reverse=True)[:10]



    return top_10_mentioned_usernames