from os import urandom
from unittest import skip

from django.test import Client
from django.test import TestCase

from apps.blog.models import BlogPost
from apps.blog.views import AllBlogPostsView
from apps.blog.views import BlogPostView
from project.utils.user_utils import UserTestMixin
from project.utils.validate_response import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin, UserTestMixin):
    def test_get(self):
        self.validate_response(
            url="/blog/",
            expected_view=AllBlogPostsView,
            expected_template="blog/all_posts.html",
            expected_view_name="blog:all_posts",
        )

    def test_post(self):
        self.validate_response(
            method="post",
            url="/blog/",
            expected_status_code=405,
            expected_view=AllBlogPostsView,
            expected_template="blog/all_posts.html",
            expected_view_name="blog:all_posts",
        )

    def test_get_absent(self):
        self.validate_response(
            url="/blog/post/01/",
            expected_status_code=404,
            expected_view=BlogPostView,
            expected_template="blog/post.html",
            expected_view_name="blog:post",
        )

    def test_get_existing_anon(self):
        placeholder = urandom(4).hex()
        post = BlogPost(title=placeholder, content=placeholder)
        post.save()

        self.validate_response(
            url=f"/blog/post/{post.pk}/",
            expected_view=BlogPostView,
            expected_template="blog/post.html",
            expected_view_name="blog:post",
        )

    def test_get_existing_authed(self):
        placeholder = urandom(4).hex()
        user = self.create_user(placeholder)
        client = Client()
        client.login(username=user.username, password=placeholder)

        post = BlogPost(title=placeholder, content=placeholder)
        post.save()

        self.validate_response(
            client=client,
            url=f"/blog/post/{post.pk}/",
            expected_view=BlogPostView,
            expected_template="blog/post.html",
            expected_view_name="blog:post",
        )

    def test_post(self):
        post = BlogPost()
        post.save()

        self.validate_response(
            method="post",
            url=f"/blog/post/{post.pk}/",
            expected_status_code=405,
            expected_view=BlogPostView,
            expected_template="blog/post.html",
            expected_view_name="blog:post",
        )
