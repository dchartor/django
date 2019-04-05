from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from boards.models import Board, Topic, Post
from boards.views import PostListView


class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='Djangoasds', description='Djaasdngo Board')
        user = User.objects.create_user(username='Johnh', email='john@mail.com', password='123')
        topic = Topic.objects.create(subject='Hopa', board=board, starter=user)
        Post.objects.create(message='Hello Hopa', topic=topic, created_by=user)
        url = reverse('boards:topic_posts', kwargs={'pk': board.pk, 'topic_pk': topic.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/boards/1/topics/1/')
        self.assertEquals(view.func.view_class, PostListView)
