from django.db import models

class Report(models.Model):
    date = models.DateField()
    daily_report_no = models.CharField(max_length=50, default="000")
    page = models.CharField(max_length=20)

    def __str__(self):
        return f"Report No: {self.daily_report_no} - Date: {self.date}"

class Picture(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="pictures")
    file_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.file_name} - {self.location}"
