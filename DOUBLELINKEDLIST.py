class node:
    def __init__(self,da):
        self.data=da
        self.next=None
        self.prev=None
        
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
        
    def create(self,val):
        self.count+=1
        if self.head==None:
            self.head=node(val)
            self.tail=self.head
        else:
            t=node(val)
            t.next=self.head
            self.head.prev=t
            self.head=t
            
    def inlast(self,val):
        self.count+=1
        if self.head==None:
            self.head=node(val)
            self.tail=self.head
        else:
            t=node(val)
            self.tail.next=t
            t.prev=self.tail
            self.tail=t
            
    def inmid(self,val,s):
        self.count+=1
        if self.head==None:
            self.head=node(val)
            self.tail=self.head
        else:
            t=self.head
            while t.data!=s and t.next!=None:
                t=t.next
            t1=node(val)
            if t.next!=None:
                t2=t.next
                t.next=t1
                t1.prev=t
                t2.prev=t1
                t1.next=t2
            elif t.data==s:
                t.next=t1
                t1.prev=t
    
    def de(self,val):
        self.count-=1
        if self.head.data==val :
            self.head=self.head.next
            if self.head:
                self.head.prev=None
        elif self.tail.data==val:
            self.tail=self.tail.prev
            self.tail.next=None
        else:
            t=self.head
            t1=self.tail
            while(t.data!=val and t1.data!=val):
                t=t.next
                t1=t1.prev
            if t.data==val:
                t1=t.prev
                t2=t.next
                t1.next=t2
                t2.prev=t1
            else:
                t=t1.prev
                t2=t1.next
                t.next=t2
                t2.prev=t
        
    def rec(self,e,o,temp,pre):#difference of sum of evens and odds
        if temp==pre or temp.next==pre:
            if temp.data%2==0 and pre.data%2==0 and temp!=pre:
                e=e+temp.data+pre.data
            elif temp.data%2==0 and temp!=pre:
                e+=temp.data
                o+=pre.data
            elif pre.data%2==0 and temp!=pre:
                e+=pre.data
                o+=temp.data
            elif pre.data%2==0:
                e+=pre.data
            else:
                o+=pre.data
            print("\nEO DIFF=",abs(e-o))
        elif temp.data%2==0 and pre.data%2==0:
            return self.rec(e+temp.data+pre.data,o,temp.next,pre.prev)
        elif temp.data%2==0 :
            return self.rec(e+temp.data,o+pre.data,temp.next,pre.prev)
        elif pre.data%2==0:
            return self.rec(e+pre.data,o+temp.data,temp.next,pre.prev)
        else:
            return self.rec(e,o+temp.data+pre.data,temp.next,pre.prev)
        
    def pr(self,n,c): #CHECK PRIME OR NOT UNSING REC
        if n==0 or n==1 or n==2 or n==3:
            return 1
        elif n%c==0:
            return 0
        elif n//2==c:
            return 1
        else:
            return self.pr(n,c+1)
        
        
    def prime(self,c,temp,pre):#NO.OF PRIMES
        if temp==pre or temp.next==pre:
            if self.pr(temp.data,2) and self.pr(pre.data,2) and temp!=pre:
                print("\n NO.OF PRIMES=",c+2)
            elif  self.pr(temp.data,2) or self.pr(pre.data,2):
                print("\n NO.OF PRIMES=",c+1)
            else:
                print("\n NO.OF PRIMES=",c)
        elif self.pr(temp.data,2) and self.pr(pre.data,2):
            return self.prime(c+2,temp.next,pre.prev)
        elif self.pr(temp.data,2) or self.pr(pre.data,2):
            return self.prime(c+1,temp.next,pre.prev)
        else:
            return self.prime(c,temp.next,pre.prev)
    
    def rev(self):
        t=self.head
        t1=self.tail
        for i in range(self.count//2):
            t.data,t1.data=t1.data,t.data
            t1=t1.prev
            t=t.next
        print("\nREVERSE=")
        self.display(self.head)
    def display(self,t):
        if t!=None:
            print(t.data,end=" ")
            self.display(t.next)
dl=dll()
for i in range(14):    
    dl.create(i+1)
dl.display(dl.head)
print("\n")
dl.de(5)
dl.display(dl.head)
dl.rev()
print("\n")
dl.de(3)
dl.display(dl.head)
dl.de(1)
print("\n")
dl.display(dl.head)
for i in range(5):    
    dl.inlast(i+1)
print("\n")
dl.display(dl.head)
dl.rev()
dl.prime(0,dl.head,dl.tail)
dl.rec(0,0,dl.head,dl.tail)