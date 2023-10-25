import json
import emoji

def q2_memory(file_path: str):
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
    q2_memory('tweets.json')

    Note:
    The file specified by 'file_path' should contain one JSON object per line, each
    representing a tweet.
    The file is not a valid json file, as it is not an array with coma separated values.
    """

    emojis_count = {}
    with open(file_path,'r') as file:

        # El archivo json no tiene un formato válido, por lo que hay que leer linea a linea y formar un json válido
        for line in file:
            object = json.loads(line)
            data = object['content']
            
            found_emojis = emoji.emoji_list(data)

            for emoji_object in found_emojis:
                if emoji_object['emoji'] in emojis_count:
                    emojis_count[emoji_object['emoji']] += 1
                else:
                    emojis_count[emoji_object['emoji']] = 1

                

    top_10_emojis = sorted(emojis_count.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_10_emojis