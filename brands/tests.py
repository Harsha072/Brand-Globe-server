from django.test import TestCase
from .models import Brand

class BrandModelTest(TestCase):

    def test_brand_creation(self):
        """brand can be created successfully."""
        brand = Brand.objects.create(
            name='Test Brand',
            description='This is a test brand.',
            logo='path/to/logo.png'  # Adjust this based on your media setup
        )
        self.assertEqual(brand.name, 'Test Brand')
        self.assertEqual(brand.description, 'This is a test brand.')

    def test_brand_read(self):
        """brand can be read successfully."""
        brand = Brand.objects.create(
            name='Test Brand',
            description='This is a test brand.',
            logo='path/to/logo.png'
        )
        retrieved_brand = Brand.objects.get(id=brand.id)
        self.assertEqual(retrieved_brand.name, brand.name)

    def test_brand_update(self):
        """brand can be updated successfully."""
        brand = Brand.objects.create(
            name='Test Brand',
            description='This is a test brand.',
            logo='path/to/logo.png'
        )
        brand.name = 'Updated Brand'
        brand.save()
        updated_brand = Brand.objects.get(id=brand.id)
        self.assertEqual(updated_brand.name, 'Updated Brand')

    def test_brand_deletion(self):
        """brand can be deleted successfully."""
        brand = Brand.objects.create(
            name='Test Brand',
            description='This is a test brand.',
            logo='path/to/logo.png'
        )
        brand_id = brand.id
        brand.delete()
        with self.assertRaises(Brand.DoesNotExist):
            Brand.objects.get(id=brand_id)


