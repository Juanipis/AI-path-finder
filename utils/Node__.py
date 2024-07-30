# %load utils/Node.py
# %%writefile utils/Node.py
class Node():
    def __init__(self, location, parent=None, get_childrens_states_fn=None):
        self.location = location
        self.parent = parent
        self.children = []
        self.get_childrens_states_fn = get_childrens_states_fn
    
    def add_child(self, state):
        child = type(self)(location=state, parent=self, get_childrens_fn=self.get_childrens_fn)
        
    
    def generate_children(self):
        if self.get_childrens_states_fn:
            children_states = get_childrens_states_fn(self.location)
            for state in children:
                if not self.is_ancestor(state):
                    add_child(state)
    
    def is_ancestor_state(self, state):
        current = self.location
        while current:
            if (current  == state): 
                return True
            current = current.parent
        return False

    
    # # def __init__(self, state, value, operators, operator=None, parent=None, objective=None):
    # def __init__(self, state, value, get_childrens_fn, operator=None, parent=None, objective=None):
    #     self.state = state
    #     self.value = value
    #     self.children = []
    #     self.parent = parent
    #     self.operator = operator
    #     self.objective = objective
    #     self.level = 0
    #     self.get_childrens_fn = get_childrens_fn

    # def add_child(self, value, state, operator):
    #     node = type(self)(value=value, state=state, operator=operator, parent=self, operators=self.operators)
    #     node.level = node.parent.level + 1
    #     self.children.append(node)
    #     return node

    # def add_node_child(self, node):
    #     node.level = node.parent.level + 1
    #     self.children.append(node)
    #     return node

    # def generate_children(self):
    #     if self.get_childrens_fn:
    #         return self.get_childrens_fn(self.state)
    #     return []
    
    # def to_string(self):
    #     return str(state)

    # #Devuelve todos los estados según los operadores aplicados
    # def get_childrens(self):
    #     return [
    #         self.get_state(i)
    #         if not self.repeat_state_path(self.get_state(i))
    #             else None for i, op in enumerate(self.operators)]

    # def get_state(self, index):
    #     if index > len(self.operators):
    #         return None
    #     return self.operators[index]

    # def __eq__(self, other):
    #     return self.state == other.state

    # def __lt__(self, other):
    #     return self.f() < other.f()

    # def repeat_state_path(self, state):
    #     n = self
    #     while n is not None and n.state != state:
    #         n = n.parent
    #     return n is not None

    # def path_objective(self):
    #     n = self
    #     result = []
    #     while n is not None:
    #         result.append(n)
    #         n = n.parent
    #     return result

    # def heuristic(self):
    #     return 0

    # def cost(self):
    #     return 1

    # def f(self):
    #     return self.cost() + self.heuristic()
