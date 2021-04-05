from django.urls import reverse,resolve


def test_login_url():
    path = reverse('login')
    assert resolve(path).view_name=='login'

def test_profile_url():
    path = reverse('my_profile')
    assert resolve(path).view_name=='my_profile'

def test_specific_profile_url():
    path = reverse('profile',kwargs={'pk':'student'})
    assert resolve(path).view_name=='profile'

def test_signup_url():
    path = reverse('signup')
    assert resolve(path).view_name=='signup'

def test_student_signup_url():
    path = reverse('students_signup')
    assert resolve(path).view_name=='students_signup'

def test_companies_signup_url():
    path = reverse('companies_signup')
    assert resolve(path).view_name=='companies_signup'

def test_alumni_signup_url():
    path = reverse('alumni_signup')
    assert resolve(path).view_name=='alumni_signup'