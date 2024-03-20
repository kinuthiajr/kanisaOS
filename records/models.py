from django.db import models

# Create your models here.
class MemberProfile(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)
    phone = models.CharField(max_length=15,null=True,blank=True)
    baptism_date = models.DateField(blank=True,null=True)
    confirmation_date = models.DateField(blank=True,null=True)
    spouse = models.OneToOneField('Spouse',on_delete = models.CASCADE,null=True,blank=True)
    # marital status choices
    MARITAL_STATUS_CHOICES = [
        ('Married','Married'),
        ('Single','Single'),
        ('Windowed','Windowed'),
        ('Divorced','Divorced'),
        ('Others','Others')
    ]
    marital_status = models.CharField(
        max_length=10,
        choices=MARITAL_STATUS_CHOICES,
        default = 'Single',
        null = True,
        blank = True
    )
    # gender choices
    GENDER = [
            ('Male','Male'),
            ('Female','Female')
    ]
    gender = models.CharField(
        max_length = 6,
        null = False,
        blank = False,
        default = 'Male',
        choices = GENDER
    )

    # service attends choices
    SERVICE_ATTENDS =[
        ('English','English'),
        ('Kikuyu','Kikuyu')
    ]
    service_attends =models.CharField(
        max_length = 8,
        null = True,
        blank = True,
        default = 'Kikuyu',
        choices = SERVICE_ATTENDS
    )

    # communicant choices
    COMMUNICANT = [
        ('Yes','Yes'),
        ('No','No')
    ]
    communicant = models.CharField(
        max_length=4,
        choices=COMMUNICANT,
        default = 'Yes',
        null=True,
        blank=True,                               

    )

    # cell grp choices
    CELL_GRPS = [
        ('Judea','Judea'),
        ('Jerusalem','Jerusalem'),
        ('Bethlehem','Bethlehem'),
    ]
    cell_group = models.CharField(
        max_length = 10,
        null = True,
        blank = True,
        default = 'Jerusalem',
        choices = CELL_GRPS
    )

    # dept choices
    DEPT = [
        ('Kama','Kama'),
        ('MoU','MoU'),
        ('Kayo','Kayo'),
        ('Choir','Choir')
    ] 
    department = models.CharField(
        max_length = 6,
        null = True,
        blank = True,
        default = 'Kama',
        choices = DEPT,
    )

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# spouse model
class Spouse(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)
    phone = models.CharField(max_length=15,null=True,blank=True)
    baptism_date = models.DateField(blank=True,null=True)
    confirmation_date = models.DateField(blank=True,null=True)
    marital_status = models.CharField(max_length=10,choices=MemberProfile.MARITAL_STATUS_CHOICES,blank=True,null=True)
    gender = models.CharField(max_length=6,choices = MemberProfile.GENDER,blank=False,null=False)
    service_attends = models.CharField(max_length=8,choices=MemberProfile.SERVICE_ATTENDS,blank=True,null=True)
    communicant = models.CharField(max_length=4,choices=MemberProfile.COMMUNICANT,blank=True,null=True)
    cell_group = models.CharField(max_length=10,choices=MemberProfile.CELL_GRPS,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)

    DEPT = (
        ['MoU','MoU'],['Choir','Choir']
    )

    department = models.CharField(max_length=6,choices=DEPT,blank=True,null=True)

    def __str__(self):
        return self.name


# child model
class Children(models.Model):
    parent = models.ForeignKey(MemberProfile,on_delete=models.CASCADE,related_name='children')
    date_of_birth = models.DateField(blank=True,null=True)
    name = models.CharField(max_length=100,blank=False,null=False)
    baptism_date = models.DateField(blank=True,null=True)
    confirmation_date = models.DateField(blank=True,null=True)

    # dept choices(Not related to MemberProfile)
    DEPT = [
        ('SundaySCH','SundaySCH'),
        ('Teens','Teens')
    ]
    department = models.CharField(
        max_length=10,
        choices=DEPT,
        blank = True,
        null = True,
    )    
    gender = models.CharField(max_length=6,choices=MemberProfile.GENDER,blank=False,null=False)
    communicant = models.CharField(max_length=4,choices=MemberProfile.COMMUNICANT,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name