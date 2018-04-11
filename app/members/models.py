import magic
from PIL import Image
from django.core.files import File
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from io import BytesIO


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email=email,
            nickname=nickname,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        help_text=_('Required. 255 characters or fewer.'),
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    nickname = models.CharField(verbose_name='nickname', max_length=20, blank=False, null=False, unique=True)
    img_profile = models.ImageField(upload_to='user', blank=True)
    img_profile_thumbnail = models.ImageField(upload_to='user', blank=True)

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        null=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.email}({self.nickname})'

    def save(self, *args, **kwargs):
        self._save_thumbnail_process()
        super().save(*args, **kwargs)

    def _save_thumbnail_process(self):

        if self.img_profile:
            # 이미지파일의 이름과 확장자를 가져옴
            full_name = self.img_profile.name.rsplit('/')[-1]
            full_name_split = full_name.rsplit('.', maxsplit=1)

            temp_file = BytesIO()
            temp_file.write(self.img_profile.read())
            temp_file.seek(0)
            mime_info = magic.from_buffer(temp_file.read(), mime=True)
            temp_file.seek(0)

            name = full_name_split[0]
            ext = mime_info.split('/')[-1]

            # Pillow를 사용해 이미지 파일 로드
            im = Image.open(self.img_profile)
            # 썸네일 형태로 데이터 변경
            im.thumbnail((200, 200))

            # 썸네일 이미지 데이터를 가지고 있을 임시 메모리 파일 생성
            temp_file = BytesIO()
            # 임시 메모리 파일에 Pillow인스턴스의 내용을 기록
            im.save(temp_file, ext)
            # 임시 메모리파일을 Django의 File로 한번 감싸 썸네일 필드에 저장
            self.img_profile_thumbnail.save(f'{name}_thumbnail.{ext}', File(temp_file), save=False)
        else:
            self.img_profile_thumbnail.delete(save=False)
