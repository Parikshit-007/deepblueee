from django.shortcuts import redirect, render
from django.views import View
from webapp.models import UserProfile
from webapp.models import Video, Summary
class Dashboard(View):
     def get(self, request):
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')
        user_profile = UserProfile.objects.get(id=user_id)
        user = user_profile.user
        videos = Video.objects.filter(user=user)
        summaries = Summary.objects.filter(user=user)
      #  userr=Video.objects.get(id=user_id)
      #  videos = Video.objects.filter(user=user)
       # if not videos.exists():
             #  videos = None

        context = {
            'first_name': user_profile.first_name,
            'email': user_profile.email,
            'username': user_profile.username,
            'videos': videos,
          #  'title': userr.title,
            'summaries': summaries,
        }
        return render(request, 'dashboard.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from webapp.models import Video

class MyVideosView(View):
    def get(self, request):
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')

        user_profile = UserProfile.objects.get(id=user_id)
        user = user_profile.user
        videos = Video.objects.filter(user=user)
        
        if not videos.exists():
            videos = None
        
        context = {
           # 'title': user.title ,
            'videos': videos,
        }
        return render(request, 'storage.html', context)
    
def summary_list(request, video_id):
    summaries = Summary.objects.filter(user=request.user.userprofile, video__id=video_id)
    return render(request, 'summary_list.html', {'summaries': summaries})