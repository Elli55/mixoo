import requests as r
import json
import functions
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = f'https://www.thecocktaildb.com/api/json/v1/{os.getenv('api')}/'


def search_coctail_from_name(name: str):

    '''search coctail from name, take str give json
    Result like json variable , full data '''
    
    try:
        result = r.get(f'{BASE_URL}search.php?s={name}').json()
        return result
    except Exception as e:
        functions.logging_errors(e, 'pull_db/search_cocktail_from_name')

def search_drinks_from_id(id: str):

    try:
        result = r.get(f'{BASE_URL}lookup.php?i={id}').json()
        return result
    except Exception as e:
        functions.logging_errors(e, 'pull_db/search_drinks_from_id')

def search_from_categ(cate: str):

    '''Search drinks via category take str give dict
    Result like {}'name':'name_of_drink'
                 'id':'id_of_drink'
                 'image':'link_of_image'}'''

    try:
        result = r.get(f'{BASE_URL}filter.php?c={cate}').json()

        cate_drinks = list()

        for i in result['drinks']:
            cate_drinks.append({
                'name':i['strDrink'],
                'id':i['idDrink'],
                'image':i['strDrinkThumb']})

        return cate_drinks

    except Exception as e:
        functions.logging_errors(e, 'pull_db/search_from_category')

# def get_cate_names():
#     ''' Give the category list. Take nothing
#      Result like list'''

#     try:
#         result = r.get(f'{BASE_URL}list.php?c=list').json()

#         cate_list = list()

#         for line in result['drinks']:
#             cate_list.append(line['strCategory'].replace('/', '').replace('  ', ' '))

#         cleaned_cate_list = [cate  for cate in cate_list if cate not in ['Beer', 'Coffee Tea', 'Other Unknown', 'Punch Party Drink', 'Soft Drink']]



#         return cleaned_cate_list 
#     except Exception as e:
#         functions.logging_errors(e, 'pull_db/get_cate_names')   



def get_cate_names_and_cover_image():

    category_and_image = [ {
                'name':'Ordinary Drink',
                'image':'https://www.thecocktaildb.com/images/media/drink/hrxfbl1606773109.jpg/small'
            }, 
            {
                'name':'Cocktail',
                'image':'https://www.thecocktaildb.com/images/media/drink/4tymma1604179273.jpg/small'
            },
            {
                'name':'Shot',
                'image':'https://www.thecocktaildb.com/images/media/drink/5a3vg61504372070.jpg/small'
            },
            {
                'name':'Homemade Liqueur',
                'image':'https://www.thecocktaildb.com/images/media/drink/swqxuv1472719649.jpg/small'
            },
            {
                'name':'Cocoa',
                'image':'https://www.thecocktaildb.com/images/media/drink/hdzwrh1487603131.jpg/small'
            },
            {
                'name':'Shake',
                'image':'https://www.thecocktaildb.com/images/media/drink/syusvw1468876634.jpg/small'
    
            }
            ]

    return category_and_image




def get_alchoholic_or_non_names(non_or : str):

    '''filter the driks about the alchohol.Take str give dict. 
        if u want search alchoholic drinks give ('Alcoholic')
        if u need non-alcholic drinks give ('Non_Alcoholic')
        Result like ('name_of_drink':'id_of_drink')'''

    try:
        result = r.get(f'{BASE_URL}filter.php?a={non_or}').json()
        drinks = dict()

        for i in result['drinks']:
            drinks[i['strDrink']] = i['idDrink']

        return drinks
        
    except Exception as e:
        functions.logging_errors(e, 'pull_dab/get_alchoholic_or_non_names')



#Ingredient
def search_drinks_vie_ingr(ingr:str):

    '''Search drinks via ingridients, take str, give list of dict
     Result like [{'name':name_of_drink,
                   'id':id_of_drink,
                   'image':image_link_of_drink}]'''
    

    try:
        result = r.get(f'{BASE_URL}filter.php?i={ingr}').json() 
                  

        return result  
    except Exception as e:
        functions.logging_errors(e, 'pull_db/search_drink_via_ingr')



def get_list_of_ingr():

    ''' the list of ingredients. Take nothing give the list'''

    try:
        result = r.get(f'{BASE_URL}list.php?i=list').json()

        if result:
            ingridents = []

            for lin in result['drinks']:
                ingridents.append(lin.get('strIngredient1'))

            return ingridents    

        else:
            print('Ingridients not found')
    except Exception as e:
        functions.logging_errors(e, 'pull_db/get_list_of_igr') 


def get_info_about_ingr(ingr_name: str):

    '''Infromation about the ingredients. Take str giv list of dict
    result  '''
    try:
        result = r.get(f'{BASE_URL}search.php?i={ingr_name}').json()
         

        
        return result   
        
    except Exception as e:
        functions.logging_errors(e, 'pull_db/get_info_about_ing')







def search_drink_first_letter(let:str):

    '''From one search drinks, take str, give json
     result like json variabel, full date '''

    try:
        result = r.get(f'{BASE_URL}search.php?f={let}').json()

        return result
    
    except Exception as e:
        print(f'ERROR::m {e}')





def get_random_drink():

    try:
        result = r.get(f'{BASE_URL}/random.php').json()

        return result

    except Exception as e:
        functions.logging_errors(e, 'pull_db/get_random_drink')
