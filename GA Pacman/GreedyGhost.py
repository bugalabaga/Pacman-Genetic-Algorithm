from Enemy import Ghost

class GreedyGhost(Ghost):
    def __init__(self,pacman,ghostColor,nodeMap):
        Ghost.__init__(self,pacman,ghostColor,nodeMap)
        self.createDict()

    #creates the graph for UCS function
    def createDict(self):
        nodeList = self.map.nodeList
        self.verticeCount = len(nodeList)
        self.dict = {}
        for node in nodeList:
        
            if nodeList.index(node) not in self.dict:
                    self.dict[nodeList.index(node)] = []

            if node.up is not None:
                self.dict[nodeList.index(node)].append(nodeList.index(node.up))
            if node.right is not None:
                self.dict[nodeList.index(node)].append(nodeList.index(node.right))
            if node.down is not None:
                self.dict[nodeList.index(node)].append(nodeList.index(node.down))
            if node.left is not None:
                self.dict[nodeList.index(node)].append(nodeList.index(node.left))


    def sort(self, list):
        l = len(list)
        for i in range(0, l):
            for j in range(0, l-i-1):
                if (list[j][1] > list[j + 1][1]):
                    temp = list[j]
                    list[j]= list[j + 1]
                    list[j + 1]= temp
        return list

    def checkTuple(self, node, list):
        for i in list:
            if i[0] == node[0]:
                return (True,list.index(i))
        return (False,-1)


    #UCS algorithm
    def findPath(self, startNode: int, destination: int) :
        nodeList = self.map.nodeList
        distList = []
        path = [startNode]
        for node in self.dict[startNode]:
            distList.append((node, abs((nodeList[node].vector-nodeList[destination].vector).magnitude())))
        self.sort(distList)
        path.append(distList[0][0])
        self.path = path
            
    #converts path found into moves for the Ghost
    def moveSet(self):
        try:
            goalNode = self.map.nodeList[self.path[1]]
        except:
            goalNode = None
        match goalNode:
            case None:
                return -1
            case self.position.up:
                return 0
            case self.position.right:
                return 1
            case self.position.down:
                return 2
            case self.position.left:   
                return 3    

    def checkNode(self):
        self.move = self.moveSet()
        
        match self.move:
            case -1:
                pass
            case 0:
                if self.position.up != None:
                    self.last = self.position
                    self.position = self.position.up
            case 1:
                if self.position.right != None:
                    self.last = self.position
                    self.position = self.position.right
            case 2:
                if self.position.down != None:
                    self.last = self.position
                    self.position = self.position.down
            case 3:
                if self.position.left != None:
                    self.last = self.position
                    self.position = self.position.left
