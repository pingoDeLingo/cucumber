from behave import given, when, then
from calc import Calculator

@given('I have a calculator')
def step_given_have_calculator(context):
    context.calculator = Calculator()

@when('I add {x:d} and {y:d}')
def step_when_add_numbers(context, x, y):
    context.result = context.calculator.add(x, y)

@then('the result should be {expected_result:d}')
def step_then_check_addition_result(context, expected_result):
    assert context.result == expected_result

@when('I subtract {y:d} from {x:d}')
def step_when_subtract_numbers(context, x, y):
    context.result = context.calculator.subtract(x, y)

@then('the result should be {expected_result:d}')
def step_then_check_subtraction_result(context, expected_result):
    assert context.result == expected_result

@when('I divide {x:d} by {y:d}')
def step_when_divide_numbers(context, x, y):
    context.result = context.calculator.divide(x, y)

@then('the result should be {expected_result:d}')
def step_then_check_result(context, expected_result):
    assert context.result == expected_result

@when('I multiply {x:d} and {y:d}')
def step_when_multiply_numbers(context, x, y):
    context.result = context.calculator.multiply(x, y)

@then('the result should be {expected_result:d}')
def step_then_check_result(context, expected_result):
    assert context.result == expected_result