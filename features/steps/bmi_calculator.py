import json

from behave import then, when
from expects import equal, expect, have_key


@when('the visitor sends request "{request_spec}"')
def the_user_hit_endpoint_with_body(context, request_spec):
    method, path = request_spec.split(" ")
    method = method.lower()

    context.response = getattr(context.client, method)(path)


@then('the app returns response "{return_code}" with the following contents')
def the_app_returns(context, return_code):
    status_code = int(return_code.split(" ")[1])
    expect(context.response.status_code).to(equal(status_code))

    expected_content = json.loads(context.text)
    fetched_content = context.response.json()

    expect(fetched_content).to(equal(expected_content))
