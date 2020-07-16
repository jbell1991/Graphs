import random
import time

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # use num_users
        for user in range(num_users):
            self.add_user(user)
        # Create friendships
        # make a list with all POSSIBLE friendships
        # Example:
        # 5 users
        # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]
        friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users + 1):
                friendship = (user, friend)
                friendships.append(friendship)
        # Shuffle the list
        self.fisher_yates_shuffle(friendships)
        # take as many as we need
        total_friendships = num_users * avg_friendships

        random_friendships = friendships[:total_friendships//2]
        # add to self.friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def linear_populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # use num_users
        for user in range(num_users):
            self.add_user(user)
        
        # linear way to add the number of friendships we need?
        target_number_friendships = num_users * avg_friendships
        friendships_created = 0

        while friendships_created < target_number_friendships:
            friend_one = random.randint(1, self.last_id)
            friend_two = random.randint(1, self.last_id)

            friendship_was_made = self.add_friendship(friend_one, friend_two)
            if friendship_was_made:
                friendships_created += 2

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()
        # enqueue starting node
        q.enqueue([starting_vertex])
        # make a set to track if we've been here before
        visited = set()
        # while our queue isn't empty
        while q.size() > 0:
            path = q.dequeue()
            current_node = path[-1]
            # if we haven't visited this node yet,
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
                # check if the node equals the target
                if current_node == destination_vertex:
                    return path
                neighbors = self.friendships[current_node]
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        paths = []
        # for each user in the network
        for user in self.users:
            # get the shortest path from input user to furthest extension using bfs
            path = self.bfs(user_id, user)
            # set key equal to user_id and value equal to the shortest path
            visited[user] = path

        # returns a dictionary containing every user in that user's extended
        # network along with the shortest friendship path between each
        visited = {key : value for key, value in visited.items() if value is not None}
        # return visited
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    num_users = 1000
    avg_friendships = 5

    start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)
    end_time = time.time()

    print(f"Populate graph O(n^2): {end_time - start_time}")

    start_time = time.time()
    sg.linear_populate_graph(num_users, avg_friendships)
    end_time = time.time()

    print(f"Populate graph linear: {end_time - start_time}")
    
    # connections = sg.get_all_social_paths(1)
    # print(connections)

    # percentage of total users are in our extended social network?

    # how many people we know, divided by how many people there are

    # print(f'{(len(connections) - 1) / 1000 * 100}%')

    # what is the average degree of separation between a user and those in his/her extended network?

    # average length of a path to each user
    # traverse a user's extended connections, gather lengths, sum,
    # total_lengths = 0
    # for friend in connections:
    #     total_lengths += len(connections[friend])
    # # divide by number of friends in connected component aka extended social network

    # print(f' Average degree of separation: {total_lengths / len(connections)}')
