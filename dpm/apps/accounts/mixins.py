from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

class UserIsOwnerMixin(LoginRequiredMixin):
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404
        return obj
