from django.conf.urls import patterns, url

urlpatterns = patterns('testapp.exam.views',
    url(r'^$', 'index'),
    url(r'^login/$', 'user_login'),
    url(r'^quizzes/$', 'quizlist_user'),
    url(r'^results/$', 'results_user'),
    url(r'^start/$', 'start'),
    url(r'^start/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$', 'start'),
    url(r'^quit/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$', 'quit'),
    url(r'^intro/(?P<questionpaper_id>\d+)/$', 'intro'),
    url(r'^complete/$', 'complete'),
    url(r'^complete/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$',\
            'complete'),
    url(r'^register/$', 'user_register'),
    url(r'^(?P<q_id>\d+)/$', 'question'),
    url(r'^(?P<q_id>\d+)/check/$', 'check'),
    url(r'^(?P<q_id>\d+)/check/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$',\
            'check'),
    url(r'^intro/$', 'start'),
    url(r'^(?P<q_id>\d+)/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$', 'show_question'),

    url(r'^manage/$', 'prof_manage'),
    url(r'^manage/addquestion/$', 'add_question'),
    url(r'^manage/addquestion/(?P<question_id>\d+)/$', 'add_question'),
    url(r'^manage/addquiz/$', 'add_quiz'),
    url(r'^manage/editquiz/$', 'edit_quiz'),
    url(r'^manage/editquestion/$', 'edit_question'),
    url(r'^manage/addquiz/(?P<quiz_id>\d+)/$', 'add_quiz'),
    url(r'^manage/gradeuser/$', 'show_all_users'),
    url(r'^manage/gradeuser/(?P<username>.*)/$', 'grade_user'),
    url(r'^manage/questions/$', 'show_all_questions'),
    url(r'^manage/showquiz/$', 'show_all_quiz'),
    url(r'^manage/monitor/$', 'monitor'),
    url(r'^manage/showquestionpapers/$', 'show_all_questionpapers'),
    url(r'^manage/showquestionpapers/(?P<questionpaper_id>\d+)/$',\
                                                    'show_all_questionpapers'),
    url(r'^manage/monitor/(?P<questionpaper_id>\d+)/$', 'monitor'),
    url(r'^manage/user_data/(?P<username>.*)/$', 'user_data'),
    url(r'^manage/designquestionpaper/$', 'design_questionpaper'),
    url(r'^manage/designquestionpaper/(?P<questionpaper_id>\d+)/$',\
                                                        'design_questionpaper'),
    url(r'^manage/designquestionpaper/automatic/(?P<questionpaper_id>\d+)/$',\
                                                    'automatic_questionpaper'),
    url(r'^manage/designquestionpaper/automatic$', 'automatic_questionpaper'),
    url(r'^manage/designquestionpaper/manual$', 'manual_questionpaper'),
    url(r'^manage/designquestionpaper/manual/(?P<questionpaper_id>\d+)/$',\
                                                        'manual_questionpaper'),
    url(r'^ajax/questionpaper/(?P<query>.+)/$', 'ajax_questionpaper'),
)
