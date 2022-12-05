from graph import Node, Graph
  

class UCS:
  def __init__(self, graph, start_position, target):
    self.graph = graph
    self.start = graph.find_node(start_position)
    self.target = graph.find_node(target)
    self.opened = []
    self.closed = []
    self.number_of_steps = 0


  def calculate_distance(self, parent, child):
    for neighbor in parent.neighbors:
      if neighbor[0] == child:
        distance = parent.heuristic_value + neighbor[1]
        if distance < child.heuristic_value:
          child.parent = parent
          return distance
        
        return child.heuristic_value

  
  def insert_to_list(self, list_category, node):
    if list_category == "open":
      self.opened.append(node)
    else:
      self.closed.append(node)
  

  def remove_from_opened(self):
    self.opened.sort()
    # for n in self.opened:
    #   print(f"({n},{n.heuristic_value})", end = " ")
    # print("\n")
    node = self.opened.pop(0)
    self.closed.append(node)
    return node


  def opened_is_empty(self):
    return len(self.opened) == 0


  def get_old_node(self, node_value):
    for node in self.opened:
      if node.value == node_value:
        return node
    return None 
      

  def calculate_path(self, target_node):
    path = [target_node.value]
    node = target_node.parent
    while True:
      path.append(node.value)
      if node.parent is None:
        break
      node = node.parent
    path.reverse()
    return path
  
  
  def search(self):
    self.start.heuristic_value = 0
    self.opened.append(self.start)

    while True:
      self.number_of_steps += 1

      if self.opened_is_empty():
        print(f"No Solution Found after {self.number_of_steps} steps!!!")
        break
        
      selected_node = self.remove_from_opened()
    
      if selected_node == self.target:
        path = self.calculate_path(selected_node)
        return path, self.number_of_steps

      new_nodes = selected_node.extend_node()

      if len(new_nodes) > 0:
        for new_node in new_nodes:
          
          new_node.heuristic_value = self.calculate_distance(selected_node, new_node)
          if new_node not in self.closed and new_node not in self.opened:
            self.insert_to_list("open", new_node)
          elif new_node in self.opened and new_node.parent != selected_node:
            old_node = self.get_old_node(new_node.value)
            if new_node.heuristic_value < old_node.heuristic_value:
              new_node.parent = selected_node
              self.insert_to_opened(new_node)