from django.urls import path
from . import views,Admin_views,Hod_views,Staff_views,Student_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # login urls
    path('',views.Login,name='Login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='doLogout'),

    # profile.urls
    path('profile',views.profile,name='profile'),
    path('profileupdate',views.profileup,name='profileup'),

    # Admin urls
    path('Admin/Home',Admin_views.AdminHome,name='AdminHome'),
    path('Admin/Add/Department',Admin_views.Adddepartment,name='Adddepartment'),
    path('Admin/View/Department',Admin_views.Viewdepartment,name='Viewdepartment'),
    path('Admin/Edit/Department/<int:id>',Admin_views.Editdepartment,name='Editdepartment'),
    path('Admin/Update/Department/',Admin_views.Updatedepartment,name='Updatedepartment'),
    path('Admin/Delete/Department/<int:id>',Admin_views.Deletedepartment,name='Deletedepartment'),
    path('Admin/Add/Hod',Admin_views.AddHod,name='AddHod'),
    path('Admin/View/Hod',Admin_views.ViewHod,name='ViewHod'),
    path('Admin/Edit/Hod/<int:id>',Admin_views.EditHod,name='EditHod'),
    path('Admin/Update/Hod',Admin_views.UpdateHod,name='UpdateHod'),
    path('Admin/Delete/Hod/<int:id>',Admin_views.DeleteHod,name='DeleteHod'),

    #Hod urls
    path('Hod/Home', Hod_views.HodHome,name='HodHome'),
    path('Hod/Add/Course', Hod_views.AddCourse,name='AddCourse'),
    path('Hod/View/Course', Hod_views.ViewCourse,name='ViewCourse'),
    path('Hod/Edit/Course/<int:id>', Hod_views.EditCourse,name='EditCourse'),
    path('Hod/Update/Course/', Hod_views.UpdateCourse,name='UpdateCourse'),
    path('Hod/Delete/Course/<int:id>', Hod_views.DeleteCourse,name='DeleteCourse'),
    path('Hod/Add/Staff', Hod_views.AddStaff,name='AddStaff'),
    path('Hod/View/Staff', Hod_views.ViewStaff,name='ViewStaff'),
    path('Hod/Edit/Staff/<int:id>', Hod_views.EditStaff,name='EditStaff'),
    path('Hod/Update/Staff', Hod_views.UpdateStaff,name='UpdateStaff'),
    path('Hod/Delete/Staff/<int:id>', Hod_views.DeleteStaff,name='DeleteStaff'),
    path('Hod/Add/Student', Hod_views.AddStudent,name='AddStudent'),
    path('Hod/View/Student', Hod_views.ViewStudent,name='ViewStudent'),
    path('Hod/Edit/Student/<int:id>', Hod_views.EditStudent,name='EditStudent'),
    path('Hod/Update/Student', Hod_views.UpdateStudent,name='UpdateStudent'),
    path('Hod/Delete/Student/<int:id>', Hod_views.DeleteStudent,name='DeleteStudent'),
    path('Hod/Add/Subject', Hod_views.AddSubject,name='AddSubject'),
    path('Hod/View/Subject', Hod_views.ViewSubject,name='ViewSubject'),

    # Staff urls
    path('Staff/Home', Staff_views.StaffHome,name='StaffHome'),
    path('Staff/Take/Attendence', Staff_views.TakeAttendence,name='TakeAttendence'),
    path('Staff/View/Attendence', Staff_views.ViewAttendence,name='ViewAttendence'),
    path('Staff/Save/Attendence', Staff_views.SaveAttendence,name='SaveAttendence'),
    path('Staff/Attendence/Report', Staff_views.AttendenceReport,name='AttendenceReport'),
    path('Staff/View/Attendence/Report', Staff_views.ViewAttendenceReport,name='ViewAttendenceReport'),
    path('Staff/All/Attendence', Staff_views.AllAttendence,name='AllAttendence'),
    path('Staff/All/Attendence/Report', Staff_views.AllAttendenceReport,name='AllAttendenceReport'),


    #student urls
    path('Student/Home', Student_views.StudentHome,name='StudentHome'),
    path('Student/View/Attendence', Student_views.StudentViewAttendence,name='StudentViewAttendence'),
    path('Student/Details/Attendence', Student_views.StudentDetailedAttendence,name='StudentDetailedAttendence'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
