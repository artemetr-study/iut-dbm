from django.urls import path

from . import views

urlpatterns = [
    path('crews/', views.crews),
    path('crew/add/', views.add_crew),
    path('crew/edit/<int:id>', views.edit_crew),
    path('crew/delete/<int:id>', views.delete_crew),

    path('positions/', views.positions),
    path('position/add/', views.add_position),
    path('position/edit/<int:id>', views.edit_position),
    path('position/delete/<int:id>', views.delete_position),

    path('employees/', views.employees),
    path('employee/add/', views.add_employee),
    path('employee/edit/<int:id>', views.edit_employee),
    path('employee/delete/<int:id>', views.delete_employee),

    # path('position/edit/<int:id>', views.edit_position),
    # path('employee/edit/<int:id>', views.edit_employee),
]
