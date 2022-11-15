from get_search_list import search_list
import re
from mktrans_dict import dict_ascii

trans_table = str.maketrans(dict_ascii)

trans_input = input().title().translate(trans_table)

pattern = re.compile(trans_input)

search_str = ' '.join(search_list)

result = pattern.findall(search_str)[0]

print(trans_input)

print(result)





