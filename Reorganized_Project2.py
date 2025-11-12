"""
CS3364 Algorithms: Project 2
By: Kartavya Sharma, Jeremiah Kornbau, Vaishnavi Makkapati, Brandon Gramlich, Amish Bhakta
This program uses the sorting and organizational methods for Topological Ordering
It takes this task on from the Depth First Search method
"""

class Graph:
    def __init__(self):
        """Initialize an empty graph."""
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        
        Args:
            vertex: The vertex to add (typically a string like "CS 1411")
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    "def add_edge(self, from_vertex, to_vertex):"
    def add_edge(self, u, v):
        """
        Add a directed edge from from_vertex to to_vertex.

        """
        if u not in self.adjacency_list:
            self.add_vertex(u)
        if v not in self.adjacency_list:
            self.add_vertex(v)
        
        self.adjacency_list[u].append(v)
    
    def topological_sort(self):
        """
        Perform a topological sort on the graph using DFS.
        
        Returns:
            list: A list of vertices in topological order, or empty list if cycle detected
        """
        visit_state = {vertex: 0 for vertex in self.adjacency_list}
        topological_order = []
        is_dag = True  # Flag to detect cycles
        
        def dfs(vertex):
            """Helper function to perform DFS recursively."""
            nonlocal is_dag
            
            if visit_state[vertex] == 1:
                # Found a cycle (back edge to a node currently in the stack)
                is_dag = False
                return
            
            if visit_state[vertex] == 2:
                # Already visited and processed
                return
            
            visit_state[vertex] = 1  # Mark as Visiting
            
            # Recursively visit all neighbors
            for neighbor in self.adjacency_list[vertex]:
                dfs(neighbor)
            
            visit_state[vertex] = 2  # Mark as Visited (Finished processing)
            
            # Add vertex to the front of the list after all dependents are visited
            topological_order.insert(0, vertex)
        
        # Run DFS on all vertices to ensure complete coverage
        for vertex in self.adjacency_list:
            if visit_state[vertex] == 0:
                dfs(vertex)
        
        # Return empty list if cycle detected
        if not is_dag:
            return []
        
        return topological_order
    
    def display_topological_order(self, order, courses_per_line=4):
        """
        Display the topological order in a formatted way.
        
        Args:
            order: The topological order list
            courses_per_line: Number of courses to display per line
        """
        if not order:
            print("Error: The prerequisites contain a cycle. A valid topological ordering is impossible.")
            return
        
        print("\n Valid Course Sequence (Topological Order): ")
        print("=" * 80)
        
        for i, course in enumerate(order):
            # Print specified number of courses per line
            if i > 0 and i % courses_per_line == 0:
                print()
            print(f"{i+1:02}. {course:<10}", end=" | ")
        
        print("\n" + "=" * 80)
        print("(This represents one of many possible orderings.)\n")


def build_cs_major_graph():
    """
    Build the graph for the program

    Returns:
        Graph: A graph object with all CS major courses and their dependencies
    """
    # Define courses and their prerequisites
    prerequisites = {
        "CS 1411": [],
        "MATH 1451": [],
        "ENGL 1301": [],
        "CS 1412": ["CS 1411"],
        "MATH 1452": ["MATH 1451"],
        "PHYS 1408": ["MATH 1451"],
        "ENGL 1302": ["ENGL 1301"],
        "CS 2413": ["CS 1412"],
        "CS 1382": ["CS 1411"],
        "ECE 2372": ["MATH 1451"],
        "MATH 2450": ["MATH 1452"],
        "PHYS 2401": ["PHYS 1408"],
        "CS 2350": ["CS 1412", "ECE 2372"],
        "CS 2365": ["CS 2413"],
        "ENGR 2392": [],
        "POLS 1301": [],
        "MATH 2360": ["MATH 1452"],
        "ENGL 2311": ["ENGL 1301", "ENGL 1302"],
        "CS 3361": ["CS 2413"],
        "CS 3364": ["CS 2413", "CS 1382", "MATH 2360"],
        "MATH 3342": ["MATH 2450"],
        "POLS 2306": [],
        "CS 3365": ["CS 2365", "CS 2413", "MATH 3342"],
        "CS 3375": ["CS 2350"],
        "CS 3383": ["CS 1382"],
        "CS 4365": ["CS 3365"],
        "CS 4352": ["CS 3364", "CS 3375"],
        "CS 4354": ["CS 3364"],
        "CS 4366": ["CS 4365"]
    }
    
    # Create graph instance
    graph = Graph()
    
    # Add all vertices
    for course in prerequisites:
        graph.add_vertex(course)
    
    # Add edges (prerequisite -> course relationship)
    for course, prereqs in prerequisites.items():
        for prereq in prereqs:
            graph.add_edge(prereq, course)
    
    return graph


def main():
    """
    Main function to demonstrate the Graph ADT with CS major course ordering.
    """
    print("\n" + "="*80)
    print("CS 3364 ALGORITHMS: PROJECT 2")
    print("Topological Ordering of Computer Science Major Courses")
    print("="*80)

    cs_graph = build_cs_major_graph()

    # Get and Print Result
    print(f"Total courses: {len(cs_graph.adjacency_list)}")
    course_order = cs_graph.topological_sort()
    cs_graph.display_topological_order(course_order)
    
    # Additional statistics
    if course_order:
        print(f"Total courses in sequence: {len(course_order)}")
        print(f"\nFirst 5 courses to take:")
        for i in range(min(5, len(course_order))):
            print(f"  {i+1}. {course_order[i]}")
        
        print(f"\nLast 5 courses in the sequence:")
        for i in range(max(0, len(course_order)-5), len(course_order)):
            print(f"  {i+1}. {course_order[i]}")


# Execute the program
if __name__ == "__main__":
    main()

