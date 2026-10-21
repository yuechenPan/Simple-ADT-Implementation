class nil:
    def __init__(self):
        self.parent = None
        self.l_child = None
        self.r_child = None

    def __str__(self):
        return 'nil'

    def height(self):
        return 0

    def is_leaf(self):
        return False

    def size(self):
        return 0

nil = nil()

class Node:
    def __init__(self,value,parent = nil, l_child = nil , r_child = nil):
        self.value = value
        self.parent = parent
        self.l_child = l_child
        self.r_child = r_child

    def __str__(self):
        return "Node {0}".format(self.value)

    def is_leaf(self):
        return self.r_child is nil and self.l_child is nil

    def height(self):
        return 1 + max(self.l_child.height(),self.r_child.height())

    def size(self):
        if self.is_leaf():
            return 1
        elif self == nil:
            return 0
        else:
            return 1 + self.l_child.size() + self.r_child.size()

    def swap_node(self,other):
        tmp = self.value
        self.value = other.value
        other.value = tmp

    def max_heapify(self):
        def cond_swap(node,a,b):
            if not (node.value >= a.value and node.value >= b.value):
                if a.value >= b.value:
                    node.swap_node(a)
                else:
                    node.swap_node(b)
        if self.is_leaf():
            return
        elif self.l_child is not nil and self.r_child is nil:
            cond_swap(self,self.l_child,self.l_child)
        elif self.l_child is nil and self.r_child is not nil:
            cond_swap(self,self.r_child,self.r_child)
        else:
            l = self.l_child
            r = self.r_child
            cond_swap(self,l,r)

def print_tree(t):
    def output(node,indent):
        if node.is_leaf():
            print(' '*4*indent + '--' + '{0}'.format(node.value) + '\n')
        elif node.l_child is nil and node.r_child is not nil:
            print(' '*4*indent + '--' + '{0}'.format(node.value) + '\n')
            output(node.r_child,indent + 1)
        elif node.l_child is not nil and node.r_child is nil:
            output(node.l_child,indent + 1)
            print(' '*4*indent + '--' + '{0}'.format(node.value) + '\n')
        else:
            output(node.l_child,indent + 1)
            print(' '*4*indent + '--' + '{0}'.format(node.value) + '\n')
            output(node.r_child,indent + 1)
    return output(t.root,0)
          
    

class BST():
    def __init__(self,array = []):
        self.array = array
        self.root = nil
        for i in array:
            self.insert(i)

    def __str__(self):
        return "A Binary Search Tree of {0}".format(self.array)

    def __repr__(self):
        return "BST()"

    
    def insert(self,x):
        if self.root == nil:
            self.root = Node(x)
            return

        current = self.root
        while True:
            if x <= current.value:
                if current.l_child is nil :
                    current.l_child = Node(x, parent=current)
                    return
                
                else:
                    current = current.l_child

            else:
                if current.r_child is nil:
                    current.r_child = Node(x, parent=current)
                    return
                
                else:
                    current = current.r_child

    def height(self):
        return self.root.height()

    def size(self):
        return self.root.size()

    def l_subtree(self):
        sub = BST()
        sub.root = self.root.l_child
        return sub

    def r_subtree(self):
        sub = BST()
        sub.root = self.root.r_child
        return sub

    def is_AVL(self):
        if self.root.is_leaf():
            return True
        elif self.root is nil:
            return True
        else:
            if abs(self.root.l_child.height() - self.root.r_child.height()) <= 1:
                return self.l_subtree().is_AVL() and self.r_subtree().is_AVL()
            else:
                return False
        

b = BST([3,1,4,1,5,9,2,6])
c= BST([3,1,4])
print_tree(b)
print(b.is_AVL())
print(c.is_AVL())


class heap:
    def __init__(self,array = []):
        self.root = nil
        self.data = []
        for i in array:
            self.insert(i)

    def insert(self,x):
        if self.root == nil:
            self.root = Node(x)
            self.data.append(x)
            return
        index = bin(len(self.data) + 1)[2:]
        current = self.root
        for i in range(1,len(index) - 1):
            if index[i] == '0' :
                current = current.l_child
            else:
                current = current.r_child
        if index[len(index) - 1] == '0':
            current.l_child = Node(value = x, parent = current)
        else:
            current.r_child = Node(value = x, parent = current)
        self.data.append(x)

    def l_subtree(self):
        sub = heap()
        sub.root = self.root.l_child
        return sub

    def r_subtree(self):
        sub = heap()
        sub.root = self.root.r_child
        return sub
    
    def is_maxheap(self):
        if self.root.is_leaf():
            return True
        if self.root.value >= self.root.l_child.value and self.root.value >= self.root.r_child.value:
            return self.l_subtree.is_maxheap() and self.r_subtree.is_maxheap()
        else:
            return False

    def maxify(self):
        def partial_maxify(node):
            if node == nil:
                return
            partial_maxify(node.l_child)
            partial_maxify(node.r_child)
            node.max_heapify()
        return partial_maxify(self.root)




    



