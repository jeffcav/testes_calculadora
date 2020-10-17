# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from calculadora import Calculadora, CalculadoraPrecisao

@given('numbers {a:f} and {b:f}')
def step_impl(context, a, b):
    context.a = a    
    context.b = b
    pass

@then('sum should be {result:f}')
def step_impl(context, result):
    c = Calculadora()
    assert c.soma(context.a, context.b) == result

@then('sum with precision {precision:d} should be {result:f}')
def step_impl(context, precision, result):
    c = CalculadoraPrecisao(precision)
    assert c.soma(context.a, context.b) == result
