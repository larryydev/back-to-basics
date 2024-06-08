class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = TNode(data)
        if not self.root:
            self.root = node
        else:
            self._insert(self.root, node)

    def insert_iterative(self, data):
        newNode = TNode(data)

        if not self.root:
            self.root = newNode
            return 
        
        cur = self.root

        while True:
            if data >= cur.data:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = newNode
                    return
            elif data < cur.data:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = newNode
                    return
            

    def search(self, data):
        cur = self.root

        while cur:
            if data == cur.data:
                return True
            if data >= cur.data:
                if cur.right:
                    cur = cur.right
                else:
                    return False
            elif data < cur.data:
                if cur.left:
                    cur = cur.left
                else:
                    return False
        return False

    def min(self):
        if self.root:
            cur = self.root
            while cur.left:
                cur = cur.left
            return cur.data

    def max(self):
        if self.root:
            cur = self.root
            while cur.right:
                cur = cur.right
            return cur.data

    def remove(self, data):
        if not self.root:
            return

        if data == self.root.data:
            return self.remove_root()
        
        cur = self.root
        prev_node = None

        while True:
            if data >= cur.data:
                if cur.right:
                    prev_node = cur
                    cur = cur.right
                else:
                    break
            elif data < cur.data:
                if cur.left:
                    prev_node = cur
                    cur = cur.left
                else:
                    break
            else:
                break

        # case 1: if cur is a leaf node
        if not cur.left and not cur.right:
            if cur == prev_node.left:
                prev_node.left = None
            else:
                prev_node.right = None
        
        # case 2: if cur has one child
        if not cur.left and cur.right:
            if cur == prev_node.left:
                prev_node.left = cur.right
            else:
                prev_node.right = cur.right
        if cur.left and not cur.right:
            if cur == prev_node.left:
                prev_node.left = cur.left
            else:
                prev_node.right = cur.left

        # case 3: if cur has two children 
        if cur.left and cur.right:
            lowest_right_sub = self._find_lowest_right_sub(cur)
            if cur == prev_node.left:
                prev_node.left = lowest_right_sub
            else:
                prev_node.right = lowest_right_sub
            lowest_right_sub.left = cur.left
            lowest_right_sub.right = cur.right
        
    
    def remove_root(self):
        ret = self.root

        lowest_right_sub = self._find_lowest_right_sub(self.root)

        lowest_right_sub.left = self.root.left
        lowest_right_sub.right = self.root.right
        self.root = lowest_right_sub

        return ret.data
    
    def _find_lowest_right_sub(self, root):
        cur = root
        prev_node = None

        if cur.right:
            prev_node = cur
            cur = cur.right
            while cur.left:
                prev_node = cur
                cur = cur.left

        next_right = cur.right if cur.right else None

        if next_right:
            prev_node.left = next_right
        else:
            prev_node.left = None

        return cur

    def inorder(self):
        l = []

        cur = self.root
        stack = []

        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                l.append(cur.data)
                cur = cur.right
            else:
                break

        print(l)

    def preorder(self):
        l = []

        cur = self.root
        stack = []

        while True:
            if cur:
                stack.append(cur)
                l.append(cur.data)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                cur = cur.right
            else:
                break

        print(l)

    def postorder(self):
        l = []

        cur = self.root
        visited = set()

        while cur and cur not in visited:
            if cur.left and cur.left not in visited:
                cur = cur.left
            elif cur.right and cur.right not in visited:
                cur = cur.right
            else:
                l.append(cur.data)
                visited.add(cur)
                cur = self.root
                
        print(l)

    def _insert(self, root, node):        
        if node.data >= root.data:
            if not root.right:
                root.right = node
                return
            else:
                self._insert(root.right, node)
        else:
            if not root.left:
                root.left = node
                return
            else:
                self._insert(root.left, node)



if __name__ == '__main__':
    b = BST()


    b.insert_iterative(10)
    b.insert_iterative(5)
    b.insert_iterative(100)
    b.insert_iterative(50)
    b.insert_iterative(6)
    b.insert_iterative(1)
    b.insert_iterative(70)
    b.insert_iterative(20)
    b.insert_iterative(40)
    b.insert_iterative(80)
    b.insert_iterative(15)




    print()
    b.remove(10)
    print()
    b.remove(15)
    print()



    # print(b.max())
    # print(b.min())


    # print(b.search(2))
    # print(b.search(1000))
    # print(b.search(700))
    # print(b.search(200))
    # print(b.search(350))

    # print(b.search(10))
    # print(b.search(5))
    # print(b.search(100))
    # print(b.search(50))
    # print(b.search(6))
    # print(b.search(1))


    b.inorder()
    b.preorder()
    b.postorder()

