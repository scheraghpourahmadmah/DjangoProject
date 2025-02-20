import json
from django.core.management.base import BaseCommand
from ReportData.models import Report, Picture

class Command(BaseCommand):
    help = "Load JSON data into the database"

    def handle(self, *args, **kwargs):
        with open("data/input.json", "r") as file:
            data = json.load(file)

            # Create the Report entry
            report = Report.objects.create(
                date=data["date"],
                daily_report_no=data["daily_report_no"],
                page=data["page"]
            )

            # Create Picture entries
            for pic in data["pictures"]:
                Picture.objects.create(
                    report=report,
                    file_name=pic["file_name"],
                    location=pic["location"],
                    description=pic["description"]
                )

        self.stdout.write(self.style.SUCCESS("Successfully loaded JSON data!"))
