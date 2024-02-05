from behave import given, when, then, step
from django.urls import reverse
from rest_framework.test import APIClient
from apps.product.models import Product

client = APIClient()

@given('the system knows about the following products')
def step_impl(context):
    for row in context.table:
        Product.objects.create(name=row['name'], description=row['description'], price=row['price'])

@when('I request the list of products')
def step_impl(context):
    context.response = client.get("/product/")

@then('the response should be a list containing {count:n} products')
def step_impl(context, count):
    assert len(context.response.data) == count

@then('the response should include {product_name} and {product_name2}')
def step_impl(context, product_name, product_name2):
    products = [product['name'] for product in context.response.data]
    assert product_name in products
    assert product_name2 in products
