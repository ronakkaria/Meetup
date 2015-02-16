from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	# relationships = models.ManyToManyFied('self', through='Relationship', 
	# 	symmetrical = True, 
	# 	related_name = 'related_to')
	friends = models.ManyToManyFied('self')



# RELATIONSHIP_FRIEND = 1
# RELATIONSHIP_BLOCKED = 2
# RELATIONSHIP_STATUSES = (
#     (RELATIONSHIP_FRIEND, 'Friend'),
#     (RELATIONSHIP_BLOCKED, 'Blocked'),
# )

# class Relationship(models.Model):
# 	from_person = models.ForeignKey(User, relate_name = '')
# 	