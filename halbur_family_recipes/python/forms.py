from flask_wtf import FlaskForm
from wtforms import Form, SelectField, StringField, IntegerField, TextAreaField, SubmitField

class InsertRecipe(FlaskForm):
    recipe_name = StringField('recipe_name', render_kw={"placeholder": "Recipe Name..."})
    recipe_type = SelectField('recipe_type', choices=[('Breakfast', 'Breakfast'), ('Appetizers', 'Appetizers'), ('Main Entrees', 'Main Entrees'),
                              ('Dessert', 'Dessert'), ('Snack', 'Snack'), ('Other', 'Other')],
                              render_kw={"placeholder": "Recipe Type..."})
    recipe_origin = StringField('recipe_origin', render_kw={"placeholder": "Recipe Origin..."})
    recipe_preheat = IntegerField('recipe_preheat', render_kw={"placeholder": "Preheat Temperature..."})
    recipe_ingredients = TextAreaField('recipe_ingredients', render_kw={"placeholder": "Ingredients..."})
    recipe_directions = TextAreaField('recipe_directions', render_kw={"placeholder": "Directions..."})
    submit_recipe = SubmitField('Submit')
