from django.conf.urls import patterns, include, url
from tastypie.api import Api
from inventory.api import InventoryRecordResource, ItemResource, CategoryResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
inventory_record = InventoryRecordResource()
item = ItemResource()
category = CategoryResource()

v1_api.register(inventory_record)
v1_api.register(item)
v1_api.register(category)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/', include(v1_api.urls)),
)
