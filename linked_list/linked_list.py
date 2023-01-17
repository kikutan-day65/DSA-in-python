"""
time complexity:             
    - appending the elemnt: O(1)
    - remove elemnt at the end: O(n) cuz needed to iterate through the linked list
    - add at the front: O(1)
    - remove element at the front: O(1)
    - insert the element: O(n)
    - remove the elemnt in the middle: O(n)
    - look up the element: O(n)
"""

"""
What is nodes?
    - value & pointer [4]->

    - node is like a nested dictionary:
        node = {
                "value": 4,
                "next": pointer
               }
    
    - exmaple:

        [11]->[3]->[23]->[4]->None

    head = {
            "value": 11,
            "next": {
                "value": 3,
                "next": {
                    "value": 23,
                    "next": {
                        "value": 4,
    tail -------------> "next": None
                    }
                }
            }
        }
"""

head = {
            "value": 11,
            "next": {
                "value": 3,
                "next": {
                    "value": 23,
                    "next": {
                        "value": 4,
                        "next": None
                    }
                }
            }
        }

print(head["value"])
print(head["next"]["value"])
print(head["next"]["next"]["value"])
print(head["next"]["next"]["next"]["value"])
print()