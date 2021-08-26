class Node():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        if self.left is None:
            left = "None"
        else:
            left = self.left.key
        if self.right is None:
            right = "None"
        else:
            right = self.right.key
        return "Key = " + str(self.key) + ",left = " + str(left) + ",right = " + str(
            right)


def create_tree(my_tree: Node, n: int):
    cnt = -1

    def create(my_tree=my_tree, n=n + 1):
        nonlocal cnt

        if n == 0:
            return
        my_tree = Node(cnt + 1)
        cnt = cnt + 1
        my_tree.left = create(my_tree.left, int(n / 2))
        my_tree.right = create(my_tree.right, int(n - (n / 2) - 1))

        return my_tree

    return create()


def show_tree(node, level=0):
    if node != None:
        show_tree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.key)
        show_tree(node.right, level + 1)


def PrefixOrder(node):
    if node != None:
        print(str(node.key) + " ", end="")
        PrefixOrder(node.left)
        PrefixOrder(node.right)


def PostfixOrder(node):
    if node != None:
        PostfixOrder(node.left)
        PostfixOrder(node.right)
        print(str(node.key) + " ", end="")


def InfixOrder(node):
    if node != None:
        InfixOrder(node.left)
        print(str(node.key) + " ", end="")
        InfixOrder(node.right)


def show_tree_before(node: Node, h: int = 0):
    if node == None:
        return
    i = 1
    while i <= h:
        print(" ", end=""),
        i += 1
    print(node.key)

    if node.left is not None:
        show_tree_before(node.left, h + 2)
    if node.right is not None:
        show_tree_before(node.right, h + 2)


## part 2

def CreateRootBST(key: int):
    return Node(key)


def SearchNodeBST(node, key: int):
    x = node
    if node.key == key:
        return node
    elif node.key < key:
        x = node.right
    else:
        x = node.left
    if x is None:
        return node
    return SearchNodeBST(x, key)


# if node.key==key:return node
# elif node.key < key: x=node.left
# else:x= node.right
# if x is None: return node
# return SearchNodeBST(x,key)


def InsertNodeBST(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif root.key < key:
            root.right = InsertNodeBST(root.right, key)
        else:
            root.left = InsertNodeBST(root.left, key)
    return root


def SuccessorNodeBST(node):
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left
        return node


def PredecessorNodeBST(node):
    if node.left is not None:
        node = node.left
        while node.right is not None:
            node = node.right
        return node


def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


def DeleteNodeBST(node, key):
    if node is None:
        return node
    if key < node.key:
        node.left = DeleteNodeBST(node.left, key)
    elif (key > node.key):
        node.right = DeleteNodeBST(node.right, key)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp

        elif node.right is None:
            temp = node.left
            node = None
            return temp
        temp = minValueNode(node.right)
        node.key = temp.key
        node.right = DeleteNodeBST(node.right, temp.key)
    return node
