from django.db import models
from django.core.urlresolvers import reverse_lazy

class Photo(models.Model):
    # id = '개별 사진을 구분하는 색인값'
    image = models.ImageField(upload_to='%Y/%m/%d/orig')                # '원본 사진 파일'
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')   #'필터 적용된 사진 파일'
    content = models.TextField(max_length=500, null=True, blank=True)   #'사진에 대한 설명문'
    created_at = models.DateTimeField(auto_now_add=True)                #'생성일시'

    # blank=True : 빈칸을 허용하겠다는 옵션
    # null=True : None 자료형을 허용
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse_lazy('detail', kwargs={'pk': self.pk})
        return url