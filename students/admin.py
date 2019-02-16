from django.contrib import admin
from .models import Grades,Students

#直接添加学生信息于班级添加页面中
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]   #直接添加学生信息于班级添加页面中
    list_filter = ['gname']  #关键字分类显示
    search_fields = ['gname']  #搜索关键字类搜索
    list_per_page = 1    #一个页面最多显示几个
    fields = ['gname','gboynum','ggirlnum', 'gdate','isDelete']  # 修改添加页修改各项顺序
    list_display = ['pk','gname','gdate','gboynum','ggirlnum','isDelete']
#admin.site.register(Grades,GradesAdmin)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    gender.short_description = '性别'
    list_display = ['pk','sname',gender,'sage','scontent','isDelete']
#admin.site.register(Students,StudentsAdmin)
