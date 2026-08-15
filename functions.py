import pull_db
import datetime
from pathlib import Path
import json

Path('logging').mkdir(exist_ok=True)


def logging_errors(e, location):

    dic = {
    'date':datetime.datetime.now().strftime('%Y_%m_%d-%H:%M:%S'),
    'type_of_error':type(e).__name__,
    'message': str(e),
    'location':location
}

    with open(f'logging/logs_at_{datetime.datetime.now().strftime("%Y-%m-%d")}.jsonl', 'a', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)



def html_header():

     head ='''<article id="head" class="container">
                <section class="description_text">
                    <a href="/" class="brand"><h2 class="brand">Mixoo...</h2></a>
                </section>

                <nav class="navi">
                    <ul class="line_ul">
                        <li><a href="/">Home</a></li>
                        <li><a href="/categories">Categories</a></li>
                        <li><a href="">Blog</a></li>
                        <li><a href="/ingridients">Ingridients</a></li>    
                    </ul>
                </nav>

            </article>'''

     return head

def html_footer():

    footer = '''<article id="footer" class="container">

            <h2 class="brand">Mixoo..</h2>

            <section class="copyright">
                <p>2026 / Copyright ©  : 
                <span></span><a href="https://www.doneatelli.com" target="_blank" class="my_button"> Elli </a></span></p>
            </section>

            <section class="db">
                <p>Used Date Base :  
                <span></span><a href="https://www.thecocktaildb.com/documentation" target="_blank" class="my_button">TheCocktailDB</a></span></p>
            </section>



        </article>'''
    return footer


def results_from_search_by_name(name_of_cocktail: str):

    try:

        result = pull_db.search_coctail_from_name(name_of_cocktail)

        if not result or not result.get('drinks'):
            return None

        coctails = []

        for drink in result['drinks']:

            same_drinks_ing = []

            for i_in in range(1, 16,1):

                ingr  = drink[f'strIngredient{i_in}']
                mens = drink[f'strMeasure{i_in}']

                if mens == None:
                    mens = 'Fill it'

                if ingr:
                    same_drinks_ing.append({'ingr': ingr,
                                            'measure': mens })

            coctails.append({
                'name': drink.get('strDrink'),
                'cate': drink.get('strCategory'),
                'glass': drink.get('strGlass'),
                'eng_resept': drink.get('strInstructions'),
                'de_resept': drink.get('strInstructionsDE'),
                'image': drink.get('strDrinkThumb'),
                'ingridients': same_drinks_ing

            })
            

        return coctails

    except Exception as e:
        logging_errors(e, 'functions/result_from_search_by_name')

def result_from_categories(name_of_category: str):


    '''Give the name to search in categories.
     Take str give list of dict'''


    
    categories = pull_db.get_cate_names_and_cover_image()
    

    

    try:

        if name_of_category in [cat.get('name') for cat in categories]:
            result = pull_db.search_from_categ(name_of_category)
            drinks = list()

            for i in result:
                drink = i['name']
                image = i['image']

                drinks.append({'name':drink,
                               'image':image})
            return drinks    

              
          
        else:
            logging_errors('no result for category', 'functions/result_from_category')  

    except Exception as e:
        logging_errors(e, 'functions/result_from_categories')

def result_from_ingridient_info(ingr):

    try:

            result = pull_db.get_info_about_ingr(ingr)

            if result:
                        
                        ingridients_info = list()

                        for inf in result['ingredients']:
                            name = inf.get('strIngredient')
                            description = inf.get('strDescription')
                            image_link = f'https://www.thecocktaildb.com/images/ingredients/{inf.get('strIngredient')}.png'
                            vol = inf.get('strABV')
            
                        
                            ingridients_info.append({
                                'name':name,
                                'description':description if description != None else '' ,
                                'image':image_link if image_link != None else '',
                                'vol': vol if vol != None else ''
                            })
                            return  ingridients_info                        
            else:
                logging_errors('no result', 'functions/result_from_ingridient_info')

    except Exception as e:
        logging_errors(e, 'functions/result_from_ingridient_info')

def result_of_random_drink():

    try:

        result = pull_db.get_random_drink()

        if not result or not result.get('drinks'):
                    return None
        
        coctails = None
        
        for drink in result['drinks']:
        
            same_drinks_ing = []
        
            for i_in in range(1, 16,1):
            
                ingr  = drink[f'strIngredient{i_in}']
                mens = drink[f'strMeasure{i_in}']
            
                if mens == None:
                    mens = 'Fill it'
            
                if ingr:
                    same_drinks_ing.append({'ingr': ingr,
                                            'measure': mens })
            
                coctails = {
                            'name': drink.get('strDrink'),
                            'cate': drink.get('strCategory'),
                            'glass': drink.get('strGlass'),
                            'eng_resept': drink.get('strInstructions'),
                            'de_resept': drink.get('strInstructionsDE'),
                            'image': drink.get('strDrinkThumb'),
                            'ingridients': same_drinks_ing
            
                        }
                        
            
        return coctails

    except Exception as e:
         logging_errors(e, 'functions/result_of_random_drink')

def result_drinks_from_ingr(ingr):

    try:
        cocktails = []
        result = pull_db.search_drinks_vie_ingr(ingr)
     
        if not result or not result.get('drinks'):
            return []
     
        for item in result.get('drinks'):

             cocktails.append({
                  'name':item['strDrink'],
                  'image':item['strDrinkThumb']
             })
             
                 
     
        return cocktails
     
    except Exception as e:
        logging_errors(e, 'functions/result_drinks_from_ingr')




