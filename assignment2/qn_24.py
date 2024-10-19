# 24. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

import random

def generate_lottery(num_tickets):
    tickets = []
    for i in range(num_tickets):
        ticket = random.randint(100000, 999999)
        tickets.append(ticket)
    return tickets

def pick_winners(tickets, num_winners):
    return random.sample(tickets, num_winners)

num_tickets = 100
lottery_tickets = generate_lottery(num_tickets)
lucky_tickets = pick_winners(lottery_tickets, 2)

print("Generated Lottery Tickets:", lottery_tickets)
print("Lucky Tickets:", lucky_tickets)
