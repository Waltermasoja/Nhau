from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class HomePageViewTests(SimpleTestCase):
    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def  test_view_url_by_name(self):
        response = self.client.get(reverse('home')) 
        self.assertEqual(response.status_code,200) 

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home')) 
        self.assertEqual(response.status_code,200)  
        self.assertTemplateUsed(response,'home.html')

class signUpTests(TestCase):
    username = 'walterf'
    email = 'walterfmasoja@gmail.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code,200)

    def test_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'registration/signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.name
        )
        self.assertEqual(get_user_model.objects.all().count(),1)
        self.assertEqual(get_user_model.objects.all()
                         [0].username,self.username)
        