import time
import random

from locust import HttpUser, task, between

name_queries = [
    'cauce',
    'smith',
    'wilson',
    'thorogood',
    'drea',
    'sha'
    'thacker',
    'kit',
    'hank',
    'cooper',
    'fleur',
    'st mary',
]


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    host = 'https://directory.iamdev.s.uw.edu'

    @task
    def view_items(self):
        self.client.post('/', data={
            'method': 'name',
            'query': random.choice(name_queries),
            'search_type': 'experimental',
        })
        time.sleep(1)
