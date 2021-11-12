import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','learning_users.settings')

import django

django.setup()

import random

from user_app.models import Webpage,Topic,AccessRecord

from faker import Faker

fakegen = Faker()

topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t
def populate(i=5):
        for i in range(i):
            top = add_topic()


            fake_url = fakegen.url()
            fake_date = fakegen.date()
            fake_name = fakegen.name()

            webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
            acc_rec = AccessRecord.objects.get_or_create(name= webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(50)
    print('populating complete!')
