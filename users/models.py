from django.db import models

class MdlUser(models.Model):
    id = models.TextField(primary_key=True) # This field type is a guess.
    auth = models.CharField(max_length=20)
    confirmed = models.SmallIntegerField()
    policyagreed = models.SmallIntegerField()
    deleted = models.SmallIntegerField()
    mnethostid = models.TextField() # This field type is a guess.
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    idnumber = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    emailstop = models.SmallIntegerField()
    icq = models.CharField(max_length=15)
    skype = models.CharField(max_length=50)
    yahoo = models.CharField(max_length=50)
    aim = models.CharField(max_length=50)
    msn = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    institution = models.CharField(max_length=40)
    department = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=2)
    lang = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timezone = models.CharField(max_length=100)
    firstaccess = models.TextField() # This field type is a guess.
    lastaccess = models.TextField() # This field type is a guess.
    lastlogin = models.TextField() # This field type is a guess.
    currentlogin = models.TextField() # This field type is a guess.
    lastip = models.CharField(max_length=15)
    secret = models.CharField(max_length=15)
    picture = models.SmallIntegerField()
    url = models.CharField(max_length=255)
    description = models.TextField()
    mailformat = models.SmallIntegerField()
    maildigest = models.SmallIntegerField()
    maildisplay = models.SmallIntegerField()
    htmleditor = models.SmallIntegerField()
    ajax = models.SmallIntegerField()
    autosubscribe = models.SmallIntegerField()
    trackforums = models.SmallIntegerField()
    timemodified = models.TextField() # This field type is a guess.
    trustbitmask = models.TextField() # This field type is a guess.
    imagealt = models.CharField(max_length=255)
    screenreader = models.SmallIntegerField()

    def __unicode__(self):
        return "%s %s" % (self.firstname, self.lastname)

    class Meta:
        db_table = u'mdl_user'

