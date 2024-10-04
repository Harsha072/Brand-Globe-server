from django.test import TestCase
from products.models import Brand


class BrandIntegrationTests(TestCase):

    databases = '__all__'

    def test_create_brand(self):
        """Test creating a brand in the actual database."""
        brand = Brand.objects.create(name='New Brand', description='A test brand', logo='logo.png')
        self.assertIsNotNone(brand.id)

    def test_read_brand(self):
        """Test retrieving a brand from the actual database."""
        brand = Brand.objects.create(name='Read Brand', description='Another test brand', logo='logo.png')
        fetched_brand = Brand.objects.get(name='Read Brand')
        self.assertEqual(fetched_brand.name, 'Read Brand')

    def test_update_brand(self):
        """Test updating a brand in the actual database."""
        brand = Brand.objects.create(name='Old Brand', description='Old description', logo='logo.png')
        brand.name = 'Updated Brand'
        brand.save()
        updated_brand = Brand.objects.get(id=brand.id)
        self.assertEqual(updated_brand.name, 'Updated Brand')

    def test_delete_brand(self):
        """Test deleting a brand in the actual database."""
        brand = Brand.objects.create(name='Temp Brand', description='A brand to delete', logo='logo.png')
        brand_id = brand.id
        brand.delete()
        with self.assertRaises(Brand.DoesNotExist):
            Brand.objects.get(id=brand_id)
