# _*_ coding: utf-8 _*_
__author__ = 'htt'
__date__ = '$DATE $TIME'

import xadmin
from .models import Courses ,Lesson ,Video ,CourseResource

class CoursesAdmin(object):

    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','add_time']
    search_fields = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums']
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','add_time']

class LessonAdmin(object):

    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__name','name','add_time']  #过滤器中有外键，需要制定过滤外键中的哪个字段

class VideoAdmin(object):

    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson__name','name','add_time']

class CourseResourceAdmin(object):

    list_display = ['course','name','download','add_time']
    search_fields = ['course','name','download']
    list_filter = ['course','name','download','add_time']

xadmin.site.register(Courses,CoursesAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)