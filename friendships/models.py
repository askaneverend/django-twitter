from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='following_friendship_set',
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='follower_friendship_set',
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        index_together = (
            # fetch all people I followed
            ('from_user_id', 'created_at'),
            # fetch all people who following me
            ('to_user_id', 'created_at'),
        )
        unique_together = (('from_user_id', 'to_user_id'),) # avoid duplicate

    def __str__(self):
        return "{} followed {}".format(self.from_user, self.to_user)
