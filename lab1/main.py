from Tree import Node, create_tree, show_tree_before, PrefixOrder, show_tree,\
    PostfixOrder, InfixOrder,SearchNodeBST,InsertNodeBST,DeleteNodeBST,topview

if __name__ == '__main__':
    tree = None
    # tree =create_tree(tree,5)
    # print("Create tree:")
    # show_tree(tree)
    # print()
    # PrefixOrder(tree)
    # print()
    # PostfixOrder(tree)
    # print()
    # InfixOrder(tree)
    # print()
    ## part 2
    tree2 = Node(8)
    tree2 =InsertNodeBST(tree2,12)
    tree2 =InsertNodeBST(tree2,4)
    tree2 =InsertNodeBST(tree2,2)
    #
    # print(" BST")
    # show_tree(tree2)
    # print()
    # print("DELETE BST NODE key == 2")
    # tree2 = DeleteNodeBST(tree2,2)
    # print()
    # show_tree(tree2)
    topview(tree2)


