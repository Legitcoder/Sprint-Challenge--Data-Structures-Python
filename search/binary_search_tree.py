class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    if self.left is None and self.right is None:
      cb(self.value)
      return
    node = self
    stack = [node]
    node.visited = True
    cb(node.value)
    while stack:
      if node.left and not hasattr(node.left, "visited"):
        node = node.left
        stack.append(node)
        node.visited = True
        cb(node.value)
      elif node.right and not hasattr(node.right, "visited"):
        node = node.right
        stack.append(node)
        node.visited = True
        cb(node.value)
      else:
        stack.pop()
        if stack: node = stack[-1]

  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
