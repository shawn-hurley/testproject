from django.db import models

# Create your models here.
class Category(models.Model):
	"""Category for each item."""
	name = models.CharField("Category Name", max_length=50)
	description = models.TextField("Description")

	def save(self):
		super(Category, self).save()

	def get_category(cate):
		return Category.objects.filter(name=cate)

	def __unicode__(self):
		return self.name


class Item(models.Model):
	"""Item, this should never be updated unless by admins
		These will only be managed by admins through either 
		the admin interface or what will eventually be the dashboard
	"""
	name = models.CharField("Item Name", max_length=150)
	category = models.ForeignKey(Category)
	min_num = models.PositiveIntegerField("Minumum Number")

	def save(self):
		super(Item, self).save()

	def get_item(item):
		return Item.objects.get(name=item)

	def __unicode__(self):
		return self.name


class InventoryRecord(models.Model):
	"""This will record that is manipulated trough the interface.
		This will keep track of quantity of that item, and the last
		time it was edited
	"""
	item = models.ForeignKey(Item)
	quantity = models.PositiveIntegerField("Quantity")
	last_update = models.DateTimeField("Last Update", auto_now_add=True)

	def save(self):
		super(InventoryRecord, self).save()

	def get_inventory_recorded(record):
		return InventoryRecord.objects.get(name=record)

	def __unicode__(self):
		return unicode(self.item)
