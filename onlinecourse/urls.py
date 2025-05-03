from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Add path here
    path(route='', view = views.course_list_view, name='course_list_view'),
    path(route= 'course/<int:course_id>/enroll/', view= views.enroll, name='enroll'),
    path(route='course/<int:course_id>/details', view = views.course_details, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

