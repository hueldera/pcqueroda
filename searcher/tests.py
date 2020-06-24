from django.test import TestCase
from .models import Software, Computer
from django.urls import reverse
from random import randint

class ModelsSearcherTest(TestCase):
    def setUp(self):
        Software.objects.create(name='Test',
                                min_graphics_level=5,
                                min_processor_level=3,
                                min_memory_level=5,
                                max_graphics_level=7,
                                max_processor_level=5,
                                max_memory_level=8)

        Computer.objects.create(title='Test 8GB',
                                graphics_level=6,
                                processor_level=4,
                                memory_level=6,
                                price=2000,
                                affiliate_link='https://example.com')

    def test_software_to_str(self):
        test_software = Software.objects.get(name='Test')
        self.assertEqual(str(test_software), test_software.name)

    def test_computer_to_str(self):
        test_computer = Computer.objects.get(title='Test 8GB')
        self.assertEqual(str(test_computer), test_computer.title)



class ViewsSearcherTest(TestCase):
    def setUp(self):
        for i in range(0, 1500):
            Software.objects.create(name='Test '+ str(i),
                                    min_graphics_level=randint(1, 10),
                                    min_processor_level=randint(1, 10),
                                    min_memory_level=randint(1, 10),
                                    max_graphics_level=randint(1, 10),
                                    max_processor_level=randint(1, 10),
                                    max_memory_level=randint(1, 10))

            Computer.objects.create(title='Test 8GB '+ str(i),
                                    graphics_level=randint(1, 10),
                                    processor_level=randint(1, 10),
                                    memory_level=randint(1, 10),
                                    price=2000,
                                    affiliate_link='https://example.com')

    def test_searcher_exists(self):
        response = self.client.get('/searcher/')
        self.assertEqual(response.status_code, 200)

    def test_results_exists(self):
        response = self.client.get('/searcher/results?sw=1')
        self.assertEqual(response.status_code, 200)

    def test_results_redirect_if_nothing_selected(self):
        response = self.client.get('/searcher/results?')
        self.assertEqual(response.status_code, 302)

    def test_results_contains_software_list(self):
        response = self.client.get('/searcher/results?sw=1&sw=3')
        self.assertTrue('selected_softwares' in response.context)
        self.assertTrue(len(response.context['selected_softwares']) == 2)

    def test_results_contains_computer_list(self):
        response = self.client.get('/searcher/results?sw=1&sw=3')
        self.assertTrue('computer_list' in response.context)

    def test_searcher_contains_software_list(self):
        response = self.client.get('/searcher/')
        self.assertTrue('software_list' in response.context)

    def test_searcher_ajax_search(self):
        response = self.client.get('/searcher/?s=Test 690')
        self.assertTrue('<!DOCTYPE html>' in str(response.content))

        response = self.client.get('/searcher/?s=Test 690',**{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertTrue('<h3 class="name">Test 690</h3>' in str(response.content).replace('\\\\n', '').replace('\\', ''))

        response = self.client.get('/searcher/?s=Test Erro',**{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertTrue('Nenhum item foi encontrado' in str(response.content).replace('\\\\n', '').replace('\\', ''))
        self.assertTrue('<h3 class="name">Test 690</h3>' not in str(response.content).replace('\\\\n', '').replace('\\', ''))




