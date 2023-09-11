Feature: Calculator
  Scenario: Addition
    Given I have a calculator
    When I add 5 and 7
    Then the result should be 12

  Scenario: Subtraction
    Given I have a calculator
    When I subtract 7 from 15
    Then the result should be 8

  Scenario: Division
  Given I have a calculator
  When I divide 12 by 3
  Then the result should be 4

  Scenario: Multiplication
  Given I have a calculator
  When I multiply 4 and 5
  Then the result should be 12