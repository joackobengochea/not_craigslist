import requests
from requests.compat import quote_plus
from django.shortcuts import render

from .scrapper import scrape_listings


BASE_CRAIGSLIST_URL = 'https://buenosaires.craigslist.org/search/?query={}'


# Create your views here.
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    full_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(full_url)
    data = response.text
    listings = scrape_listings(data)

    context = {
        'search': search,
        'listings': listings,
    }
    return render(request, 'myapp/new_search.html', context=context)
