
from amazon.paapi import AmazonAPI

KEY    = "<INPUT YOUR KEY>"
SECRET = "<INPUT YOUR SECRET KEY>"
TAG    = "<INPUT YOUR PARTNER TAG>"
COUNTRY = "JP"
keyword = "任天堂Switch"

amazon = AmazonAPI(KEY, SECRET, TAG, COUNTRY)

products = amazon.search_items(keywords=keyword)
asin     = products["data"][0].asin
price    = products["data"][0].offers.listings[0].price.amount
url      = products["data"][0].detail_page_url
title    = products["data"][0].item_info.title.display_value

print(asin, price, url, title)

