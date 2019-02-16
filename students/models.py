from django.db import models

class  Grades(models.Model):
    gname = models.CharField(max_length=50)
    gdate = models.DateTimeField()
    gboynum = models.IntegerField()
    ggirlnum = models.IntegerField()
    isDelete =models.BooleanField(default=False)
    def __str__(self):
        return (self.gname)

class Students(models.Model):
    sname = models.CharField(max_length=60)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontent = models.CharField(max_length=200)
    isDelete = models.BooleanField(default=False)
    #关联外键：
    sgrade = models.ForeignKey('Grades')
    def __str__(self):
        return (self.gname)