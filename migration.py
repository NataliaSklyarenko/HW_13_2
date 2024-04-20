import os
import django

from pymongo import mongo_client
os.environ.setdefault("DJANGO_SETTINGS_MODULE","hw_project.settings" )
django.setup()

from quotes.models import Quote, Tag, Author
client=mongo_client("mongodb://localhost")
db=client.hw
authors=db.authors.find()
for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )
quotes=db.quotes.find()
for quote in quotes:
    tags=[]
    for tag in quotes["tags"]:
        t,*_=Tag.objective.get_or_create(name=tag)
        tags.append(t)
print(tags)
exist_quote=len(Quote.objects.filter(quote=quote['quote']))
if not exist_quote:
    author=db.authors.find_one({'_id':quote['author']})
    a=Author.objects.get(fullname=author['fullname'])
    q=Author.objects.create(
      quote=quote['quote'])
    author=a  
    for tag in tags:
        q.tags.add(tag)
    
