class Ticket:
    def __init__(self,ticket_id,customer_name,issue,priority):
        self.ticket_id=ticket_id
        self.customer_name=customer_name
        self.issue=issue
        self.priority=priority


class Queue:
    def __init__(self):
        self.front=None
        self.rear=None


    def add(self,ticket):
        if self.rear is None:
            self.front=self.rear=ticket
            return
        self.rear.next=ticket
        self.rear=ticket

    def remove(self):
        if self.front is None:
            return
        temp=self.front
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        temp.next=None
        return temp

        