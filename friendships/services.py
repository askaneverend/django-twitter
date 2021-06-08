from friendships.models import Friendship


class FriendshipService(object):

    @classmethod
    def get_followers(cls, user):
