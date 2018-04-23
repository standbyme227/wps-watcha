import os

from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.management import BaseCommand
from django.db import connection

from utils.file import get_buffer_ext

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user_data = [
            {
                'email': 'tang@test.com',
                'nickname': '탱구',
                'password': 'abc123456789',
            },
            {
                'email': 'nana@test.com',
                'nickname': '나나',
                'password': 'abc123456789',
            },
            {
                'email': 'omg@test.com',
                'nickname': 'oh my girl',
                'password': 'abc123456789',
            },
        ]
        for user in user_data:
            if not User.objects.filter(email=user['email']).exists():
                user = User.objects.create_user(
                    email=user['email'],
                    nickname=user['nickname'],
                    password=user['password'],
                )
                # if user.img_profile:
                #     user.img_profile.delete()
                # img_dir = '/home/djshin2000/Downloads/img_profile'
                # file_path = os.path.join(img_dir, 'taeyeon_1.jpg')
                # with open(file_path, 'r') as f:
                #     contents = f.read()
                #     file_name = 'user_{user_id}.{ext}'.format(
                #         user_id=user.id,
                #         ext=get_buffer_ext(contents)
                #     )
                #     user.img_profile.save(file_name, File(contents))
        print('connection.queries: ', len(connection.queries))
        self.stdout.write(self.style.SUCCESS('Success: setdata_user command'))
