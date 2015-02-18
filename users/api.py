from .models import User
from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class UserDetails(APIView):
	
	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		serialized_user = UserSerializer(user)
		return Response(serialized_user.data)


class GetFriends(APIView):

	def get(self, request, pk, format=None):
		user = User.objects.get(pk=pk)
		friends = user.friends.all()
		serialized_friends = UserSerializer(friends, many=True)
		return Response(serialized_friends.data)


class DeleteFriend(APIView):

	def delete(self, request, pk, friend_id, format=None):
		user = User.objects.get(pk=pk)
		friend = user.friends.get(pk=friend_id)
		serialized_friend = UserSerializer(friend)
		user.friends.remove(friend)
		return Response(serialized_friend.data)



class DeleteUser(APIView):

	def delete(self, request, pk, format=None):
		try:
			user = User.objects.get(pk=pk)
			user.delete()
			return Response({'status':True})
		except:
			return Response({'status':False})


class CreateUser(APIView):

	def post(self, request, format=None):
		data = request.data
		user = User(name = data['name'])
		user.save()
		serialized_user = UserSerializer(user)
		return Response(serialized_user.data)


class AddFriends(APIView):

	def post(self, request, pk, format=None):
		user = User.objects.get(pk=pk)

		data = request.data
		friends_data_list = data['friends']
		print(friends_data_list)
		status_dict = {}
		for friends_data in friends_data_list:
			try:
				friendId = friends_data['id']
				friend = User.objects.get(pk=friendId)
				user.friends.add(friend)
				status_dict[str(friendId)] = True
			except User.DoesNotExist:
				status_dict[str(friendId)] = False

		return Response(status_dict)

