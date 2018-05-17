# views will essentially be that middle layer getting data from the ORM (the models) and returning it to the template so we can actually look at it

from django.shortcuts import render
from .models import Bookmark

# index view that takes a request
def index(request):
    context = {} # he mentioned python dictionary? put stuff in here soon. analogous to what we've done with express and react
    # TODO: business logic, get data, etc. - do some stuff to the context
    context['bookmarks'] = Bookmark.objects.all()
    return render(request, 'bookmarks/index.html', context)
