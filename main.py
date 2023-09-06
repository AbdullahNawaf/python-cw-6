person = {  
    'name': 'abdullah',
    'age': 17,
    'hobbies': ['volley ball', 'gaming', 'boxing']
}

person['age']= 18
print(person['name'])
print(person['age'])
person ['country'] = 'kuwait'
print (len(person))
person['hobbies'] = 'football'




def check_hobbies(person):
    if len(person['hobbies']) >= 3:
        print ("WOW YOU ARE AMAZING")


check_hobbies(person)





