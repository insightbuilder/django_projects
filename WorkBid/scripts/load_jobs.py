from myjob.models import Work
import pandas as pd

def run():
    jobs = pd.read_csv("/home/kamal/gitfolders/django_projects/support_files/job_data.csv")

    jobs_list = jobs.to_dict(orient='records')

    Work.objects.all().delete()
#job_title,job_description,budget,type,experience_level,bid_value,author

    for job in jobs_list:
        title = job['job_title']
        description = job['job_description']
        budget = job['budget']
        work_type = job['type']
        experience_level = job['experience_level']
        author = job['author']

        w = Work(title = title, 
            description = description,
             budget = budget,
            work_type = work_type,
            experience_level = experience_level,
            author = author)

        w.save()
         



