from django.db      import models
from room.models    import Branch


class Inquiry(models.Model) :  
    user              = models.ForeignKey('users.User', on_delete=models.CASCADE)
    branch            = models.ForeignKey(Branch,  on_delete=models.CASCADE)
    inquiry_type      = models.ForeignKey('InquiryType',  on_delete=models.CASCADE)
    title             = models.CharField(max_length = 300)
    content           = models.TextField()
    created_at        = models.DateTimeField(auto_now_add = True)
    
    class Meta : 
        db_table = 'inquires'

class InquiryType(models.Model) :
    inquiry_type       = models.CharField(max_length = 20)

    class Meta:
        db_table = 'inquiry_types'