from django.db import models
import cv2
import numpy as np
import os
import numpy as np
from fingerprintscanner.settings import BASE_DIR
from PIL import Image
import re
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files.base import ContentFile
from . import imagepro


class content(models.Model):
    name = models.CharField(max_length=10)
    addedby = models.ForeignKey('userprofile',on_delete=models.CASCADE,null=False)
    thumbnail = models.ImageField(upload_to="Proccesed Image")
     # global variables for image ,blackPoint, whitePoint
    # global img
    # global whitePoint
    # global blackPoint

    def str(self):
        return self.thumbnail
    
    def save(self, *args, **kwargs):
        super(content,self).save(*args, **kwargs)
        # filename = "%s.jpg" % self.thumbnail.path.split('.')[0]
        # os.rename(self.thumbnail.path,filename + '.jpg')
        # self.thumbnail = filename+'.jpg'
        # self.thumbnail.save()
        # image = Image.open(self.thumbnail)
        # # for PNG images discarding the alpha channel and fill it with some color
        # if image.mode in ('RGBA', 'LA'):
        #     background = Image.new(image.mode[:-1], image.size, '#fff')
        #     background.paste(image, image.split()[-1])
        #     image = background
        # image_io = BytesIO()
        # image.save(image_io, format='JPEG', quality=100)

        # # change the image field value to be the newly modified image value
        # self.thumbnail.save(filename, ContentFile(image_io.getvalue()), save=False)
        # global img
        
        img=Image.open(self.thumbnail.path)

        #width, height = im.size
        # Setting the points for cropped image
        left =140
        top = 220
        right = 330
        bottom = 410

        # Cropped image of above dimension
        # (It will not change orginal image)
        im1 = img.crop((left, top, right, bottom))

        im1.save(self.thumbnail.path)
        imagepro.main(self.thumbnail.path)
        # cropped.show()
        # img = cv2.imread(self.thumbnail.path,0)
        # edge_img = cv2.Canny(img,100,200)

        # s = cv2.Laplacian(img,cv2.CV_64F,ksize=11)
        # cv2.imwrite(self.thumbnail.path,s)

        # img = cv2.imread(self.thumbnail.path,0)
        # img = cv2.medianBlur(img,3)

        # th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15,0)

        # th1 = cv2.medianBlur(th1,3)

        # img2 = cv2.GaussianBlur(img,(3,7),0)
        # s=cv2.Canny(img2, 12, 17)

        # cv2.imwrite(self.thumbnail.path,s)


class userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    mobile = models.PositiveIntegerField(null=True,blank=True)
    admin=models.ForeignKey('adminUser',null=False,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.mobile)

class adminUser(models.Model):
    userid = models.OneToOneField(User,on_delete=models.CASCADE,null=False)
    uniqueCode = models.CharField(max_length=6)

    def __str__(self):
        return self.uniqueCode