from django.db import models

# Create your models here.
class UserInput(models.Model):
    userID = models.CharField(max_length=40)
    text = models.TextField()
    typingData = models.TextField()
    dateOfData = models.DateTimeField()

    def __str__(self):
        return self.userID + ":" + self.dateOfData.__str__() + ':' + self.typingData