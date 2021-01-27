from django.urls import path
# from .views import tweet_list 
# from .views import TweetAPIView,TweetDetails,
from django.views.decorators.csrf import csrf_exempt

from .views import GenericAPIView, RegisterApi, UserAPIView, FollowAPIView, uploadProfileImageAPI, LikeAPIView
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        # path('tweets/',TweetAPIView.as_view()),
        # path('tweet/<int:pk>/',TweetDetails.as_view()),
        path('generic/tweet/<int:pk>/', csrf_exempt(GenericAPIView.as_view())),
        path('generic/tweet/', csrf_exempt(GenericAPIView.as_view())),
        path('generic/register/', csrf_exempt(RegisterApi.as_view())),
        path('generic/token/', csrf_exempt(jwt_views.TokenObtainPairView.as_view()), name='token_obtain_pair'),
        path('generic/token/refresh/', csrf_exempt(jwt_views.TokenRefreshView.as_view()), name='token_refresh'),
        path('generic/follow/', csrf_exempt(FollowAPIView.as_view())),
        path('generic/user/', csrf_exempt(UserAPIView.as_view())),
        path('generic/upload_profile/', csrf_exempt(uploadProfileImageAPI.as_view())),
        path('generic/like/<int:pk>/', csrf_exempt(LikeAPIView.as_view()))
        # path('tweets/', tweet_list ),
        # path('tweet/<int:pk>/',tweetdetails)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
