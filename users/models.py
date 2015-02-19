from django.db import models
from django.http import Http404

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	friends = models.ManyToManyField('self', blank=True)

	def __unicode__(self):
		return self.name
		
	@staticmethod
	def getUserById(id):
		try:
			return User.objects.get(id=id)
		except User.DoesNotExist:
			raise Http404
					
	def getFriendById(self, friend_id):
		try:
			return self.friends.get(id=friend_id)
		except User.DoesNotExist:
			raise Http404

	# relationships = models.ManyToManyFied('self', through='Relationship', 
	# 	symmetrical = True, 
	# 	related_name = 'related_to')





# RELATIONSHIP_FRIEND = 1
# RELATIONSHIP_BLOCKED = 2
# RELATIONSHIP_STATUSES = (
#     (RELATIONSHIP_FRIEND, 'Friend'),
#     (RELATIONSHIP_BLOCKED, 'Blocked'),
# )

# class Relationship(models.Model):
# 	from_person = models.ForeignKey(User, relate_name = '')
# 	