from django.urls import path, include
# from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetails
from .views import GenericAPIView
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

## router for the viewset
router = DefaultRouter()
router.register('article', ArticleViewSet, basename = 'article')

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>/', ArticleDetails.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]


	## Function based views
    # path('article/', article_list),
    # path('detail/<int:pk>/', article_detail),
