from django.urls import path
from . import views 
from .views import FileUploadDeleteView

app_name = 'tokai'
urlpatterns = [
    path('',views.TokaiView, name='index'),
    path('tosimitu/',views.Tosimitu,name='tosimitu'),
    path('tetuya/',views.Tetuya,name='tetuya'),
    path('sibayu/',views.Sibayu,name='sibayu'),
    path('musimegane/',views.Musimegane,name='musimegane'),
    path('yumemaru/',views.Yumemaru,name='yumemaru'),
    path('ryo/',views.Ryo,name='ryo'),
    path('tokaivideo_site/',views.Video.as_view(),name='video'),
    path('mypage/',views.Mypage.as_view(),name='mypage'),
    path('upload/',views.UploadView.as_view(), name='upload'),
    path('delete/<int:pk>/',FileUploadDeleteView.as_view(), name='delete_fileupload'),

]
