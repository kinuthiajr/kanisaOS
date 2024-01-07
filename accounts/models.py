from django.db import models



# member model

class MemberProfile(models.Model):
    name = models.CharField(max_length = 100,blank=False,null=False)
    phone_number = models.CharField(max_length=12,blank=True,null=True)
    baptism_date = models.DateField(blank=True,null=True)
    confirmation_date = models.DateField(blank=True,null=True)
    spouse = models.OneToOneField('Spouse', on_delete=models.CASCADE, blank=True, null=True)


    # marital choices
    MARITAL_STATUS_CHOICES =[
        ('married','Married'),
        ('single','Single'),
        ('windowed','Windowed'),
        ('divorced','Divorced'),
        ('others','Others'),
    ]

    marital_status = models.CharField(
        max_length=10,
        choices = MARITAL_STATUS_CHOICES,
        default='single',
        null=True,
        blank=True,)

    # communicant choices
    COMMUNICANT = [
        ('yes','Yes'),
        ('no','No'),
    ]

    communicant = models.CharField(
        max_length=4,
        choices=COMMUNICANT,
        default='yes',
        blank=True,
        null=True
    )
    
    # service attends
    SERVICE_ATTEND =[
        ('kikuyu','Kikuyu'),
        ('english','English'),
    ]

    service_attend =models.CharField(
        max_length=7,
        choices=SERVICE_ATTEND,
        default='kikuyu',
        blank=True,
        null=True,
    )

    # cell group choice
    CELL_GROUP = [
        ('bethlehem','Bethlehem'),
        ('judea','Judea'),
        ('jerusalem','Jerusalem'),
    ]

    cell_group = models.CharField(
        max_length=9,
        choices = CELL_GROUP,
        default='judea',
        blank=True,
        null=True,
    )  

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# Spouse model
class Spouse(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    baptism_date = models.DateField(blank=True,null=True)
    confirmation_date = models.DateField(blank=True,null=True)
    phone_number = models.CharField(max_length = 15,blank=True,null=True)
    marital_status = models.CharField(max_length = 10,choices = MemberProfile.MARITAL_STATUS_CHOICES,blank=True,null=True,default = 'single')
    cell_group = models.CharField(max_length = 9, choices=MemberProfile.CELL_GROUP,blank=True,null=True)

    communicant = models.CharField(

        max_length=4,
        choices = MemberProfile.COMMUNICANT,
        default = 'yes',
        blank=True,
        null=True,
    )
    service_attend = models.CharField(
        max_length=7,
        choices=MemberProfile.SERVICE_ATTEND,
        default='kikuyu',
        blank=True,
        null=True,
    )
    
    #created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'No Spouse'

class Children(models.Model):
    member_profile = models.ForeignKey(MemberProfile,on_delete=models.CASCADE, related_name='children')
    date_of_birth = models.DateField(blank=True,null=True)
    name = models.CharField(max_length=20,blank=True,null=True)
    baptism_date = models.DateField(blank=True,null=True)
    confirmation_date = models.DateField(blank=True,null=True)
    
    #deptartment choices
    DEPT=[
        ('sunday sch.','Sunday Sch'),
        ('teens','Teens')
    ]

    dept = models.CharField(
        max_length=11,choices=DEPT,blank=True,null=True
    )

    def __str__(self):
        return self.name
