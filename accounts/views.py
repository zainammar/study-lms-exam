from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class LogoutGetView(LogoutView):
    # Redirect users to quiz list after logout
    next_page = reverse_lazy('quiz_list')
    http_method_names = ['get', 'post']  # allow GET and POST
