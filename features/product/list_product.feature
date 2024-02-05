Feature: Product listing
  As a customer
  I want to be able to view a list of available products
  So that I can choose products to purchase

  Scenario: Retrieve the list of products
    Given the system knows about the following products
      | name       | description       | price |
      | Product 1  | Description 1     | 10.00 |
      | Product 2  | Description 2     | 20.00 |
    When I request the list of products
    Then the response should be a list containing 2 products
    And the response should include Product 1 and Product 2
