from source_modules.fox import FoxQuery

temp = FoxQuery('trump')
for i in temp.result_articles:
    print(i.metatags['og:title'])