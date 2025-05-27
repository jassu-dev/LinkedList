class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
class Linked_List:
    def __init__(self):
        self.head=None
    def append(self, val):
        if(self.head==None):
            self.head = Node(val)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=Node(val)
    def prepend(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        list_v = self.head
        while list_v:
            print(list_v.val)
            list_v=list_v.next
    def insert_index(self, index, data):
        if(index==0):
            self.prepend(data)
        else:
            last = self.head
            for i in range(index-1):
                if(last.next==None):
                    pass
                last=last.next
            new_node= Node(data)
            new_node.next=last.next
            last.next=new_node
    def __contanis__(self, valu):
        lat = self.head
        while lat:
            if(lat.val == valu):
                return True
            lat = lat.next
        return False
    def __len__(self):
        len_of_list=0
        s=self.head
        while s:
            len_of_list+=1
            s=s.next
        return int(len_of_list)
    def delete(self, data):
        head_pos = self.head
        if(head_pos.val==data):
            self.head = head_pos.next
        else:
            while head_pos:
                if(head_pos.next.val==data):
                    head_pos.next=head_pos.next.next
                    break
                head_pos=head_pos.next
    def pop_s(self, index=None):
        if index is None:
            men = self.head
            while men.next.next:
                men=men.next
            men.next=None
        else:
            last=self.head
            for i in range(index-1):
                if(last.next==None):
                    pass
                last = last.next
            if(last.next==None):
                pass
            else:
                last.next = last.next.next
l1=Linked_List()
l1.append(4)
l1.insert_index(0, 3)
l1.insert_index(0, 5)
l1.insert_index(1, 7)
l1.append(6)
l1.pop_s(1)
l1.display()