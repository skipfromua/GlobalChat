from django.shortcuts import render, redirect
from .models import Messages
from django.views import View
from django.http import JsonResponse


class ChatView(View):
    def get(self, request):
        messages = Messages.objects.order_by('-pub_date')
        if request.is_ajax():
            if messages:
                message = Messages.objects.latest('pub_date')
                response = {
                            'id': message.id,
                            'text_message': message.text_message,
                            'pub_date': message.pub_date.strftime("%H:%M:%S")
                            }
                return JsonResponse(response)
        context = {
            'last_message': messages[0].id,
            'messages': messages,
        }
        return render(request, 'Chat/index.html', context)

    def post(self, request):
        message = Messages(text_message=request.POST['message'])
        message.save()
        return redirect('Chat')