from .models import Article
from .serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, mixins, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView


## Generic viewset
class ArticleViewSet(viewsets.GenericViewSet, 
					mixins.ListModelMixin,
					mixins.CreateModelMixin,
					mixins.RetrieveModelMixin,
					#mixins.DestroyModelMixin,
					mixins.UpdateModelMixin,
					):
	serializer_class = ArticleSerializer
	queryset = Article.objects.all()
	authentication_classes = [TokenAuthentication]
	permission_classes = (IsAuthenticatedOrReadOnly,)

## View sets
# class ArticleViewSet(viewsets.ViewSet):
# 	def list(self, request):
# 		articles = Article.objects.all()
# 		serializer = ArticleSerializer(articles, many=True)
# 		return Response(serializer.data)

# 	def create(self, request):
# 		serializer = ArticleSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def retrieve(self, request, pk=None):
# 		queryset = Article.objects.all()
# 		article = get_object_or_404(queryset, pk=pk)
# 		serializer = ArticleSerializer(article)
# 		return Response(serializer.data)

# 	def update(self, request, pk=None):
# 		article = Article.objects.get(pk=pk)
# 		serializer = ArticleSerializer(article, data=request.data) 
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## Generic Views with mixins
class GenericAPIView(generics.GenericAPIView, 
					mixins.ListModelMixin, 
					mixins.CreateModelMixin,
					mixins.UpdateModelMixin,
					mixins.RetrieveModelMixin,
					mixins.DestroyModelMixin
					):
	serializer_class = ArticleSerializer
	queryset = Article.objects.all()
	lookup_field = 'id'

	#authentication_classes = [SessionAuthentication, BasicAuthentication]
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, id = None):
		if id:
			return self.retrieve(request)
		else:
			return self.list(request)

	def post(self, request):
		return self.create(request)

	def put(self, request, id=None):
		return self.update(request, id)

	def delete(self, request, id=None):
		return self.destroy(request, id)


## Class based views
class ArticleAPIView(APIView):

	def get(self, request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):

	def get_object(self, pk):
		try:
			return Article.objects.get(id=pk)
		except Article.DoesNotExist:
 			return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, pk):
		article = self.get_object(pk)
		serializer = ArticleSerializer(article)
		return Response(serializer.data)

	def put(self, request, pk):
		article = self.get_object(pk)
		serializer = ArticleSerializer(article, data=request.data) 
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		article = self.get_object(pk)
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


## decorated function based views
# ## View all content, create specific content
# @api_view(['GET', 'POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def article_list(request):

# 	# Get list of all articles with a GET request
# 	if request.method == 'GET':
# 		articles = Article.objects.all()
# 		serializer = ArticleSerializer(articles, many=True)
# 		return Response(serializer.data)

# 	# If the request method is POST and valid, serialize it from JSON and save the article
# 	elif request.method == "POST":
# 		serializer = ArticleSerializer(data=request.data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ## View specific, Update specific, Delete specific content
# @api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def article_detail(request, pk):

# 	# Check that the pk of the article actually exists
# 	try:
# 		article = Article.objects.get(id=pk)
# 	except Article.DoesNotExist:
# 		return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

# 	# if the request method is get, return the specific article
# 	if request.method == "GET":
# 		serializer = ArticleSerializer(article)
# 		return Response(serializer.data)

# 	# if the request method is PUT, serialize it from JSON and check its valid
# 	elif request.method == "PUT":
# 		serializer = ArticleSerializer(article, data=request.data) 
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == "DELETE":
# 		article.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)


