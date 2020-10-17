# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from calculadora import Calculadora, CalculadoraPrecisao

@given('numbers {valueA:f} and {valueB:f}')
def step_impl(context, valueA, valueB):
    context.valA = valueA    
    context.valB = valueB
    pass

@then('sum should be {result:f}')
def step_impl(context, result):  # -- NOTE: number is converted into integer
    c = Calculadora()
    assert c.soma(context.valA, context.valB) == result

@then('sum with precision {precision:d} should be {result:f}')
def step_impl(context, precision, result):
    c = CalculadoraPrecisao(precision)
    assert c.soma(context.valA, context.valB) == result
