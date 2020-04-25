import boto3
import os
import uuid

AWS_ACCESS_KEY_ID = os.getenv('AWSAccessKeyId')
AWS_SECRET_ACCESS_KEY = os.getenv('AWSSecretKey')

resource = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name='us-east-1')
table = resource.Table('halbur_family_recipes')
bucket = 'halbur-recipes'


def put_item(recipe_name=None, recipe_type=None, recipe_origin=None,
             recipe_preheat=None, recipe_ingredients=None,
             recipe_directions=None, attachment=None, img=None):
    local = locals()

    for variable in locals():
        if local[variable] is None or local[variable] == '':
            print("delete ")
            print(variable)
            del local[variable]
    print(local)
    # response = table.put_item(Item={
    #     'id': str(uuid.uuid1()),
    #     'recipe_name': recipe_name,
    #     'recipe_type': recipe_type,
    #     'recipe_origin': recipe_origin,
    #     'recipe_preheat': recipe_preheat,
    #     'recipe_ingredients': recipe_ingredients,
    #     'recipe_directions': recipe_directions})



def get_all_items():
    response = table.scan()
    data = response['Items']
    return data


def get_item():
    return ''


def edit_item():
    return ''


def delete_item():
    return ''
