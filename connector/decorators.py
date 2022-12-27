from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


# Decorator code from simpleisbetterthancomplex.com tutorial.

# Decorator to check if logged in user is a rescue.
def rescue_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME,
                    login_url='login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_rescue,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# Decorator to check if logged in user is a pound.
def pound_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME,
                   login_url='login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_pound,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
