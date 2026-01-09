class Ticket:
    def __init__(self,ticket_id,customer_name,issue,priority):
        self.ticket_id=ticket_id
        self.customer_name=customer_name
        self.issue=issue
        self.priority=priority

class TicketQueue:
    def __init__(self):
       self.critical=[]
       self.high=[]
       self.normal=[]


    def add_ticket(self,ticket):
        if ticket.priority == "CRITICAL":
            self.critical.append(ticket)
        elif ticket.priority == "HIGH":
            self.high.append(ticket)
        else:
            self.normal.append(ticket)

        print("Ticket added:", ticket.ticket_id)
        

    def resolve_ticket(self):
        if self.critical:
            t = self.critical.pop(0)
        elif self.high:
            t = self.high.pop(0)
        elif self.normal:
            t = self.normal.pop(0)
        else:
            print("No tickets to resolve")
            return

        print("Resolved ticket:", t.ticket_id)


    def cancel_ticket(self,ticket_id):
        for q in[self.critical,self.high,self.normal]:
            for i in range(len(q)):
                if q[i].ticket_id==ticket_id:
                    q.pop(i)
                    print('cancelled ticket',ticket_id)
                    return
        print("Ticket not found")


    def find_ticket(self, ticket_id):
        pos = 1
        for q in [self.critical, self.high, self.normal]:
            for t in q:
                if t.ticket_id == ticket_id:
                    print("Ticket position:", pos)
                    return
                pos += 1
        print("Ticket not found")


    def list_tickets(self):
        if not (self.critical or self.high or self.normal):
            print("Queue empty")
            return

        for t in self.critical:
            print( t.customer_name)
        for t in self.high:
            print(t.customer_name)
        for t in self.normal:
            print( t.customer_name)


system = TicketQueue()

system.add_ticket(Ticket(1,"C1","Issue","CRITICAL"))
system.add_ticket(Ticket(2,"C2","Issue","CRITICAL"))
system.add_ticket(Ticket(3,"H1","Issue","HIGH"))
system.add_ticket(Ticket(4,"H2","Issue","HIGH"))
system.add_ticket(Ticket(5,"N1","Issue","NORMAL"))
system.add_ticket(Ticket(6,"N2","Issue","NORMAL"))

system.list_tickets()

print("\nAdding C3\n")
system.add_ticket(Ticket(7,"C3","Issue","CRITICAL"))

system.list_tickets()

    




        