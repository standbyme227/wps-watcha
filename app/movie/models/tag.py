from django.db import models

__all__ = (
    'Tag',
)


class Tag(models.Model):
    # 검색을 위한 or 정렬을 위한 태그

    tag = models.CharField('태그', max_length=20, unique=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    def __str__(self):
        return self.tag
