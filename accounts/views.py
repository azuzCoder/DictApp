from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView,
                     generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


# @api_view(['GET', 'POST', 'PUT'])
# def work(request):
#     if request.method.upper() == 'GET':
#         return Response(data={'blee': 'ishlayapti'}, status=status.HTTP_200_OK)
#     if request.method.upper() == 'POST':
#         print('data: ',request.data)
#         # print('meta: ', request.meta)
#         return Response(data={'blee': 'ishlayapti'}, status=status.HTTP_200_OK)
#     return Response(data={'get': 'get yo post emasku pidr'}, status=status.HTTP_200_OK)
