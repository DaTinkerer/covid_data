from celery import shared_task
import requests
import json
import csv


@shared_task()
def test():

    r = requests.get(
        'https://data.cdc.gov/api/id/9bhg-hcku.json?$query=select%20*%2C%20%3Aid%20limit%20100')
    res = r.json()

    # selecting the data from the json list
    # that I need and storing each set in a list
    # each set represent data from different age groups
    set1 = res[2]
    list1 = [
        set1['age_group'],
        set1['covid_19_deaths'],
        set1['total_deaths'],
        set1['pneumonia_deaths'],
        set1['influenza_deaths'],
    ]

    set2 = res[6]
    list2 = [
        set2['age_group'],
        set2['covid_19_deaths'],
        set2['total_deaths'],
        set2['pneumonia_deaths'],
        set2['influenza_deaths'],
    ]

    set3 = res[8]
    list3 = [
        set3['age_group'],
        set3['covid_19_deaths'],
        set3['total_deaths'],
        set3['pneumonia_deaths'],
        set3['influenza_deaths'],
    ]

    set4 = res[10]
    list4 = [
        set4['age_group'],

        set4['covid_19_deaths'],
        set4['total_deaths'],
        set4['pneumonia_deaths'],
        set4['influenza_deaths'],
    ]

    set5 = res[12]
    list5 = [
        set5['age_group'],
        set5['covid_19_deaths'],
        set5['total_deaths'],
        set5['pneumonia_deaths'],
        set5['influenza_deaths'],
    ]

    set6 = res[14]
    list6 = [
        set6['age_group'],
        set6['covid_19_deaths'],
        set6['total_deaths'],
        set6['pneumonia_deaths'],
        set6['influenza_deaths'],
    ]

    set7 = res[15]
    list7 = [
        set7['age_group'],
        set7['covid_19_deaths'],
        set7['total_deaths'],
        set7['pneumonia_deaths'],
        set7['influenza_deaths'],
    ]

    set8 = res[16]
    list8 = [
        set8['age_group'],
        set8['covid_19_deaths'],
        set8['total_deaths'],
        set8['pneumonia_deaths'],
        set8['influenza_deaths'],
    ]

    with open('covid_data/data.csv', 'w') as f:

        writer = csv.writer(f)
        writer.writerow(['age_group', 'c19_deaths', 'total_deaths',
                        'pneumonia_deaths', 'flu_deaths'])
        writer.writerow([list1[0], list1[1], list1[2], list1[3]])
        writer.writerow([list2[0], list2[1], list2[2], list2[3]])
        writer.writerow([list3[0], list3[1], list3[2], list3[3]])
        writer.writerow([list4[0], list4[1], list4[2], list4[3]])
        writer.writerow([list5[0], list5[1], list5[2], list5[3]])
        writer.writerow([list6[0], list6[1], list6[2], list6[3]])
        writer.writerow([list7[0], list7[1], list7[2], list7[3]])
        writer.writerow([list8[0], list8[1], list8[2], list8[3]])

        f.close()
