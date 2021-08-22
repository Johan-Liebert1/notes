"""  
SECOND METHOD

1. Create a job graph in which each node has a number that corresponds to the number of prerequisites it has and has an array containing the number of dependencies it has.

2. Iterate through the nodes in the graph and append a node with no prerequisites to the final array.

3. Then Iterate through all the dependencies of that node, and remove the dependency from the dependent nodes and subtract the number of prerequisites

4. Keep doing it until there are no nodes left with zero prereqs

5. Finally check if there are still nodes left with prerequisites, and if there are, then there's a cycle

Given an array of tasks and an array of task dependencies, find the practical order in which the 
tasks can be completed.

ex = tasks = [1,2,3]
task dependencies = [[2,1], [3,2]]
[2,1] <=> 1 is dependent on 2 being completed, i.e. 2 is a prerequisite for 1
"""


class JobNode:
    def __init__(self, job) -> None:
        self.job = job
        self.deps: "list[JobNode]" = []
        self.num_prereqs = 0


class JobGraph:
    def __init__(self, jobs) -> None:
        self.nodes: "list[JobNode]" = []
        self.graph: "dict[int, JobNode]" = {}

        for job in jobs:
            self.add_node(job)

    def add_node(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def add_dep(self, job, dep):
        job_node = self.get_node(job)
        dep_node = self.get_node(dep)

        job_node.deps.append(dep_node)
        dep_node.num_prereqs += 1

    def get_node(self, job) -> JobNode:
        if job not in self.graph:
            self.add_node(job)

        return self.graph[job]


def create_job_graph(jobs, deps):
    graph = JobGraph(jobs)

    # [x, y] : x = prereq, y = job
    for job, dep in deps:
        # adding edges
        graph.add_dep(job, dep)

    return graph


def remove_deps(node: JobNode, nodes_with_no_prereqs: "list[JobNode]"):
    while len(node.deps):
        dep = node.deps.pop()
        dep.num_prereqs -= 1

        if dep.num_prereqs == 0:
            nodes_with_no_prereqs.append(dep)


def get_ordered_jobs(graph: JobGraph):
    ordered_jobs = []
    nodes_with_no_prereqs = list(
        filter(lambda node: node.num_prereqs == 0, graph.nodes)
    )

    while len(nodes_with_no_prereqs) > 0:
        node = nodes_with_no_prereqs.pop()

        # this node has no prereqs so append immediately
        ordered_jobs.append(node.job)
        remove_deps(node, nodes_with_no_prereqs)

    # if there are still nodes that have dependencies then there's a cycle
    graph_has_edges = any(node.num_prereqs for node in graph.nodes)

    return [] if graph_has_edges else ordered_jobs


def topological_sort(jobs, deps):
    job_graph = create_job_graph(jobs, deps)
    return get_ordered_jobs(job_graph)


if __name__ == "__main__":
    print(topological_sort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]))
