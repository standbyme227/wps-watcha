from PIL import Image
from django.core.files import File
from django.db import models
from utils.file import *
__all__ = (
    'Member',
)


class Member(models.Model):
    actor_director_id = models.CharField('감독/배우 아이디', max_length=10, unique=True, null=True, blank=True)
    name = models.CharField('이름', max_length=50)
    real_name = models.CharField('본명', max_length=50, null=True, blank=True)
    img_profile = models.ImageField(upload_to='members', blank=True)
    img_profile_x3 = models.ImageField(upload_to='members/ios', blank=True)
    # img_profile_x2 = models.ImageField(upload_to='members/ios', blank=True)
    # img_profile_x1 = models.ImageField(upload_to='members/ios', blank=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self._save_resizing_process()
        super().save(*args, **kwargs)

    def _save_resizing_process(self):
        if self.img_profile:
            full_name = self.img_profile.name.rsplit('/')[-1]
            full_name_split = full_name.rsplit('.', maxsplit=1)

            temp_file = BytesIO()
            temp_file.write(self.img_profile.read())
            temp_file.seek(0)
            mime_info = magic.from_buffer(temp_file.read(), mime=True)
            temp_file.seek(0)

            name = full_name_split[0]
            ext = mime_info.split('/')[-1]

            im = Image.open(self.img_profile)

            x3 = im.resize((210, 306))
            temp_file = BytesIO()
            x3.save(temp_file, ext)
            self.img_profile_x3.save(f'{name}_x3.{ext}', File(temp_file), save=False)

            # x2 = im.resize((140, 204))
            # temp_file = BytesIO()
            # x2.save(temp_file, ext)
            # self.img_profile_x2.save(f'{name}_x2.{ext}', File(temp_file), save=False)
            #
            # x1 = im.resize((70, 102))
            # temp_file = BytesIO()
            # x1.save(temp_file, ext)
            # self.img_profile_x1.save(f'{name}_x1.{ext}', File(temp_file), save=False)

        else:
            self.img_profile_x3.delete(save=False) \
            # and self.img_profile_x2.delete(save=False) \
            # and self.img_profile_x1.delete(save=False)



