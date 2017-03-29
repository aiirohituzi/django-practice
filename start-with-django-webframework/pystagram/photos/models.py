from django.db import models

class Photo(models.Model):
    # id = '개별 사진을 구분하는 색인값'
    image = models.ImageField()                             # '원본 사진 파일'
    filtered_image = models.ImageField()                    #'필터 적용된 사진 파일'
    content = models.TextField(max_length=500)              #'사진에 대한 설명문'
    created_at = models.DateTimeField(auto_now_add=True)    #'생성일시'