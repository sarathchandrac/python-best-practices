import random
import string
from abc import ABC, abstractmethod
from typing import List


class SupportTicket:
    id: str
    customer: str
    issue: str
    
    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def generate_id(length=8):
    #helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list

class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        return reversed(list_copy)

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy
        

        
class CustomerSupport:
    tickets: List[SupportTicket] = []
    
    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer=customer, issue=issue))
        
    def process_tickets(self, processing_strategy:TicketOrderingStrategy):

        ticket_list = processing_strategy.create_ordering(self.tickets)

        # if it's empty, don't do anyting
        if len(ticket_list) == 0:
            print("There are no tickets to process.")
            return
        # create the ordered list
        for ticket in ticket_list:
            self.process_ticket(ticket)
    
    def process_ticket(self, ticket: SupportTicket):
        print("===================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("===================================")


#Testing
app = CustomerSupport()

#register few tickets
app.create_ticket("John Smith", "My Computer makes strange sounds")
app.create_ticket("Louis Sebastian", "I can't upload videos, please help")
app.create_ticket("Arjan Egges", "VS Code not customizable for typing")

app.process_tickets(RandomOrderingStrategy())
