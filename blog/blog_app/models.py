from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):

    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Post(models.Model):
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    text = models.TextField(blank=False)
    rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    tag = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag


class PostComment(models.Model):
    class Meta:
        db_table = 'post_comments'
        verbose_name = 'Post comment'
        verbose_name_plural = 'Post comments'

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class SubComment(models.Model):
    class Meta:
        db_table = 'sub_comments'
        verbose_name = 'Subcomment'
        verbose_name_plural = 'Subcomments'

    parent = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='parent')
    child = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='child')

    def __str__(self):
        return f"Parent comment: {self.parent}"


class PostTag(models.Model):
    class Meta:
        db_table = 'post_tags'
        verbose_name = 'Post tag'
        verbose_name_plural = 'Post tags'

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"Tag for {self.post}: {self.tag}"
