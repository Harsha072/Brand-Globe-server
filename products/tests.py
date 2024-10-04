from django.test import TestCase
from .models import Product, Brand
from decimal import Decimal
class ProductModelTest(TestCase):

    def setUp(self):
        """Create a brand for the product."""
        self.brand = Brand.objects.create(
            name='Test Brand',
            description='This is a test brand.',
            logo='path/to/logo.png'
        )

    def test_product_creation(self):
        """Test that a product can be created successfully."""
        product = Product.objects.create(
            name='Test Product',
            description='This is a test product.',
            category='Electronics',
            price=199.99,
            image='path/to/product_image.png',
            brand=self.brand
        )
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.category, 'Electronics')
        self.assertEqual(product.price, 199.99)
        self.assertEqual(product.brand, self.brand)

    def test_product_read(self):
        """Test that a product can be read successfully."""
        product = Product.objects.create(
            name='Test Product',
            description='This is a test product.',
            category='Electronics',
            price=199.99,
            image='path/to/product_image.png',
            brand=self.brand
        )
        retrieved_product = Product.objects.get(id=product.id)
        self.assertEqual(retrieved_product.name, 'Test Product')

    def test_product_update(self):
        """Test that a product can be updated successfully."""
        product = Product.objects.create(
            name='Test Product',
            description='This is a test product.',
            category='Electronics',
             price=Decimal('199.99'),
            image='path/to/product_image.png',
            brand=self.brand
        )
        product.name = 'Updated Product'
        product.price = Decimal('299.99')
        product.save()

        updated_product = Product.objects.get(id=product.id)
        self.assertEqual(updated_product.name, 'Updated Product')
        self.assertEqual(updated_product.price, Decimal('299.99'))

    def test_product_deletion(self):
        """Test that a product can be deleted successfully."""
        product = Product.objects.create(
            name='Test Product',
            description='This is a test product.',
            category='Electronics',
            price=199.99,
            image='path/to/product_image.png',
            brand=self.brand
        )
        product_id = product.id
        product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product_id)


