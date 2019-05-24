import re

def get_key(personal_url):
    """
    お寺・神社のURLを受け取り、一意のキー(URL末尾の数字)を作成し返す関数
    :global None:
    :param personal_url:
    :return unique_key.group(1):
    """
    unique_key = re.search(r'/(\d+)',personal_url)
    return unique_key.group(1)


# personal_url = "https://omairi.club/spots/77916"
#
# print(get_key(personal_url))