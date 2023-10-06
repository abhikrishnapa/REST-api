#CRUD
from rest_framework.decorators import api_view
from workapp.models import Record
from workapp.serializers import RecordSerializer

#login and Register
from .serializers import UserRegister
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

# Login and Register
class register(APIView):
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)
    
class welcome(APIView):
    permission_classes =(IsAuthenticated,)
    
    def get(self,request):
        content={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)
    
# Pagination
class setPagination(PageNumberPagination):
    page_size=2
        
class paginationApi(ListAPIView):
    queryset=Record.objects.all()
    serializer_class=RecordSerializer
    pagination_class=setPagination
    filter_backends=(SearchFilter,)
    search_fields=('name','price','year','quantity')

# CRUD
@api_view(['GET'])
def apiOverview(request):
    api_urls = {\
        'Register': '/register/',
        'Create':'/create/',
        'Read':'/read/',
        'ReadAll':'/readAll/<str:pk>/',
        'Update':'/update/<str:pk>',
        'Delete':'/delete/<str:pk>',
        'DeleteAll':'/deleteAll/',
        'Pagination': 'paginationApi/',
    }
    return Response(api_urls)

# CREATE
@api_view(['POST'])
def create(request):
    serializer = RecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# READ
@api_view(['GET'])
def readAll(request):
    tasks = Record.objects.all() #ALL
    serializer = RecordSerializer(tasks,many=True)
    return Response(serializer.data)

# READ BY ID
@api_view(['GET'])
def read(request,pk):
    tasks = Record.objects.get(id=pk) #ID
    serializer = RecordSerializer(tasks,many=False)
    return Response(serializer.data)

# UPDATE
@api_view(['PUT'])
def update(request,pk):
    rec = Record.objects.get(id=pk) 
    serializer = RecordSerializer(instance=rec,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#DELETE BY ID
@api_view(['DELETE'])
def delete(request,pk):
    rec = Record.objects.get(id=pk)
    rec.delete()
    return Response("item succesfully deleted")

#DELETE ALL RECORDS
@api_view(['DELETE'])
def deleteAll(request):
    tasks = Record.objects.all() #ALL
    tasks.delete()
    return Response("item succesfully deleted")    












# @csrf_exempt
# def recordAPI(request):
#     if request.method == 'GET':
#         jdata = request.body
#         stream = io.BytesIO(jdata)
#         pydata = JSONParser().parse(stream)
#         id = pydata.get('id', None)
#         if id is not None:
#             rec = Record.objects.get(id=id)
#             serializer = RecordSerializer(rec)
#             jdata = JSONRenderer().render(serializer.data)
#             return HttpResponse(jdata,content_type='application/json')
#         # if id is none
#         rec = Record.objects.all()
#         serializer = RecordSerializer(rec, many=True)
#         jdata = JSONRenderer().render(serializer.data)
#         return HttpResponse(jdata, content_type='application/json')
    
#     # for POST data
#     if request.method == 'POST':
#         jdata = request.body
#         stream = io.BytesIO(jdata)
#         pydata = JSONParser().parse(stream)
#         serializer = RecordSerializer(data=pydata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data is created'}
#             jdata = JSONRenderer().render(res)
#             return HttpResponse(jdata, content_type='application/json')
#         # If not valid
#         jdata = JSONRenderer().render(serializer.errors)
#         return HttpResponse(jdata, content_type='application/json')
    
#     #for put data
#     if request.method == 'PUT':
#         jdata = request.body
#         stream = io.BytesIO(jdata)
#         pydata = JSONParser().parse(stream)
#         id = pydata.get('id')
#         rec = Record.objects.get(id=id)
#         serializer = RecordSerializer(rec, data=pydata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data are updated'}
#             jdata = JSONRenderer().render(res)
#             return HttpResponse(jdata, content_type='application/json')
#         jdata = JSONRenderer().render(serializer.errors)
#         return HttpResponse(jdata, content_type='application/json')
    
#     #for delete
#     if request.method == 'DELETE':
#         data = request.body
#         stream = io.BytesIO(data)
#         pydata = JSONParser().parse(stream)
#         id = pydata.get('id')
#         rec = Record.objects.get(id = id)
#         rec.delete()
#         res = {'msg':'Data was deleted !'}
#         jdata = JSONRenderer().render(res)
#         return HttpResponse(jdata,content_type='application/json')
    

