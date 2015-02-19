from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class UserDetails(APIView):
	
	def get(self, request, id, format=None):
		user = User.getUserById(id)
		serialized_user = UserSerializer(user)
		return Response(serialized_user.data)


class GetFriends(APIView):

	def get(self, request, id, format=None):
		user = User.getUserById(id)
		friends = user.friends.all()
		serialized_friends = UserSerializer(friends, many=True)
		return Response(serialized_friends.data)


class DeleteFriend(APIView):

	def delete(self, request, id, friend_id, format=None):
		user = User.getUserById(id)
		friend = user.getFriendById(friend_id)
		serialized_friend = UserSerializer(friend)
		user.friends.remove(friend)
		return Response(serialized_friend.data)


class DeleteUser(APIView):

	def delete(self, request, id, format=None):
		user = User.getUserById(id)
		user.delete()
		serialized_user = UserSerializer(user)
		return Response(serialized_user)


class CreateUser(APIView):

	def post(self, request, format=None):
		data = request.data
		user = User(name = data['name'])
		user.save()
		serialized_user = UserSerializer(user)
		return Response(serialized_user.data)


class AddFriends(APIView):

	def post(self, request, id, format=None):
		user = User.getUserById(id)
		data = request.data
		friends_data_list = data['friends']
		status_dict = {}
		for friends_data in friends_data_list:
			friend_id = friends_data['id']
			if friend_id == id:
				continue
			try:
				friend = User.objects.get(id=friend_id)
				user.friends.add(friend)
				status_dict[str(friend_id)] = True
			except User.DoesNotExist:
				status_dict[str(friend_id)] = False
		return Response(status_dict)

