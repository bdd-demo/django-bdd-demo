from behave import given, when, then
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from apps.book.models import Book

@given('I am an authenticated librarian')
def step_impl(context):
    context.client = APIClient()
    context.user = get_user_model().objects.create_user(username='librarian', password='password')
    context.client.force_authenticate(user=context.user)

@when('I submit a new book with title "{title}" and author "{author}"')
def step_impl(context, title, author):
    context.response = context.client.post('/book/', {'title': title, 'author': author}, format='json')

@then('the book should be added to the system')
def step_impl(context):
    assert context.response.status_code == 201
    assert Book.objects.filter(title=context.response.json()['title']).exists()

@then('I should receive a confirmation message with the book\'s details')
def step_impl(context):
    response_data = context.response.json()
    assert 'id' in response_data
    assert response_data['title'] == 'The Great Gatsby'
    assert response_data['author'] == 'F. Scott Fitzgerald'
