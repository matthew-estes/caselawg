from django.db import models
from django.urls import reverse

CASESTATUS = (
    ('A', 'Open-Active'),
    ('I', 'Open-Inactive'),
    ('C', 'Closed')
)

CASESTAGE = (
    ('1', 'Intake'),
    ('2', 'Complaint'),
    ('3', 'Pre-Trial Motions/Discovery'),
    ('4', 'Trial Preparation'),
    ('5', 'Trial'),
    ('6', 'Mediation'),
    ('7', 'Arbitration'),
    ('8', 'Settlement'),
    ('9', 'MISC')
)

TASKTYPE = (
    ('1', 'Research'),
    ('2', 'Draft Motion'),
    ('3', 'Draft Correspondence'),
    ('4', 'Hearing'),
    ('5', 'Administrative'),
    ('6', 'Status call'),
    ('7', 'Discovery'),
    ('8', 'Doc Review'),
    ('9', 'MISC')
)

TASKSTATUS = (
    ('O', 'Open'),
    ('C', 'Complete')
)

class Case(models.Model):
    name = models.CharField(max_length=20)
    client = models.CharField(max_length=20)
    attorney = models.CharField(max_length=20)
    date_opened = models.DateField()
    date_closed = models.DateField()
    description = models.TextField(max_length=500)
    case_status = models.CharField(
        max_length=1,
        choices=CASESTATUS,
        default=CASESTATUS[0][0]
    )
    case_stage = models.CharField(
        max_length=1,
        choices=CASESTAGE,
        default=CASESTAGE[0][0]
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("case-detail", kwargs={"pk": self.pk})
    

class Task(models.Model):
    task_name = models.CharField(max_length=20)
    task_type = models.CharField(
        max_length=1,
        choices=TASKTYPE,
        default=TASKTYPE[0][0]
    )
    task_status = models.CharField(
        max_length=1,
        choices=TASKSTATUS,
        default=TASKSTATUS[0][0]
    )
    task_description = models.TextField(max_length=500)
    date_created = models.DateField()
    date_closed = models.DateField()
    estimated_time = models.IntegerField()
    actual_time = models.IntegerField()
    
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
