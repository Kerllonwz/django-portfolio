import pytest
import factory
from blog.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f"Post {n}")
    content = factory.Faker("paragraph")
    published = False


@pytest.mark.django_db
def test_post_is_created():
    post = PostFactory()
    assert Post.objects.count() == 1
    assert post.title is not None
    assert post.content is not None


@pytest.mark.django_db
def test_post_published_default_is_false():
    post = PostFactory()
    assert post.published is False
