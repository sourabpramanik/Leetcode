#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    #Your code here
    if not root or not root.next:
        return root
    
    flatten(root.next)
    
    return merge(root, root.next)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
        
    l1=left
    l2=right
    res=Node(0)
    tmp=res
    while l1 and l2:
        
        if l1.data<=l2.data:
            tmp.bottom = l1
            tmp = tmp.bottom
            l1=l1.bottom
        else:
            tmp.bottom = l2
            tmp = tmp.bottom
            l2=l2.bottom
        
        
    
    if l1:
        tmp.bottom=l1
    
    if l2:
        tmp.bottom=l2
        
        
    return res.bottom
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()


if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag == 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 == 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        root=flatten(head)
        printList(root)
        
        t-=1
            
# } Driver Code Ends