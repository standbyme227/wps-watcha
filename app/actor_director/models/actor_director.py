from PIL import Image
from django.core.files import File
from django.db import models
from utils.file import *
__all__ = (
    'Member',
)


class Member(models.Model):
    actor_director_id = models.CharField('감독/배우 아이디', max_length=10, unique=True, null=True, blank=True)
    # 네이버 영화에서 사용되는 actor와 director의 id이다. 이걸이용해서 중복된 인물이 저장되지 않도록 unique=True 옵션을 걸어두었다.
    name = models.CharField('이름', max_length=50)
    # 보다시피 이름이다.
    real_name = models.CharField('본명', max_length=50, null=True, blank=True)
    # 이건 본명인데, 사실상 본명으로 사용한다기 보다는 영어이름 Full name용으로 보는게 맞다.(이름을 잘못지었다.)
    img_profile = models.ImageField(upload_to='members', blank=True)
    # 프로필 사진이 저장되는 곳이다.
    img_profile_x3 = models.ImageField(upload_to='members/ios', blank=True)
    img_profile_x2 = models.ImageField(upload_to='members/ios', blank=True)
    img_profile_x1 = models.ImageField(upload_to='members/ios', blank=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # models.Model 안에 있는 save라는 메소드가 있는데 그걸 override해서 저장될때 이미지의 resizing 작업이 동시에 이뤄지도록 했다.
        self._save_resizing_process()
        # 저장 전에 resizing과정을 먼저하고
        super().save(*args, **kwargs)
        # super를 이용해서 save함수를 다시 이용한다.

    def _save_resizing_process(self):
        # IOS와 Frontend의 요청 이미지사이즈가 달라서 resizing 작업을 해야했다.
        if self.img_profile:
            # img_profile이 저장되는 시점이니, 네이버영화의 프로필에 image가 있다면 Member의 모델에도 img_profile이 있는거고
            # 그 이미지 프로필이 있다면 resizing을 실행해야한다.
            full_name = self.img_profile.name.rsplit('/')[-1]
            # root를 제외한 img파일의 이름만을 가져온다.
            full_name_split = full_name.rsplit('.', maxsplit=1)
            # 위에서 얻어온 fullname을 잘라낸다. 파일명과 확장자로 나누기위해서...

            temp_file = BytesIO()
            # BytesIO를 이용해서 임시파일을 만들었다.
            temp_file.write(self.img_profile.read())
            # img_profile의 정보를 임시파일에 씌운다.
            temp_file.seek(0)
            mime_info = magic.from_buffer(temp_file.read(), mime=True)
            # 확장자를 가져오기위한 일련의 방법인데...아직 확실히는 모르겠다.
            # 일단 mime이란? 파일을 문자로 변환해서 이메일 시스템을 통해 전달하기위 방법이었는데
            # 지금은 웹상의 이동에서 많이 쓰인다.
            # 이 방법으로 파일의 형식을 알 수 있다고 한다.
            temp_file.seek(0)

            name = full_name_split[0]
            ext = mime_info.split('/')[-1]
            # 위에서 얻은 mime_info로 뒤의 확장자를 앋은거 같다.
            # 근데 궁금한 점은 왜 full_name에서 split을 하지 않았냐 하는 점이다.
            # 그렇게 하면 안됐을까?
            # 나는 왜 그렇게 하지 않았을까??

            im = Image.open(self.img_profile)
            # 여기서부터는 파일 리사이징 작업이다. 일단 파일을 열어서 im에 지정해둔다음

            x3 = im.resize((210, 306))
            # resize함수를 이용해서 크기를 줄이고 x3에 넣는다.
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



