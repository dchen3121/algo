# Given information about active users on the network, find the shortest route for a message from one user (the sender) to another (the recipient).
# Return a list of users that make up this route.
# There might be a few shortest delivery routes, all with the same length. For now, let's just return any shortest route.
# Your network information takes the form of a dictionary mapping username strings to a list of other users nearby.

# Example:
# input:
network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam'    : ['Nathan', 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min', 'Scott'],
}
# output:
# For sending from Jayden to Adam:
# ['Jayden', 'Amelia', 'Adam']


from typing import List, Dict
from collections import deque


def send_msg(network: Dict[str, str], sender: str, receiver: str) -> List[str]:
    queue = deque()
    prev_dict = {}
    queue.append(sender)

    while queue:
        curr_node = queue.popleft()
        for neighbour_node in network[curr_node]:
            if neighbour_node == receiver:
                result = [receiver]
                while curr_node != sender:
                    result.append(curr_node)
                    curr_node = prev_dict[curr_node]
                result.append(sender)
                return result[::-1]
            elif neighbour_node not in prev_dict:
                prev_dict[neighbour_node] = curr_node
                queue.append(neighbour_node)

    raise Exception



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# This is a graph traversal problem.
# To find the shortest message, we want to use BFS
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        network = {
            'Min'     : ['William', 'Jayden', 'Omar'],
            'William' : ['Min', 'Noam'],
            'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
            'Ren'     : ['Jayden', 'Omar'],
            'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
            'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
            'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
            'Noam'    : ['Nathan', 'Jayden', 'William'],
            'Omar'    : ['Ren', 'Min', 'Scott'],
        }
        self.assertEqual(
            send_msg(network, 'Jayden', 'Adam'), ['Jayden', 'Amelia', 'Adam']
        )

if __name__ == '__main__':
    unittest.main()


