Feature: Add new books to the library system
  As a librarian
  I want to be able to add new books to the system
  So that the library's inventory is up to date

  Scenario: Add a new book with valid information
    Given I am an authenticated librarian
    When I submit a new book with title "The Great Gatsby" and author "F. Scott Fitzgerald"
    Then the book should be added to the system
    And I should receive a confirmation message with the book's details
