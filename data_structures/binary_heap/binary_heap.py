"""
Implement a binary heap
"""
class BinaryHeap:
    def __init__(self, capacity):
        self.customList = capacity * [None]
        self.size = 0
        self.capacity = capacity
    
def peek(heap):
    if heap == None:
        return
    else:
        if heap.size == 0:
            return "Empty heap"
        else:
            return heap.customList[0]

def sizeOfHeap(heap):
    if heap == None:
        return
    else:
        return heap.size

def levelOrderTraversal(heap):
    if heap == None:
        return
    else:
        for i in range(heap.size):
            print(heap.customList[i])

def heapifyNodeInsert(heap, index, heapType):
    if heap == None:
        return
    else:
        if index <= 0:
            return
        parentIndex = int((index-1)/2)
        if heapType == "Min":
            if heap.customList[parentIndex] > heap.customList[index]:
                parentValue = heap.customList[parentIndex]
                heap.customList[parentIndex] = heap.customList[index]
                heap.customList[index] = parentValue
        else:
            if heap.customList[parentIndex] < heap.customList[index]:
                parentValue = heap.customList[parentIndex]
                heap.customList[parentIndex] = heap.customList[index]
                heap.customList[index] = parentValue
        heapifyNodeInsert(heap, parentIndex, heapType)

def insertNode(heap, value, heapType):
    if heap == None:
        return
    else:
        if heap.size + 1 > heap.capacity:
            return "Heap full"
        else:
            heap.customList[heap.size] = value
            heap.size += 1
            heapifyNodeInsert(heap, heap.size-1, heapType)

def heapifyExtractNode(heap, index, heapType):
    if heap == None:
        return
    else:
        leftChildIndex = index * 2 + 1
        rightChildIndex = index * 2 + 2
        swapChildIndex = 0
        if leftChildIndex + 1 > heap.size:
            return
        elif leftChildIndex + 1 == heap.size:
            if heapType == "Min":
                if heap.customList[index] > heap.customList[leftChildIndex]:
                    parentValue = heap.customList[index]
                    heap.customList[index] = heap.customList[leftChildIndex]
                    heap.customList[leftChildIndex] = parentValue
            else:
                if heap.customList[index] < heap.customList[leftChildIndex]:
                    parentValue = heap.customList[index]
                    heap.customList[index] = heap.customList[leftChildIndex]
                    heap.customList[leftChildIndex] = parentValue
            return
        else:
            if heapType == "Min":
                if heap.customList[leftChildIndex] < heap.customList[rightChildIndex]:
                    swapChildIndex = leftChildIndex
                else:
                    swapChildIndex = rightChildIndex
                if heap.customList[index] > heap.customList[swapChildIndex]:
                    parentValue = heap.customList[index]
                    heap.customList[index] = heap.customList[swapChildIndex]
                    heap.customList[swapChildIndex] = parentValue
            else:
                if heap.customList[leftChildIndex] > heap.customList[rightChildIndex]:
                    swapChildIndex = leftChildIndex
                else:
                    swapChildIndex = rightChildIndex
                if heap.customList[index] < heap.customList[swapChildIndex]:
                    parentValue = heap.customList[index]
                    heap.customList[index] = heap.customList[swapChildIndex]
                    heap.customList[swapChildIndex] = parentValue
            heapifyExtractNode(heap, swapChildIndex, heapType)
            

def extractNode(heap, heapType):
    if heap == None:
        return
    else:
        if heap.size == 0:
            return "Empty heap"
        else:
            topNode = heap.customList[0]
            heap.customList[0] = heap.customList[heap.size-1]
            heap.customList[heap.size-1] = None
            heap.size -= 1
            heapifyExtractNode(heap, 0, heapType)
            return topNode

customHeap = BinaryHeap(6)
insertNode(customHeap, 5, "Max")
insertNode(customHeap, 10, "Max")
insertNode(customHeap, 4, "Max")
insertNode(customHeap, 11, "Max")
insertNode(customHeap, 3, "Max")
# levelOrderTraversal(customHeap)
# print(f"**************")
insertNode(customHeap, 22, "Max")
# print(insertNode(customHeap, 12, "Min"))
levelOrderTraversal(customHeap)
print(f"**************")
print(extractNode(customHeap, "Max"))
print(f"**************")
levelOrderTraversal(customHeap)