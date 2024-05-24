def is_lucky(ticket):
    ticket_str = str(ticket).zfill(6)
    first_half = ticket_str[:3]
    second_half = ticket_str[3:]
    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)
    return ticket_str if sum_first_half == sum_second_half else None


def count_lucky_tickets(start, end):
    lucky_tickets = []
    for ticket in range(start, end + 1):
        lucky_ticket = is_lucky(ticket)
        if lucky_ticket:
            lucky_tickets.append(lucky_ticket)
    with open("lucky_tickets.txt", "w") as file:
        file.write("all_lucky_tickets = [\n")
        for ticket in lucky_tickets:
            file.write(f"{ticket},\n")
        file.write("]")
    return len(lucky_tickets)


# Ввод начального и конечного значения диапазона
start = int(input().strip())
end = int(input().strip())

# Подсчёт и вывод количества счастливых билетов
lucky_count = count_lucky_tickets(start, end)
print("Количество счастливых билетов:", lucky_count)
