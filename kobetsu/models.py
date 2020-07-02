from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200, null=True, blank=True)
    ticket_number = models.CharField(max_length=50, null=True, blank=True)
    admission_number = models.IntegerField(null=True, blank=True)
    choice_member = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return '<Participant:id=' + str(self.id) + ',' + \
            self.name + '(' + str(self.ticket_number) + ')>'
