details = {'name':'Yasoda','age':22, 'fav_num':[1,2,3]}
print(details['name'])

details['fav_lang'] = 'Python' # add a new key fav_lang
print(details)

print(len(details))

details.pop('fav_num') # fav_num lae hataedincha
print(details)

details['age'] = 23 # now age lai edit garyo
print(details)
