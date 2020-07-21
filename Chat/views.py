from django.shortcuts import render
from .models import Messages
from django.views import View


class ChatView(View):

    def get(self, request):
        messages = Messages.objects.order_by('-pub_date')
        context = {
            'messages': messages
        }
        return render(request, 'Chat/index.html', context)

    def post(self, request):
        message = Messages(text_message=request.POST['message'])
        message.save()
        messages = Messages.objects.order_by('-pub_date')
        context = {
            'messages': messages
        }
        return render(request, 'Chat/index.html', context)