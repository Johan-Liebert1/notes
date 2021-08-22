"""  
DFS METHOD

Given an array of tasks and an array of task dependencies, find the practical order in which the 
tasks can be completed.

ex = tasks = [1,2,3]
task dependencies = [[2,1], [3,2]]
[2,1] <=> 1 is dependent on 2 being completed, i.e. 2 is a prerequisite for 1
"""


class JobNode:
    def __init__(self, job) -> None:
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False


class JobGraph:
    def __init__(self, jobs) -> None:
        self.nodes: "list[JobNode]" = []
        self.graph: "dict[int, JobNode]" = {}

        for job in jobs:
            self.add_node(job)

    def add_node(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def add_prereq(self, job, prereq):
        job_node = self.get_node(job)
        prereq_node = self.get_node(prereq)

        job_node.prereqs.append(prereq_node)

    def get_node(self, job) -> JobNode:
        if job not in self.graph:
            self.add_node(job)

        return self.graph[job]


def create_job_graph(jobs, deps):
    graph = JobGraph(jobs)

    # [x, y] : x = prereq, y = job
    for prereq, job in deps:
        # adding edges
        graph.add_prereq(job, prereq)

    return graph


def dfs_traverse(node: JobNode, ordered_jobs: "list"):
    """
    Traverses a node in DFS manner and returns a bool indicating whether it found a cycle or not
    """
    if node.visited:
        return False

    if node.visiting:
        # we have a cycle
        return True

    node.visiting = True

    for prereq_node in node.prereqs:
        contains_cycle = dfs_traverse(prereq_node, ordered_jobs)

        if contains_cycle:
            return True

    node.visited = True
    node.visiting = False

    ordered_jobs.append(node.job)

    return False


def get_ordered_jobs(graph: JobGraph):
    ordered_jobs = []
    nodes = graph.nodes

    while len(nodes) > 0:
        node = nodes.pop()

        contains_cycle = dfs_traverse(node, ordered_jobs)

        if contains_cycle:
            return []

    return ordered_jobs


def topological_sort_dfs(jobs, deps):
    job_graph = create_job_graph(jobs, deps)
    return get_ordered_jobs(job_graph)
