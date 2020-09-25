class User:

    def __init__(self):
        self._trips = []
        self._friends = []

    def getFriends(self):
        return self._friends

    def addFriend(self, user):
        self._friends.append(user)

    def addTrip(self, trip):
        self._trips.append(trip)

    def trips(self):
        return self._trips
