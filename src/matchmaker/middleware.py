from django.contrib import messages
from django.conf import settings
from  django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect

URLS = [reverse(url) for url in settings.SUBSCRIPTION_REQUIRED_URLS]

class CheckMembership():
    def process_request(self,request):
        if request.user.is_authenticated():
            if request.path in URLS:
                role = request.user.userrole
                if str(role) != 'Premium':
                    messages.success(request, 'You need to upgrade your membership to see what')
                    return HttpResponseRedirect('/')
        else:
            messages.error(request,'User is not Logged in')