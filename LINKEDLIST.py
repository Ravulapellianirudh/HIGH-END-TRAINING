class node:
    def __init__(self,d):
        self.data=d
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    
    def eo(self):#SLOW POINTER WAY TO FIND LENGTH OF LIST IS EVEN OR ODD
        f=self.head
        s=self.head
        while True:
            if f.next==None:
                print("LIST IS ODD IN LENGTH")
                break
            elif f.next.next==None:
                print("LIST IS EVEN IN LENGTH")
                break
            else:
                s=s.next
                f=f.next.next
    def m(self):#SLOW POINTER WAY
        f=self.head
        s=self.head
        while True:
            if f.next==None:
                print(s.data)
                break
            elif f.next.next==None:
                print(s.data,s.next.data)
                break
            else:
                s=s.next
                f=f.next.next
    def mid(self):#TRADITIONAL WAY TO FIND MID ELEMENTS
        c=0
        t=self.head
        while(t!=None):
            t=t.next
            c+=1
        n=1
        t=self.head
        if c%2==0:
            self.display()
            while(True):
                if n==c//2:
                    print(t.data)
                elif n==(c//2)+1:
                    print(t.data)
                    break
                n+=1
                t=t.next
        else:
            self.display()
            while(True):
                if n==c//2 +1:
                    print(t.data)
                    break
                n+=1
                t=t.next
                    
        
    def las(self):#LAST ELEMENT IN THE LIST
        t=self.head
        while(t.next!=None):
            t=t.next
        return t
    def create(self,val):
        l=node(val)
        l.next=self.head
        self.head=l
    def inlast(self,val):
        if self.head==None:
            self.head=node(val)
        else:
            t=self.head
            while(t.next!=None):
                t=t.next
            t.next=node(val)
    def inmid(self,val,s):
        t=self.head
        while(t!=None):
            if t.data==s and t.next==None:
                t.next=node(val)
                break
            elif t.data==s:
                t1=t.next
                t.next=node(val)
                t=t.next
                t.next=t1
                break
            else:
                t=t.next
        
    def de(self,val):#DELETE ANYTHING BY VALUE
        t=self.head
        while(t.next!=None):
            if t.data==val:
                self.head=t.next
                break
            elif t.next.data==val and not t.next.next:
                t.next=None
                break
            elif t.next.data==val and t.next.next:
                t.next=t.next.next
                break
            else:
                t=t.next
    def search(self,s):
        t=self.head
        c=0
        while(t!=None):
            c+=1
            if t.data==s:
                print(s,"is at",c,"position")
                break
            t=t.next
        else:
            print("ELEMENT ",s," NOT FOUND IN THE LIST")
    def se(self):#HIGHEST SEQUENCE
        t=self.head
        c=1
        m=0
        while(t.next!=None):
            if t.data==t.next.data-1 :
                c+=1
            elif c>m:
                m=c
                c=1
            else:
                c=1
            t=t.next
        if c>m:
            m=c
        print("SEQUENCE=",m)
    def dis(self):#DISPLAY COUPLE PAIRED DATA
        t=self.head
        while(t.next!=None):
            t1=t.next
            while(t1!=None):
                print(t.data,"-",t1.data,",",end=" ")
                t1=t1.next
            print("\n")
            t=t.next
    def bbsort(self):
        print("BUBBLE SORT=")
        p=self.head
        while(p!=None):
            c=0
            t=self.head
            t1=t.next
            while(t1!=None):
                if t.data>t1.data:
                    c=1
                    t.data,t1.data=t1.data,t.data
                t=t.next
                t1=t1.next
            if not c:
                break
            p=p.next
        self.display()
    def ins(self):
        print("INSERTION SORT=")
        t=self.head
        while(t.next!=None):
            t1=t.next
            m=t
            while(t1!=None):
                if m.data>t1.data:
                    m=t1
                t1=t1.next
            if m.data!=t.data:
                m.data,t.data=t.data,m.data
            t=t.next
        self.display()
    def rev(self):
        print("REVERSE=")
        t=self.head
        t1=t.next
        t.next=None
        while(t1.next!=None):
            temp=t1.next
            t1.next=t
            t=t1
            t1=temp
        t1.next=t
        self.head=t1
        self.display()
    def d(self,t):
        print(t.data,end=" ")
        if t.next!=None:
            self.d(t.next)
    def rec(self,e,o,temp):
        if not temp:
            return abs(e-o)
        elif temp.data%2==0:
            return self.rec(e+temp.data,o,temp.next)
        else:
            return self.rec(e,o+temp.data,temp.next)
    def pr(self,n,a):
        if n==0 or n==1 or n==2 or n==3:
            return 1
        elif n%a==0:
            return 0
        elif n//2==a:
            return 1
        else:
            return pr(n,a+1)
    def prime(self,temp,c):
        if not temp:
            print("\nNO.OF PRIMES=",c)
        elif self.pr(temp.data,2):
            self.prime(temp.next,c+1)
        else:
            self.prime(temp.next,c)
        
            
            
            
    def display(self):
        t=self.head
        while t!=None:
            print(t.data,end="  ")
            t=t.next
        self.last=self.las()
        print("LAST=",self.last.data)
ll=sll()
for i in range(5,1,-1):
    ll.inlast((i+1))
ll.inmid(10,3)
ll.create(1)
ll.mid()
ll.m()
ll.eo()
ll.se()
ll.inmid(2,4) 
ll.display()
ll.ins()
ll.bbsort()
ll.rev() 
ll.de(4)
ll.se()
ll.dis()
ll.mid()
ll.m()
ll.eo()
ll.search(60)
ll.search(20)
ll.search(80)
ll.display()
ll.d(ll.head)
k=ll.rec(0,0,ll.head)
print("\nDIFF OF EVEN & ODD SUM=",k)
ll.prime(ll.head,0)