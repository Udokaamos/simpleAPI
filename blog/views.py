from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Post
from .serializers import PostSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, PermissionDenied

# Create your views here.
@swagger_auto_schema(methods=['POST'] ,
                    request_body=PostSerializer())
@api_view(['GET', 'POST'])
def blog_posts(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        
        data = {
           "message":"successful",
           "data": serializer.data
        }
    
    
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): 
                
            serializer.save()
            data = {
                'message' : 'success',
                'data'  : serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        else:
            data = {
                'message' : 'failed',
                'error'  : serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    
    
    

    
    
@swagger_auto_schema(methods=['put'] ,
                    request_body=PostSerializer())
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def post_detail(request, user_id,):

    
    try:
        user = Post.objects.get(id=user_id)
    except Post.DoesNotExist:

        data = {
            'message' : 'failed',
            'error'  : f"Post with ID {user_id} does not exist."
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PostSerializer(user)
        
        data = {
           "message":"successful",
           "data": serializer.data
        }
    
    
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
                
            serializer.save()
            data = {
                'message' : 'success',
                'data'  : serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        else:
            data = {
                'message' : 'failed',
                'error'  : serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=="DELETE":
        user.delete()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    



@swagger_auto_schema(methods=['POST'] ,
                    request_body=PostSerializer())
@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def posts(request):
    user= request.user
    if request.method == "GET":
        post_ = Post.objects.filter(user=user)
        serializer = PostSerializer(post_, many=True)
        
        data = {
           "message":"successful",
           "data": serializer.data
        }
    
    
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): 
            if "user" in serializer.validated_data.keys():
                serializer.validated_data.pop("user")
            # print(serializer.validated_data)  
            song = serializer.validated_data["song"]
            
            # print(song)
            post_list = Post.objects.create(user=user, song=song)
            new_serializer = PostSerializer(post_list)
            
            data = {
                'message' : 'success',
                'data'  : new_serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        else:
            data = {
                'message' : 'failed',
                'error'  : serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    
    
    

    
    
# @swagger_auto_schema(methods=['POST'] ,
#                     request_body=SongSerializer())
# @api_view(['GET', 'POST', 'DELETE'])
# @authentication_classes([BasicAuthentication])
# # @permission_classes([IsAuthenticated])
# def post_detail(request, item_id):
#     user = request.user
    
#     try:
#         song = Post.objects.get(id=item_id)
#     except Post.DoesNotExist:

#         data = {
#             'message' : 'failed',
#             'error'  : f"Post with ID {item_id} does not exist."
#         }
#         return Response(data, status=status.HTTP_404_NOT_FOUND)
#     if song.user != request.user:
#         raise PermissionDenied(detail={"message":"You do not have the permission to view this item."})
    
#     if request.method == "GET":
#         serializer = PostSerializer(song)
        
#         data = {
#            "message":"successful",
#            "data": serializer.data
#         }
    
    
#         return Response(data, status=status.HTTP_200_OK)
    
#     elif request.method=="DELETE":
#         song.delete()
        
#         return Response({}, status=status.HTTP_204_NO_CONTENT)
