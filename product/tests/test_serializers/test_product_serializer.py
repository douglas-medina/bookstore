from django.test import TestCase
from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer

class TestProductSerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(title="technology")
        self.product_1 = ProductFactory(title="mouse", price=100, category=[self.category])
        self.product_serializer = ProductSerializer(self.product_1)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data["price"], 100)
        self.assertEqual(serializer_data["title"], "mouse")

        self.assertIn("category", serializer_data)

        categories_data = serializer_data["category"]
        self.assertEqual(len(categories_data), 1)
        self.assertEqual(categories_data[0]["title"], "technology")
