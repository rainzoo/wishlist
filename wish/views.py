from datetime import date
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext 
from wish.models import Wishlist, WishlistForm 

def index(request):
	userstring = request.META['HTTP_USER_AGENT'].split()
	msg = ""
	if 'MSIE' in userstring:
		ie = userstring[userstring.index('MSIE')+1].split(".")[0]
		if ie == '6':
			msg = "This site doesn't look good in IE6"
	return render_to_response('index.html',{ 'browser': msg},context_instance=RequestContext(request))

def detail(request, wish_id):
	w = get_object_or_404(Wishlist, pk=wish_id)
	return render_to_response('detail.html', {'wish': w})
	
def create(request):
	f = WishlistForm()
	return render_to_response('create.html', {'form' :f},context_instance=RequestContext(request))
	
def store(request):
    w = WishlistForm(request.POST)
    #w.pub_date = date.today()
    try:
        new_list = w.save()
        return HttpResponseRedirect('/wishes/')
    except:
        return HttpResponseRedirect('/create/')