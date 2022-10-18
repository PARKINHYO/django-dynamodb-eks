from dynamorm import DynaModel
from marshmallow import fields
from django.conf import settings


class MyTable(DynaModel):
    class Table:
        name = settings.DB_TABLE
        hash_key = settings.HASH_KEY

    class Schema:
        name = fields.String()
        diet = fields.String()
        email = fields.Email()
        created_on = fields.DateTime()


DIET_CHOICES = [('', 'choose diet'), ('gluten-free', 'gluten-free'),
                ('Keto', 'Keto'), ('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan')]
