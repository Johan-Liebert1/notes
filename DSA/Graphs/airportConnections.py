class AirportNode:
    def __init__(self, airport: str):
        self.airport: str = airport
        self.connections: list[str] = []
        self.isReachable: bool = True
        self.unreachableConnections: list[str] = []


AirportsType = list[str]
RoutesType = tuple[str, str]
AirportGraphType = dict[str, AirportNode]

# O(a * (a + r) + a + r + alog(a)) time | O(a + r) space - where a is the number of airports and r is the number of routes
def airportConnections(
    airports: AirportsType, routes: RoutesType, startingAirport: str
):
    airportGraph = createAirportGraph(airports, routes)
    unreachableAirportNodes = getUnreachableAirportNodes(
        airportGraph, airports, startingAirport
    )
    markUnreachableConnections(airportGraph, unreachableAirportNodes)
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)


# O(a + r) time | O(a + r) space
def createAirportGraph(airports: AirportsType, routes: RoutesType):
    airportGraph: AirportGraphType = {}

    for airport in airports:
        airportGraph[airport] = AirportNode(airport)

    for route in routes:
        airport, connection = route
        airportGraph[airport].connections.append(connection)

    return airportGraph


# O(a + r) time | O(a) space
def getUnreachableAirportNodes(
    airportGraph: AirportGraphType, airports: AirportsType, startingAirport: str
):
    visitedAirports: dict[str, bool] = {}

    # this will add all the visitable airports to the visitedAirports dict
    # so all other airports are not reachable
    depthFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)

    unreachableAirportNodes: list[AirportNode] = []

    for airport in airports:
        if airport in visitedAirports:
            continue

        airportNode = airportGraph[airport]
        airportNode.isReachable = False
        unreachableAirportNodes.append(airportNode)

    return unreachableAirportNodes


def depthFirstTraverseAirports(
    airportGraph: AirportGraphType, airport: str, visitedAirports: dict[str, bool]
):
    if airport in visitedAirports:
        return

    visitedAirports[airport] = True
    connections = airportGraph[airport].connections

    for connection in connections:
        depthFirstTraverseAirports(airportGraph, connection, visitedAirports)


# O(a * (a + r)) time | O(a) space
def markUnreachableConnections(
    airportGraph: AirportGraphType, unreachableAirportNodes: list[AirportNode]
):
    for airportNode in unreachableAirportNodes:
        airport = airportNode.airport
        unreachableConnections = []

        depthFirstAddUnreachableConnections(
            airportGraph, airport, unreachableConnections, {}
        )

        airportNode.unreachableConnections = unreachableConnections


def depthFirstAddUnreachableConnections(
    airportGraph: AirportGraphType,
    airport: str,
    unreachableConnections: list[AirportNode],
    visitedAirports: dict[str, bool],
):
    if airportGraph[airport].isReachable:
        return

    if airport in visitedAirports:
        return

    visitedAirports[airport] = True
    unreachableConnections.append(airport)
    connections = airportGraph[airport].connections

    for connection in connections:
        depthFirstAddUnreachableConnections(
            airportGraph, connection, unreachableConnections, visitedAirports
        )


# O(alog(a) + a + r) time | O(1) space
def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
    unreachableAirportNodes.sort(
        key=lambda airport: len(airport.unreachableConnections), reverse=True
    )

    numberOfNewConnections = 0

    for airportNode in unreachableAirportNodes:
        if airportNode.isReachable:
            continue

        numberOfNewConnections += 1

        for connection in airportNode.unreachableConnections:
            airportGraph[connection].isReachable = True

    return numberOfNewConnections
