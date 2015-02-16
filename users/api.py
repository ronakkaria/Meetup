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


class Friends(APIView):

	def get(self, request, pk, format=None):
		user = User.objects.get(pk=pk)
		friends = user.friends.all()
		serialized_friends = UserSerializer(friends, many=True)
		return Response(serialized_friends.data)


class DeleteUser(APIView):

	def get(self, request, pk, format=None):
		try:
			user = User.objects.get(pk=pk)
			user.delete()
			return Response({'status':True})
		except:
			return Response({'status':False})





