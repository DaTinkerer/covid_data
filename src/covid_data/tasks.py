from celery import shared_task
import requests
import csv
from bs4 import BeautifulSoup

@shared_task()
def test():

    with open('covid_data/data.csv', 'w') as f:

        writer = csv.writer(f)
        writer.writerow(['test'])
        f.close()
