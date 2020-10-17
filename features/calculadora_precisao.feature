Feature: calculadora com precisao

    Scenario: Sum 30 with precision 6
        Given numbers 1.0 and 1.0
        Then sum should be 2.0

    Scenario: Sum 0.24 with precision 6
        Given numbers 0.2 and 0.04
        Then sum with precision 6 should be 0.24