from django.test import TestCase
from products.models import Product  
from brands.models import Brand 

class ProductIntegrationTests(TestCase):

    databases = '__all__'

    def setUp(self):
        """Create a brand instance to associate with products."""
        self.brand = Brand.objects.create(name='Test Brand', description='Brand for testing', logo='logo.png')

    def test_create_product(self):
        """Test creating a product in the actual database."""
        product = Product.objects.create(
            name='New Product',
            description='A test product',
            category='Test Category',
            price=99.99,
            image='product_image.png',
            brand=self.brand  # Associate with the brand created in setUp
        )
        self.assertIsNotNone(product.id)

    def test_read_product(self):
        """Test retrieving a product from the actual database."""
        product = Product.objects.create(
            name='Read Product',
            description='Another test product',
            category='Read Category',
            price=49.99,
            image='read_product_image.png',
            brand=self.brand  # Associate with the brand created in setUp
        )
        fetched_product = Product.objects.get(name='Read Product')
        self.assertEqual(fetched_product.name, 'Read Product')

    def test_update_product(self):
        """Test updating a product in the actual database."""
        product = Product.objects.create(
            name='Old Product',
            description='Old description',
            category='Old Category',
            price=19.99,
            image='old_product_image.png',
            brand=self.brand  # Associate with the brand created in setUp
        )
        product.name = 'Updated Product'
        product.save()
        updated_product = Product.objects.get(id=product.id)
        self.assertEqual(updated_product.name, 'Updated Product')

    def test_delete_product(self):
        """Test deleting a product in the actual database."""
        product = Product.objects.create(
            name='Temp Product',
            description='A product to delete',
            category='Delete Category',
            price=9.99,
            image='temp_product_image.png',
            brand=self.brand  # Associate with the brand created in setUp
        )
        product_id = product.id
        product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product_id)
