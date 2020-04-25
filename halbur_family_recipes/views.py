import os
from python.dynamodb import put_item, get_all_items
from flask import Flask, render_template, redirect, url_for, request
from python.forms import InsertRecipe

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)


@app.route("/")
def index():
    form = InsertRecipe()
    # data = get_all_items()
    return render_template('index.html', form=form)


@app.route('/handle_new_recipe',  methods=['GET', 'POST'])
def insert_recipe():
    form = InsertRecipe()
    put_item(recipe_name=request.form['recipe_name'],
             recipe_type=request.form['recipe_type'],
             recipe_origin=request.form['recipe_origin'],
             recipe_preheat=request.form['recipe_preheat'],
             recipe_ingredients=request.form['recipe_ingredients'],
             recipe_directions=request.form['recipe_directions'])
    return render_template('index.html', form=form)
