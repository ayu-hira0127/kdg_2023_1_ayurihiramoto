
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import FileUpload
from .form import UploadForm
from django.views.generic import CreateView,ListView
# from .models import Tokai
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
import logging
# from django.views import View




class UploadView(LoginRequiredMixin,CreateView):
    template_name = 'tokai/create.html'
    model = FileUpload
    fields = ('files',)
    success_url = reverse_lazy('tokai:mypage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    # def some_method(self):
    #     # user_id 列にアクセスする例
    #     upload_instance = FileUpload.objects.get(pk=1)  # 適切な条件を指定して取得
    #     user_id_value = upload_instance.user_id
    


def TokaiView (request):
    return render(request, 'tokai/index.html',)

def Tosimitu(request):
    return render(request,'tokai/Tosimitu.html')

def Tetuya(request):
    return render(request,'tokai/Tetuya.html')

def Sibayu(request):
    return render(request,'tokai/Sibayu.html')

def Musimegane(request):
    return render(request,'tokai/Musimegane.html')

def Yumemaru(request):
    return render(request,'tokai/Yumemaru.html')

def Ryo(request):
    return render(request,'tokai/Ryo.html')


class Video(ListView):
    template_name='tokai/video_site.html'
    model = FileUpload
    context_object_name = 'videos'  # テンプレート内で使用する変数名

    def get_queryset(self):
        return FileUpload.objects.all()

class Mypage(LoginRequiredMixin,ListView):
    template_name='tokai/mypage.html'
    model = FileUpload
    context_object_name = 'file_list'

    

def get(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info("User: %s", request.user)
        return super().get(request, *args, **kwargs)
def get_queryset(self):
        queryset = FileUpload.objects.filter(user=self.request.user)
        logger = logging.getLogger(__name__)
        logger.info("Queryset: %s", queryset)
        return queryset








