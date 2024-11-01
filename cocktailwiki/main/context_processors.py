from django.conf import settings



def moderator_status(request):
    is_moderator = request.user.groups.filter(name='Administrator').exists() if request.user.is_authenticated else False
    return {'is_moderator': is_moderator}