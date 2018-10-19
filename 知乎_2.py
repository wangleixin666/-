# coding:utf-8


class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    # 层次遍历
    def lookup(self):
        queue = [self]
        l = []
        while queue:
            current = queue.pop(0)
            l.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return l

    # 分层打印树
    def printLevel(self):
        currentLevel=[self]
        val=[]
        while currentLevel:
            val.append([c.data for c in currentLevel])
            nextLevel=[]
            for i in currentLevel:
                if i.left:
                    nextLevel.append(i.left)
                if i.right:
                    nextLevel.append(i.right)
            currentLevel=nextLevel
        return val

    def __str__(self):
        s = self.printLevel()
        return '%s'%s

tree=Node(0,
        Node(1,
            Node(3,
                Node(7),
                Node(8)),
            Node(4,
                Node(9),
                Node(10))),
        Node(2,
            Node(5,
                Node(11),
                Node(12)),
            Node(6,
                Node(13),
                Node(14)))
        )

tree2=Node(0,
        Node(1,
            Node(3,
                Node(7),
                Node(8)),
            ),
        Node(2,
            Node(5,
                Node(11),
                Node(12)),
            Node(6))
        )


print(tree.lookup())
print(tree.printLevel())
