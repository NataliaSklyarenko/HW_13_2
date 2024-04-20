from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongogodb

def main(request, page=1):
    db=get_mongodb()
    quotes=db.quotes.find()
    per_page=10
    paginator=Paginator(list(quotes), per_page)
    quotes_on_page=paginator.page(page)
    return render(request, 'quotes/index.htnl',context={'quotes':quotes_on_page})