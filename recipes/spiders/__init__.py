# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


from __future__ import absolute_import, print_function, division

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from recipes.items import RecipeItem


class TasteSpider(CrawlSpider):
    name = 'taste'
    allowed_domains = ['www.taste.com.au']
    start_urls = ['http://www.taste.com.au/']
    rules = [
        Rule(SgmlLinkExtractor(allow=['/recipes/\d+/.*']),
             callback='parse_recipe',
             follow=True),
        Rule(SgmlLinkExtractor(deny=['/recipes/kitchen/.*']),
             follow=True),
    ]

    PATTERNS = {
        'rating': "//span[@itemprop='rating']//text()",
        'rating_count': "//td[@itemprop='review']//span[@itemprop='count']/text()",  # nopep8
        'ingredients': "//ul[@class='ingredient-table']//text()",
        'method': "//li[@class='methods']/p[@class='description']/text()",
        'prep_time': "//td[@class='prepTime']/em/text()",
        'cook_time': "//td[@class='cookTime']/em/text()",
        'difficulty': "//td[@class='difficultyTitle']/em/text()",
        'serves': "//td[@class='servings']/em/text()",
    }

    def parse_recipe(self, response):
        sel = Selector(response)
        recipe = RecipeItem()
        recipe['url'] = response.url
        for k, v in self.PATTERNS.iteritems():
            recipe[k] = filter(None, (x.strip()
                                      for x in sel.xpath(v).extract()))

        return recipe
