from django.urls import reverse,resolve


def test_get_notifications_url():
    path = reverse('notifications')
    assert resolve(path).view_name=='notifications'

def test_delete_url():
    path = reverse('delete_notification',kwargs={'pk':'notif1'})
    assert resolve(path).view_name=='delete_notification'

def test_clear_url():
    path = reverse('clear_notifications')
    assert resolve(path).view_name=='clear_notifications'