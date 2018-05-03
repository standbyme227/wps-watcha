import magic
from PIL import Image
from django.core.files import File
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from io import BytesIO


class UserManager(BaseUserManager):
    # 유저매니저로 User의 쿼리셋 objects로 통해서 들어갈 수 있다.
    def create_user(self, email, nickname, password):
        """
        :param email:
        :param nickname:
        :param password:
        :return: email, nickname, password를 갖는 생성된 user가 반환된다.
        """
        # UserManager 클래스안에 create_user 메소드를 선언했다.
        if not email:
            # email이 없으면
            # raise로 ValueError를 일으킨다.
            raise ValueError('Users must have an email address')
        # ValueError 가 뭘하는지 아직 정확히는 모르겠다.

        user = self.model(
            # self.model이라면 UserManager의 model을 지칭하는 것 같고 그건 BaseUserManager이다.
            # 처음에는 User를 지칭하는 줄 알았다.
            # 근데 user를 생성하는데 왜 BaseUserManager를 이용해서 채워 넣는것일까???
            email=self.normalize_email(email),
            # BaseUserManager를 이용해서 email을 normalize(정규화?) 시킨다.
            nickname=nickname
            # nickname엔 nickname을 넣는다.
        )
        user.set_password(password)
        # set_password라는 AbstractBaseUser의 메소드로 password를 규정한다.
        user.save(using=self._db)
        # 그렇게 구성되어진 user를 저장하는데 using이라는 옵션을 왜 줬는지는 확실치 않다.
        return user

    def create_superuser(self, email, nickname, password):
        """

        :param email: email형식으로 입력한다.
        :param nickname: nickname으로 지정할 str을 입력한다.
        :param password: 비밀번호를 설정한다.
        :return: email, nickname, password를 갖는 생성된 superuser가 반환된다.
        """
        user = self.create_user(
            # 메소드인 create_user를 이용해서 각 parameter에 맞는 형식으로 값을 넣는다.
            email=email,
            nickname=nickname,
            password=password
        )
        user.is_staff = True
        # 스태프와 슈퍼유저에 True값을 준다.
        user.is_superuser = True
        user.save(using=self._db)
        # 구성된 user를 저장한다.
        return user


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        help_text=_('Required. 255 characters or fewer.'),
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    nickname = models.CharField(verbose_name='nickname', max_length=20, blank=False, null=False)
    img_profile = models.ImageField(upload_to='user', blank=True)
    # img_profile_thumbnail = models.ImageField(upload_to='user', blank=True)

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