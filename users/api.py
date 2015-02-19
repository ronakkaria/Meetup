from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class UserDetails(APIView):
	
	def get(self, request, id, format=None):
		user = User.get_user_by_id(id)
		serialized_user = UserSerializer(user)
		return Response(serialized_user.data)


class GetFriends(APIView):

	def get(self, request, id, format=None):
		user = User.get_user_by_id(id)
		friends = user.friends.all()
		serialized_friends = UserSerializer(friends, many=True)
		return Response(serialized_friends.data)


class DeleteFriend(APIView):

	def delete(self, request, id, friend_id, format=None):
		user = User.get_user_by_id(id)
		friend = user.get_friend_by_id(friend_id)
		serialized_friend = UserSerializer(friend)
		user.friends.remove(friend)
		return Response(serialized_friend.data)


class DeleteUser(APIView):

	def delete(self, request, id, format=None):
		user = User.get_user_by_id(id)
		user.delete()


class CreateUser(APIView):

	def post(self, request, format=None):
		data = request.data
		user = User(name = data['name'])
		user.save()
		serialized_user = UserSerializer(user)
		return Response(serialized_user.data)


class AddFriends(APIView):

	def post(self, request, id, format=None):
		user = User.get_user_by_id(id)
		data = request.data
		friends_data_list = data['friends']
		status_dict = {}
		for friends_data in friends_data_list:
			try:
				friend_id = friends_data['id']
				friend = User.objects.get(id=friendId)
				user.friends.add(friend)
				status_dict[str(friend_id)] = True
			except User.DoesNotExist:
				status_dict[str(friend_id)] = False
		return Response(status_dict)

