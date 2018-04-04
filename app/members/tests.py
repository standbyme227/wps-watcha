from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class EmailAccountsTest(TestCase):
    def setup(self):
        self.test_user = User.objects.create_user('20djshin@naver.com', '네이버계정', 'testpassword')
        pass
