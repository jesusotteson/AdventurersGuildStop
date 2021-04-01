from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    passwordhash = models.CharField(max_length=250)
    birthday = models.DateField()
    registrationDate = models.DateField()
    realname = models.CharField(max_length=150)
    bio = models.TextField()

class Guild(models.Model):
    name = models.CharField(max_length=250)
    handle = models.CharField(max_length=15)
    description = models.TextField()

class Thread(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    postDate = models.DateTimeField()

class ThreadReaction(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reactionType = models.CharField(max_length=10)
    reactionDate = models.DateTimeField()

class ThreadComment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    commentDate = models.DateTimeField()

class CommentReaction(models.Model):
    comment = models.ForeignKey(ThreadComment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reactionType = models.CharField(max_length=10)
    reactionDate = models.DateTimeField()
