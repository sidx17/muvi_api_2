from django.db import models



class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=70)
   # def __str__(self):
    #    return str({"id":self.id, "name" :self.name})



class Video(models.Model):
    user_id=models.ForeignKey("User",related_name='user_id',on_delete=models.CASCADE)
    watch_duration=models.IntegerField()
    bandwidth_usage=models.IntegerField()

    def __str__(self):
         return str({'watch_duration' :self.watch_duration ,'bandwidth_usage' :self.bandwidth_usage})



    