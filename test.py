import pull_db
from pull_db import search_from_categ
import functions
import requests as r
import datetime
import json
from pathlib import Path

# result = r.get(f'{pull_db.BASE_URL}filter.php?c=Other%20/%20Unknown').json()       
# result = r.get(f'{pull_db.BASE_URL}list.php?c=list').json()
# result = pull_db.search_from_categ('Other%20/%20Unknown')
# print(result)

# Path('logging').mkdir(exist_ok=True)


# def loggin_errors(e, location):

#     dic = {
#     'date':datetime.datetime.now().strftime('%Y_%m_%d-%H:%M:%S'),
#     'type_of_error':type(e).__name__,
#     'message': str(e),
#     'location':location
# }

#     with open(f'logging/logs_at_{datetime.datetime.now().strftime("%Y-%m-%d")}.jsonl', 'w', encoding='utf-8') as f:
#         json.dump(dic, f, ensure_ascii=False, indent=4)

# loggin_errors(33, 'burda')        

# st = "ade / made"

# print(st.replace('/',''))


# def search_from_categ(cate: str):

#     '''Search drinks via category take str give dict
#     Result like {}'name':'name_of_drink'
#                  'id':'id_of_drink'
#                  'image':'link_of_image'}'''

#     try:
#         result = r.get(f'{pull_db.BASE_URL}filter.php?c={cate}').json()

#         cate_drinks = list()

#         for i in result['drinks']:
#             cate_drinks.append({
#                 'name':i['strDrink'],
#                 'id':i['idDrink'],
#                 'image':i['strDrinkThumb']})

#         return cate_drinks

#     except Exception as e:
#         functions.logging_errors(e, 'pull_dsb/search_from_cate')
        


# print(search_from_categ('Tea Coffe'))        

# print(functions.result_from_ingridient_info('l'))

result = pull_db.search_drinks_vie_ingr('gin')

with open('test_drinks_via_ingr.jsonl', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

    