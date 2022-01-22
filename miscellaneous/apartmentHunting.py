"""  
Problem Statement — You're looking to move into a new apartment, and you're given a list of blocks where each block contains some services that it offers. In order to pick your apartment, you want to optimize its location in such a way that the maximum distance to any services that you care for is minimized.
Example —

blocks = [ 
    { “gym” : true, “school” : true, “store” : false } ,
    { “gym” : true, “school” : true, “store” : false } ,
    { “gym” : true, “school” : true, “store” : false } ,
    { “gym” : true, “school” : true, “store” : false } ,
    { “gym” : true, “school” : true, “store” : false } 
]

requirements = [ “gym”, “school”, “store” ]
"""


def apartment_hunting(blocks: list[dict[str, bool]], requirements: list[str]) -> int:
    """
    make passes through the blocks once from left to right and once from right to left
    and keep track of the index of the closest required amenity for each block
    """

    mapping = {k: [float("inf")] * len(blocks) for k in requirements}

    for req in requirements:
        closest_required_index = float("inf")
        # scan from left to right
        for i in range(1, len(blocks)):
            print(f"{blocks[i][req] = }, {i = }, { req = }")
            if blocks[i][req]:
                closest_required_index = i

            mapping[req][i] = abs(i - closest_required_index)

        closest_required_index = float("inf")

        # scan from right to left
        for i in reversed(range(len(blocks))):
            if blocks[i][req]:
                closest_required_index = i

            mapping[req][i] = min(mapping[req][i], abs(i - closest_required_index))

    # now get the max of all and then return the min


apartment_hunting(
    [
        {"gym": False, "school": True, "store": False},
        {"gym": True, "school": False, "store": False},
        {"gym": True, "school": True, "store": False},
        {"gym": False, "school": True, "store": False},
        {"gym": False, "school": True, "store": True},
    ],
    ["gym", "school", "store"],
)
