from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(blank=True,null=True,max_length=30, unique=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    teamA = models.ForeignKey(
                'Team',
                on_delete=models.CASCADE,
                related_name='matchsA',
                null=True,
            )
    teamB = models.ForeignKey(
            'Team',
            on_delete=models.CASCADE,
            related_name='matchsB',
            null=True,
        )
    credits = models.IntegerField(default=5000)
    time = models.DateTimeField()

    def __str__(self):
        return "%s - %s"%(self.teamA, self.teamB)

class Overs(models.Model):
    over = models.IntegerField() 

class Balls(models.Model):
    NOUT = 'Not OUT'
    OUT = 'OUT'
    CHOICES = [
        (NOUT, NOUT),
        (OUT, OUT)
    ]
    over = models.ForeignKey(
                'Overs',
                on_delete=models.CASCADE,
                related_name='balls',
                null=True,
            )
    run = models.IntegerField(default=0)
    player = models.ForeignKey(
                'user_administration.Player',
                on_delete=models.CASCADE,
                related_name='balls',
                null=True,
            )
    ball_status = models.CharField(
        max_length=10,
        choices=CHOICES,
        default=NOUT,
    )
