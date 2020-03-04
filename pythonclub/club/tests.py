from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, getresource, getmeeting, meetid
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.

class MeetingTest(TestCase):
    def test_string(self):
        meet = Meeting(meetingtitle="BasketBall")
        self.assertEqual(str(meet),  meet.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')


class MeetingMinutesTest(TestCase):
    def test_string(self):
        meetmin = MeetingMinutes(meetingtext="Played basketball")
        self.assertEqual(str(meetmin),  meetmin.meetingtext)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingMinutes')


class ResourceTest(TestCase):
    def test_string(self):
        source = Resource(resourcename="Python")
        self.assertEqual(str(source),  source.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class EventTest(TestCase):
    def test_string(self):
        vents = Event(eventTitle="Place")
        self.assertEqual(str(vents),  vents.eventTitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


class indexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class getresourceTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('source'))
       self.assertEqual(response.status_code, 200)

class getmeetingTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('meeting'))
       self.assertEqual(response.status_code, 200)