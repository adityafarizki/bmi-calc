Feature: BMI Calculator
    As a visitor
    I want to be able to calculate my BMI (Body Mass Index)
    So I can verify if my weight is healthy or not

    @wip
    Scenario: Calculate an overweight BMI
        When the visitor sends request "GET /?height=175&weight=85"
        Then the app returns response "HTTP 200" with the following contents
            """
            {
                "bmi": 27.75,
                "label": "overweight"
            }
            """
    
    Scenario: Calculate an underweight BMI
        When the visitor sends request "GET /?height=175&weight=50"
        Then the app returns response "HTTP 200" with the following contents
            """
            {
                "bmi": 16.32,
                "label": "underweight"
            }
            """

    Scenario: Calculate a normal BMI
        When the visitor sends request "GET /?height=175&weight=70"
        Then the app returns response "HTTP 200" with the following contents
            """
            {
                "bmi": 22.85,
                "label": "normal"
            }
            """
    
    Scenario: Height params less than or equal 0
        When the visitor sends request "GET /?height=-1&weight=70"
        Then the app returns response "HTTP 400" with the following contents
            """
            {
                "detail": "Height should be > 0 cm"
            }
            """
    
    Scenario: Weight params less than or equal 0
        When the visitor sends request "GET /?height=85&weight=-2"
        Then the app returns response "HTTP 400" with the following contents
            """
            {
                "detail": "Weight should be > 0 kg"
            }
            """
    
    Scenario: Request without height params
        When the visitor sends request "GET /?weight=82"
        Then the app returns response "HTTP 422" with the following contents
            """
            {
                "detail": [{"loc": ["query", "height"], "msg": "field required", "type": "value_error.missing"}]
            }
            """
    
    Scenario: Request without weight params
        When the visitor sends request "GET /?height=175"
        Then the app returns response "HTTP 422" with the following contents
            """
            {
                "detail": [{"loc": ["query", "weight"], "msg": "field required", "type": "value_error.missing"}]
            }
            """