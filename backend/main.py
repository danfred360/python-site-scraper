from source_modules.fox import FoxQuery
from source_modules.abc import ABCQuery

query = 'trump'

temp1 = FoxQuery(query)

temp1 = FoxQuery(query)
print('-----------------------------------------------------------------------------')
print('First Article on Fox\'s site for query: "{}" -->\n{}'.format(query, temp1.result_articles[0].info))
print('-----------------------------------------------------------------------------')

temp2 = ABCQuery(query)
print('-----------------------------------------------------------------------------')
print('First Article on ABC\'s site for query: "{}" -->\n{}'.format(query, temp2.result_articles[0].info))
print('-----------------------------------------------------------------------------')