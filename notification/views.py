from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from notification.models import Notification
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class NotificationView(LoginRequiredMixin, TemplateView):
    
    def get(self, request, user_id):
        notifications = Notification.objects.filter(receiver__id=user_id)
        received_notification = []
        for notified in notifications:
            if not notified.viewed_at:
                received_notification.append(notified.tweet)
            notified.viewed_at = timezone.now()
            notified.save()
        return render(request, "notification.html",{"received_notification": received_notification[::-1]})
