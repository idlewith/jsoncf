import json
import sys

import pyperclip


def prettify():
    """prettify json string from clipboard.

    1. get data from clipboard

    2. dump data to local data.json

    3. dumps to local terminal
    """
    json_file = 'data.json'

    args = sys.argv
    if len(args) > 1:
        content_list = args[1:]
        content = " ".join(content_list)
    else:
        content = pyperclip.paste()

    content_eval = eval(content)
    json.dump(content_eval, open(json_file, 'w', encoding='utf-8'), indent=True)

    text = json.dumps(content_eval, indent=True)
    return text


if __name__ == "__main__":
    prettify()