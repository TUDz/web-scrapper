from lxml import html
import requests
import pandas as pd

URI = 'http://books.toscrape.com'
page = requests.get(URI)
tree = html.fromstring(page.content)

# title_pattern = '//article[@class="product_pod"]/h3/a/@title'
# titles = tree.xpath(title_pattern)
# price_pattern = '//div[@class="product_price"]/p[@class="price_color"]/text()'
# prices = tree.xpath(price_pattern)

# datos_completo = [list(row) for row in zip(titles, prices)]
# dataframe_scrap = pd.DataFrame(datos_completo, columns=['titles','prices'])
title_pages_pattern = '//article[@class="product_pod"]/h3/a/@href'
title_pages = tree.xpath(title_pages_pattern)

subpage_category_pattern = '//ul[@class="breadcrumb"]/li[@class="active"]/text()'


sub_page_main_content_pattern = '//article[@class="product_page"]/div[@class="row"]/div[contains(@class, "col-sm-6")]'
subpage_title_pattern = '//h1/text()'
subpage_price_pattern = '//p[@class="price_color"]/text()'
subpage_stock_pattern = '//p[contains(@class, "instock") and contains(@class, "availability")]/text()'

for c in title_pages:
    current_URL = f'{URI}/{c}'
    sub_page = requests.get(current_URL)
    sub_tree = html.fromstring(sub_page.content)
    
    sub_page_category = sub_tree.xpath(f'subpage_category_pattern')
    sub_page_title = sub_tree.xpath(f'{sub_page_main_content_pattern}{subpage_title_pattern}')
    sub_page_price = sub_tree.xpath(f'{sub_page_main_content_pattern}{subpage_price_pattern}')
    sub_page_stock = sub_tree.xpath(f'{sub_page_main_content_pattern}{subpage_stock_pattern}')
    print(sub_page_category)
