from flask import Flask, render_template, request
import functions
import pull_db



app = Flask(__name__)


@app.route('/')

def index():
    try:

        random_drink = functions.result_of_random_drink()
        head = functions.html_header()
        footer = functions.html_footer()
    
        return render_template('index.html', random_drink=random_drink, head=head, footer=footer)
     
    except Exception as e:
        functions.logging_errors(e, 'back_end/index')



@app.route('/search')

def search():

    try:

        head = functions.html_header()
        cock_name = request.args.get('cock_name')
        footer = functions.html_footer()

        if cock_name:
            cocktails = functions.results_from_search_by_name(cock_name)
        else:
            cocktails = None


        return render_template('search.html', cocktails=cocktails, header=head, footer=footer)
    except Exception as e:
        functions.logging_errors(e, 'back_end/search')


@app.route('/categories')



def categories():

    try:
        cate_image = pull_db.get_cate_names_and_cover_image()
        
        return render_template('categories.html', cate_and_image = cate_image)


        
    except Exception as e:
        functions.logging_errors(e, 'back_end/categories')
        return render_template(f'<Error: {e} ')


    


@app.route('/category/<cat_name>')

def category(cat_name):

    try:
        drinks = functions.result_from_categories(cat_name)

        return render_template('category.html', drinks=drinks, cat_name=cat_name)
    

      

    except Exception as e:
        functions.logging_errors(e, 'back_end/category')
        return 'error fayl'
 
@app.route('/ingridients')


def ingridients():

    try:
        head = functions.html_header()

        researched_ingr_name = request.args.get('ingr_name', 'Gin')
        result_of_search =  None

        if researched_ingr_name:
            result_of_search = functions.result_from_ingridient_info(researched_ingr_name)
            


        ingridients = pull_db.get_list_of_ingr()

        return render_template('ingridients.html', ingridients=ingridients, result_of_search=result_of_search, head=head)

    except Exception as e:
        functions.logging_errors(e, 'back_en/ingridients')


@app.route('/ingredient/<ingr_name>')

def ingredient(ingr_name):

    try:

        header = functions.html_header()

        result_of_search =functions.result_from_ingridient_info(ingr_name)
        coctails = functions.result_drinks_from_ingr(ingr_name)
        footer = functions.html_footer()

        return render_template('ingredient.html', ingr_info=result_of_search ,head=header, cocktails=coctails, footer=footer)

    except Exception as e:
        functions.logging_errors(e, 'back_end/ingridient')
        








if __name__ == '__main__':
    app.run(debug=True)   