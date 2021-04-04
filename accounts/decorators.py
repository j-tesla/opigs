from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from .models import Company


def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 'STUDENT',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function is not None:
        return actual_decorator(function)

    return actual_decorator


def company_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 'COMPANY',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function is not None:
        return actual_decorator(function)

    return actual_decorator


def verified_company_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    def f(u):
        if u.is_active and u.user_type == 'COMPANY':
            company = Company.objects.get(user__id=u.id)
            return company.verified
        return False

    actual_decorator = user_passes_test(
        f,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function is not None:
        return actual_decorator(function)

    return actual_decorator


def alumni_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 'ALUMNI',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function is not None:
        return actual_decorator(function)

    return actual_decorator


def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    def f(u):
        return u.is_active and u.user_type == 'ADMIN'

    actual_decorator = user_passes_test(
        f,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function is not None:
        return actual_decorator(function)

    return actual_decorator
