class Tree ():
  def __init__(self, root, operators):
    self.root = root
    self.operators = operators

  def printPath(self, n):
    path = n.path_to_objective()
    for i in path:
        if i.operator is not None:
            print(f'operador:  {self.operators[node.operator]} \t estado: {node.state}')
        else:
            print(f' {node.state}')
    
    return path

    # stack = n.path_to_objective()
    # path = stack.copy()
    # while len(stack) != 0:
    #     node = stack.pop()
    #     if node.operator is not None:
    #         print(f'operador:  {self.operators[node.operator]} \t estado: {node.state}')
    #     else:
    #         print(f' {node.state}')
    # return path

  def reinit_root(self):
    self.root.operator = None
    self.root.parent = None
    self.root.objective = None
    self.root.children = []
    self.root.level = 0

  ## Primero a lo ancho
  def breadth_first(self,endState):
    self.reinit_root()
    pq = queue.Queue()
    pq.put(self.root)
    while not pq.empty():
      node = pq.get()
      children = node.get_childrens()
      for i, child in enumerate(children):
        if child is not None:
          newChild = node.add_child(value=node.value + '-' + str(i), state=child, operator=i)
          pq.put(newChild)
          if endState == child:
            return newChild

  ## Primero en profundidad
  def depht_first(self, endState):
    self.reinit_root()
    pq = []
    pq.append(self.root)
    while len(pq) > 0:
      node = pq.pop()
      if (node.parent is not None):
        node.parent.add_node_child(node)
      children = node.get_childrens()
      temp = []
      for i, child in enumerate(children):
        if child is not None:
          newChild = type(self.root)(value=node.value + '-' + str(i), state=child, operator=i, parent=node, operators=node.operators)
          temp.append(newChild)
          if endState == child:
            node.add_node_child(newChild)
            return newChild
      #Adicionar los hijos en forma inversa para que salga primero el primero que se adicionó
      temp.reverse()
      for e in temp:
        pq.append(e)

  ## Costo uniforme
  def uniform_cost(self, endState):
    self.reinit_root()
    pq = queue.PriorityQueue()
    pq.put((self.root.cost(), self.root))
    while not pq.empty():
      node = pq.get()[1]
      children = node.get_childrens()
      for i, child in enumerate(children):
        if child is not None:
          newChild = node.add_child(value=node.value + '-' + str(i), state=child, operator=i)
          pq.put((newChild.cost(), newChild))
          if endState == child:
            return newChild

  ## Primero el mejor
  def best_first(self, endState):
    self.reinit_root()
    pq = queue.PriorityQueue()
    pq.put((self.root.heuristic(), self.root))
    while not pq.empty():
      node = pq.get()[1]
      children = node.get_childrens()
      for i, child in enumerate(children):
        if child is not None:
          newChild = node.add_child(value=node.value + '-' + str(i), state=child, operator=i)
          pq.put((newChild.heuristic(), newChild))
          if endState == child:
            return newChild

  ## A*
  def astar(self, endState):
    self.reinit_root()
    pq = queue.PriorityQueue()
    pq.put((self.root.f(), self.root))
    while not pq.empty():
      node = pq.get()[1]
      children = node.get_childrens()
      for i, child in enumerate(children):
        if child is not None:
          newChild = node.add_child(value=node.value + '-' + str(i), state=child, operator=i)
          pq.put((newChild.f(), newChild))
          if endState == child:
            return newChild

  ## Método para dibujar el árbol
  def draw(self,path):
    graph = pydot.Dot(graph_type='graph')
    nodeGraph = pydot.Node(str(self.root.state) + "-" + str(0),
                          label=str(self.root.state), 
                          shape ="circle",
                          style="filled",
                          fillcolor="red")
    graph.add_node(nodeGraph)
    path.pop()
    return self.draw_tree_rec(self.root, nodeGraph, graph, 0, path.pop(), path)

  ## Método recursivo para dibujar el árbol
  def draw_tree_rec(self, r, rootGraph, graph, i, topPath, path):
    if r is not None:
      children = r.children
      for j,child in enumerate(children):
        i = i + 1
        color="white"
        if topPath.value == child.value:
          if len(path) > 0 : topPath = path.pop()
          color='red'
        c = pydot.Node(child.value, label=str(child.state) + r"\n\n" + "f=" + str(child.f()),
                      shape ="circle",
                      style="filled",
                      fillcolor=color)
        graph.add_node(c)
        graph.add_edge(pydot.Edge(rootGraph, c,
                                  label=str(child.operator) + '(' + str(child.cost()) + ')'))
        graph = self.draw_tree_rec(child, c, graph, i, topPath, path)  # recursive call
      return graph
    else:
      return graph
