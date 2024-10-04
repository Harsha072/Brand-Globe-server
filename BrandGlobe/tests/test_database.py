
from django.test import TestCase
from django.db import connection

class DatabaseIntegrationTests(TestCase):
    
    # Use the actual database and not Django's test database for integration tests
    databases = '__all__'
    
    def test_database_connection(self):
        """Test that a connection to the actual database can be established."""
        try:
            # Check if the connection is active
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1')  # Simple query to test the connection
                row = cursor.fetchone()
            self.assertEqual(row[0], 1)  # Assert that the query returned a result
        except Exception as e:
            self.fail(f"Database connection failed: {e}")