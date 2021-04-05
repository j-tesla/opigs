from django.urls import reverse,resolve


def test_post_url():
    path = reverse('post_job')
    assert resolve(path).view_name=='post_job'


def test_update_url():
    path = reverse('update_job',kwargs={'pk':'job'})
    assert resolve(path).view_name=='update_job'

def test_delete_url():
    path = reverse('delete_job',kwargs={'pk':'job'})
    assert resolve(path).view_name=='delete_job'

def test_apply_url():
    path = reverse('apply_to_job',kwargs={'pk':'job'})
    assert resolve(path).view_name=='apply_to_job'

def test_job_url():
    path = reverse('job',kwargs={'pk':'job_name'})
    assert resolve(path).view_name=='job'

def test_resume_url():
    path = reverse('view_resume',kwargs={'pk':'job_name'})
    assert resolve(path).view_name=='view_resume'
