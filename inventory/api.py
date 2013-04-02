from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from inventory.models import Item, InventoryRecord, Category
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
class CategoryResource(ModelResource):
	class Meta:
		queryset = Category.objects.all()
		resource_name = 'category'
		allowed_methods = ['get']

		authentication = BasicAuthentication()
		authorization = Authorization()

class ItemResource(ModelResource):
	category = fields.ForeignKey(CategoryResource, 'category')
	class Meta:
		queryset = Item.objects.all()
		resource_name= 'item'
		filtering = {
			'name': ['exact', 'contains', 'startswith']
		}
		allowed_methods = ['get', 'post', 'put']

		authentication = ApiKeyAuthentication()
		authorization = Authorization()
		
class InventoryRecordResource(ModelResource):
	item = fields.ForeignKey(ItemResource, 'item')
	class Meta:
		queryset = InventoryRecord.objects.all()
		resource_name = 'inventory_record'
		allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
		fields = ['item', 'quantity', 'last_update']
		filtering = {
			'item': ALL_WITH_RELATIONS
		}
		authorization = Authorization()
