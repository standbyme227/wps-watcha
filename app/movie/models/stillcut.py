import os

from PIL import Image
from django.core.files import File
from django.db import models
from utils.file import *
from ..models import Movie

__all__ = (
    'StillCut',
)


class StillCut(models.Model):
    # stillcut 추가할 모델 OneToMany
    movie = models.ForeignKey(Movie, related_name='still_cuts', verbose_name='영화', on_delete=models.CASCADE, blank=True,
                              null=True)
    still_img = models.ImageField('스틸 이미지', upload_to='still_cut', blank=True)
    still_img_x3 = models.ImageField('아이폰용 스틸 이미지', upload_to='still_cut/ios', blank=True)
    # still_img_x2 = models.ImageField('아이폰용 스틸 이미지', upload_to='still_cut/ios', blank=True)
    # still_img_x1 = models.ImageField('아이폰용 스틸 이미지', upload_to='still_cut/ios', blank=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def image_path(instance, filename):
        return os.path.join('some_dir', str(instance.some_identifier), 'filename.ext')

    def __str__(self):
        return f'{self.id} - {self.movie.title_ko} - stillcut: {self.still_img}'

    def save(self, *args, **kwargs):
        self._save_resizing_process()
        super().save(*args, **kwargs)

    def _save_resizing_process(self):
        if self.still_img:
            full_name = self.still_img.name.rsplit('/')[-1]
            full_name_split = full_name.rsplit('.', maxsplit=1)

            temp_file = BytesIO()
            temp_file.write(self.still_img.read())
            temp_file.seek(0)
            mime_info = magic.from_buffer(temp_file.read(), mime=True)
            temp_file.seek(0)

            name = full_name_split[0]
            ext = mime_info.split('/')[-1]

            im = Image.open(self.still_img)

            x3 = im.resize((1125, 849))
            temp_file = BytesIO()
            x3.save(temp_file, ext)
            self.still_img_x3.save(f'{name}_x3.{ext}', File(temp_file), save=False)

            # x2 = im.resize((750, 566))
            # temp_file = BytesIO()
            # x2.save(temp_file, ext)
            # self.still_img_x2.save(f'{name}_x2.{ext}', File(temp_file), save=False)
            #
            # x1 = im.resize((375, 283))
            # temp_file = BytesIO()
            # x3.save(temp_file, ext)
            # self.still_img_x1.save(f'{name}_x1.{ext}', File(temp_file), save=False)

        else:
            self.still_img_x3.delete(save=False) \
            # and self.still_img_x1.delete(save=False) \
            # and self.still_img_x2.delete(save=False)
