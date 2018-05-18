# views will essentially be that middle layer getting data from the ORM (the models) and returning it to the template so we can actually look at it

from django.shortcuts import render
from .models import Bookmark, PersonalBookmark

# index view that takes a request
def index(request):
    context = {} # he mentioned python dictionary? put stuff in here soon. analogous to what we've done with express and react
    # TODO: business logic, get data, etc. - do some stuff to the context
    context['bookmarks'] = Bookmark.objects.exclude(
        id__in=PersonalBookmark.objects.values_list('id'))
    if request.user.is_anonymous:
        context['personal_bookmarks'] = PersonalBookmark.objects.none()
    else:
        context['personal_bookmarks'] = PersonalBookmark.objects.filter(
            user=request.user)
    return render(request, 'bookmarks/index.html', context)
