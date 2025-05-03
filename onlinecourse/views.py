from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.
def course_list_view(request):
    context = {}
    if request.method == "GET":
        top_ten_courses = Course.objects.order_by('total_enrollment')[:10]
        # context = {'course_list': courses}
        # Append the course list as an entry of context dict
        context['course_list'] = top_ten_courses
        return render(request, 'onlinecourse/course_list.html', context)

def enroll(request, course_id):
    if request.method == "POST":
        # First try to read the course object / record
        # If could be found, raise a 404 exception
        course = get_object_or_404(Course, pk=course_id) # Same as Course.objects.get(pk=course_id)
        # Increase the enrollment by 1
        course.total_enrollment += 1
        course.save() #Save the record with the updated value
        # Return a HTTP response redirecting user to course list view
        # As if you never left the page
        # return HttpResponseRedirect(reverse(viewname='onlinecourse:course_list_view'))
        return HttpResponseRedirect(reverse(viewname='onlinecourse:detail', args=(course.id,)))
    
def course_details(request, course_id):
    context = {}
    if request.method == 'GET':
        this_course = get_object_or_404(Course, pk=course_id)
        context['course'] = this_course
        return render(request, 'onlinecourse/course_detail.html', context)