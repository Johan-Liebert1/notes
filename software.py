class Node:
    def __init__(self, value, components=[]) -> None:
        self.value: int = value
        self.components: list[Node] = components

    def __repr__(self) -> str:
        return f"value {self.value}"


root = Node(
    200, [Node(120, [Node(110), Node(20), Node(30)]), Node(180, [Node(150), Node(80)])]
)


class Helper:
    def __init__(self, num_children: int, children_sum: int) -> None:
        self.num_children = num_children
        self.children_sum = children_sum
        self.average_sum = (children_sum) / (num_children + 1)

    def __repr__(self) -> str:
        return f"num_children = {self.num_children} children_sum = {self.children_sum}, average_sum = {self.average_sum}"


def helper(root: Node, max_avg_sum: list[float, Node | None]) -> Helper:

    if len(root.components) == 0:
        # no children
        h = Helper(0, root.value)
        print("base -> ", root, " -> ", h)
        return h

    # recursively iterate over children of the node and keep track of number of children and node values
    sum_list: list[Helper] = []

    for child in root.components:
        sum_list.append(helper(child, max_avg_sum))

    this_nodes_children_sum = root.value
    total_children = len(root.components)

    for helper1 in sum_list:
        this_nodes_children_sum += helper1.children_sum
        total_children += helper1.num_children

    h = Helper(total_children, this_nodes_children_sum)

    print(root, " -> ", h)

    if h.average_sum > max_avg_sum[0]:
        max_avg_sum[0] = h.average_sum
        max_avg_sum[1] = root

    return h


def fastest_moving_component(root: Node):
    array = [0, None]

    helper(root, array)

    return array[1]


print(fastest_moving_component(root))
