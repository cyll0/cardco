from django.test import TestCase, Client
from main.models import Item  # Import the Item model from your app

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')


class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item = Item.objects.create(name="Sample Item", amount=10, description="This is a test item description.")

    def test_name_field(self):
        item = Item.objects.get(id=self.item.id)
        max_length = item._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
    
    def test_amount_field(self):
        item = Item.objects.get(id=self.item.id)
        self.assertEqual(item.amount, 10)
    
    def test_description_field(self):
        item = Item.objects.get(id=self.item.id)
        self.assertEqual(item.description, "This is a test item description.")

    def test_name_label(self):
        item = Item.objects.get(id=self.item.id)
        field = item._meta.get_field('name')
        self.assertEqual(field.verbose_name, 'name')
    
    def test_amount_label(self):
        item = Item.objects.get(id=self.item.id)
        field = item._meta.get_field('amount')
        self.assertEqual(field.verbose_name, 'amount')

    def test_description_label(self):
        item = Item.objects.get(id=self.item.id)
        field = item._meta.get_field('description')
        self.assertEqual(field.verbose_name, 'description')