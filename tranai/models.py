from django.db import models

class Document(models.Model):
  dod = models.DateTimeField('Date of Delivery')
  tod = models.CharField('Time of Day', max_length=60)
  dow = models.CharField('Day of Week', max_length=60)
  title = models.CharField('Document Title', max_length=120)
  descriptor = models.CharField('Descriptor', max_length=120)

  def __str__(self):
    return self.title


class User(models.Model):
  email = models.EmailField('Email')
  username = models.CharField('Username', max_length=30)
  admin = models.BooleanField('Admin', default=False)
  cur_assign_id = models.IntegerField('current Assignment ID', blank=True, null=True)

  def __str__(self):
    return self.username + ' ' + self.email


class Translation(models.Model):
  lan = models.CharField('lan', max_length=3)
  tran_title = models.CharField('tran_title', max_length=300)
  # descrip = models.CharField('descrip', max_length=300)
  descrip = models.TextField('descrip', max_length=300)
  blkc = models.CharField('blkc', max_length=300)
  subc = models.CharField('subc', max_length=300)
  senc = models.CharField('senc', max_length=300)
  xcrip = models.CharField('xcrip', max_length=1)
  li = models.CharField('li', max_length=300)
  pubdate = models.CharField('pubdate', max_length=300)
  version = models.CharField('version', max_length=300)
  document = models.ForeignKey(Document, blank=True, null=True, on_delete=models.CASCADE)
  # Translation.Document.title?
  # email = models.EmailField('email')
  # username = models.CharField('username', max_length=300)
  # url = models.URLField('url',max_length=300)
  # admin = 
  # cur_assign_id = 

  def __str__(self):
    return self.tran_title


# class Task(models.Model):
#   role =
#   attendees = models.ManyToManyField(User, blank=True)

#   def __str__(self):
#     return self.role