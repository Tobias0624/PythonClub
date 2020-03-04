from django.db import models
from django.contrib.auth.models import User
# Create your models here.

objects = models.Manager()



class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255,null=True, blank=True)
    meetingdate=models.DateField()
    meetingtime=models.CharField(max_length=255, null=True, blank=True)
    meetinglocation=models.CharField(max_length=255,null=True, blank=True)
    meetingAgenda=models.TextField()


    def __str__(self):
        return self.meetingtitle
    

    class Meta:
        db_table='Meeting'
        verbose_name_plural='Meetings'

class MeetingMinutes(models.Model):
    meetingID=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    meetingAttendence=models.ManyToManyField(User)
    meetingtext=models.TextField()

    def __str__(self):
        return self.meetingtext
    class Meta:
        db_table='meetingMinutes'


class Resource(models.Model):
      resourcename=models.CharField(max_length=255, null=True, blank=True)
      resourcetype=models.CharField(max_length=255, null=True, blank=True)
      resourceURL=models.URLField(null= True, blank=True)
      resourcedateEnter=models.TextField()
      userID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
      resourceDescription=models.CharField(max_length=255, null=True, blank=True)
      
      
      def __str__(self):
          return self.resourcename

      class Meta:
         db_table='resource'
         verbose_name_plural='resources'



class Event(models.Model):
    eventTitle=models.CharField(max_length=255, null=True, blank=True)
    eventLocation=models.CharField(max_length=255, null=True, blank=True)
    eventDate=models.DateField()
    eventTime=models.CharField(max_length=255, null=True, blank=True)
    eventDescription=models.CharField(max_length=255, null=True, blank=True)
    userID=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.eventTitle

    class Meta:
        db_table= 'event'
        verbose_name_plural='events'