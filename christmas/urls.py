from django.conf.urls import patterns, include, url
from django.contrib import admin
from wish.models import Wishlist
from django.views.generic import list_detail

admin.autodiscover()

list_info = {
			'queryset': Wishlist.objects.all(),
			'template_name': 'wishlists.html',
			}
			
urlpatterns = patterns('',
    url(r'^$', 'wish.views.index'),
	url(r'^create/$', 'wish.views.create'),
	url(r'^store/$', 'wish.views.store'),
	url(r'^wish/(?P<wish_id>\d+)/$', 'wish.views.detail'),
	url(r'^wishes/$', list_detail.object_list, list_info),
    url(r'^admin/', include(admin.site.urls)),
)