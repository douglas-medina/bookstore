import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="Category 1")
        self.product = ProductFactory(
            title="notebook", price=800.00, active=True, category=[self.category]
        )

    def test_get_all_product(self):

        response = self.client.get(reverse("product-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = json.loads(response.content)
        self.assertEqual(product_data["results"][0]["title"], self.product.title)
        self.assertEqual(product_data["results"][0]["price"], self.product.price)
        self.assertEqual(product_data["results"][0]["active"], self.product.active)
        self.assertEqual(
            product_data["results"][0]["category"][0]["title"], self.category.title
        )

    def test_create_product(self):
        category = CategoryFactory()
        data = {
            "title": "unique_notebook",
            "price": 800.00,
            "categories_id": [category.id],
        }

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title="unique_notebook")

        self.assertEqual(created_product.title, "unique_notebook")
        self.assertEqual(created_product.price, 800.00)
