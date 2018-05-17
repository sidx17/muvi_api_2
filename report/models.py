from django.db import models



class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=70)
    def __str__(self):
        return self.name



class Video(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    watch_duration=models.IntegerField()
    bandwidth_usage=models.IntegerField()



    