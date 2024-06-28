
from django.contrib import admin
from django.urls import path
from  app.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login_page' ),
    path('teacher_login/', teacher_Lpage, name='teacher_Lpage'),
    path('administrator_login/', administrator_Lpage, name='administrator_Lpage'),
    path('home/', home_page, name='home_page'),
    path('course/', course_page, name='course_page'),
    path('select/', select_page, name='select_page'),
    path('Register/', register_page, name='register_page'),
    path('chooseyearbba/', choose_year_bba_page, name='choose_year_bba_page'),
    path('chooseyearbit/', choose_year_bit_page, name='choose_year_bit_page'),
    # path('year1bba/', year_1_bba_page, name='year_1_bba_page'),
    path('year2bba/', year_2_bba_page, name='year_2_bba_page'),
    path('year3bba/', year_3_bba_page, name='year_3_bba_page'),
    path('year4bba/', year_4_bba_page, name='year_4_bba_page'),
    # path('year1bit/', year_1_bit_page, name='year_1_bit_page'),
    path('year2bit/', year_2_bit_page, name='year_2_bit_page'),
    path('year3bit/', year_3_bit_page, name='year_3_bit_page'),
    path('delete-register/<int:id>/' , delete_register, name="delete_register"),
    path('update-register/<int:id>/' , update_register, name="update_register"),
    path('year1bba/', display_bba_students, name='display_bba_students'),
    path('year1bit/', display_bit_students, name='display_bit_students'),
    path('year1bba/', display_bba_students, name='display_bba_students'),
    path('calculate-attendance/', calculate_attendance, name='calculate_attendance'),
]
