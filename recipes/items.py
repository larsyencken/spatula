# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class RecipeItem(Item):
    url = Field()
    rating = Field()
    prep_time = Field()
    cook_time = Field()
    difficulty = Field()
    ingredients = Field()
    method = Field()
    serves = Field()
