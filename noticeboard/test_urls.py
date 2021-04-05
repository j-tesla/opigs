from django.urls import reverse,resolve


def test_get_annnouncements_url():
    path = reverse('announcements')
    assert resolve(path).view_name=='announcements'

def test_post_annnouncements_url():
    path = reverse('post_announcement')
    assert resolve(path).view_name=='post_announcement'

def test_update_url():
    path = reverse('update_announcement',kwargs={'pk':'announcement2'})
    assert resolve(path).view_name=='update_announcement'

def test_delete_url():
    path = reverse('delete_announcement',kwargs={'pk':'announcement2'})
    assert resolve(path).view_name=='delete_announcement'