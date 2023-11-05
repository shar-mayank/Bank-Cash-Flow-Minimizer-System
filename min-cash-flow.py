class Bank:
    def __init__(self, name, net_amount, types):
        self.name = name
        self.net_amount = net_amount
        self.types = types

def get_min_index(list_of_net_amounts, num_banks):
    min_val = float('inf')
    min_index = -1
    for i in range(num_banks):
        if list_of_net_amounts[i].net_amount == 0:
            continue
        if list_of_net_amounts[i].net_amount < min_val:
            min_index = i
            min_val = list_of_net_amounts[i].net_amount
    return min_index

def get_simple_max_index(list_of_net_amounts, num_banks):
    max_val = float('-inf')
    max_index = -1
    for i in range(num_banks):
        if list_of_net_amounts[i].net_amount == 0:
            continue
        if list_of_net_amounts[i].net_amount > max_val:
            max_index = i
            max_val = list_of_net_amounts[i].net_amount
    return max_index

def get_max_index(list_of_net_amounts, num_banks, min_index, input, max_num_types):
    max_val = float('-inf')
    max_index = -1
    matching_type = ""
    
    for i in range(num_banks):
        if list_of_net_amounts[i].net_amount == 0:
            continue
        if list_of_net_amounts[i].net_amount < 0:
            continue
        common_types = list(list_of_net_amounts[min_index].types.intersection(list_of_net_amounts[i].types))
        if len(common_types) != 0 and max_val < list_of_net_amounts[i].net_amount:
            max_val = list_of_net_amounts[i].net_amount
            max_index = i
            matching_type = common_types[0]
    return max_index, matching_type

def print_ans(ans_graph, num_banks, input):
    print("\nThe transactions for minimum cash flow are as follows:\n")
    for i in range(num_banks):
        for j in range(num_banks):
            if i == j:
                continue
            if ans_graph[i][j][0] != 0 and ans_graph[j][i][0] != 0:
                if ans_graph[i][j][0] == ans_graph[j][i][0]:
                    ans_graph[i][j][0] = 0
                    ans_graph[j][i][0] = 0
                elif ans_graph[i][j][0] > ans_graph[j][i][0]:
                    ans_graph[i][j][0] -= ans_graph[j][i][0]
                    ans_graph[j][i][0] = 0
                    print(f"{input[i].name} pays Rs {ans_graph[i][j][0]} to {input[j].name} via {ans_graph[i][j][1]}")
                else:
                    ans_graph[j][i][0] -= ans_graph[i][j][0]
                    ans_graph[i][j][0] = 0
                    print(f"{input[j].name} pays Rs {ans_graph[j][i][0]} to {input[i].name} via {ans_graph[j][i][1]}")
            elif ans_graph[i][j][0] != 0:
                print(f"{input[i].name} pays Rs {ans_graph[i][j][0]} to {input[j].name} via {ans_graph[i][j][1]}")
            elif ans_graph[j][i][0] != 0:
                print(f"{input[j].name} pays Rs {ans_graph[j][i][0]} to {input[i].name} via {ans_graph[j][i][1]}")
            ans_graph[i][j][0] = 0
            ans_graph[j][i][0] = 0
    print("\n")

def minimize_cash_flow(num_banks, input, index_of, num_transactions, graph, max_num_types):
    list_of_net_amounts = [Bank(input[i].name, 0, input[i].types) for i in range(num_banks)]
    
    for b in range(num_banks):
        amount = 0
        for i in range(num_banks):
            amount += graph[i][b]
        for j in range(num_banks):
            amount += (-1) * graph[b][j]
        list_of_net_amounts[b].net_amount = amount
    
    ans_graph = [[[0, ""] for _ in range(num_banks)] for _ in range(num_banks)]
    num_zero_net_amounts = 0
    
    for i in range(num_banks):
        if list_of_net_amounts[i].net_amount == 0:
            num_zero_net_amounts += 1
    
    while num_zero_net_amounts != num_banks:
        min_index = get_min_index(list_of_net_amounts, num_banks)
        max_index, matching_type = get_max_index(list_of_net_amounts, num_banks, min_index, input, max_num_types)
        
        if max_index == -1:
            ans_graph[min_index][0] = [abs(list_of_net_amounts[min_index].net_amount), input[min_index].types.pop()]
            simple_max_index = get_simple_max_index(list_of_net_amounts, num_banks)
            ans_graph[0][simple_max_index] = [abs(list_of_net_amounts[min_index].net_amount), input[simple_max_index].types.pop()]
            list_of_net_amounts[simple_max_index].net_amount += list_of_net_amounts[min_index].net_amount
            list_of_net_amounts[min_index].net_amount = 0
            if list_of_net_amounts[min_index].net_amount == 0:
                num_zero_net_amounts += 1
            if list_of_net_amounts[simple_max_index].net_amount == 0:
                num_zero_net_amounts += 1
        else:
            transaction_amount = min(abs(list_of_net_amounts[min_index].net_amount), list_of_net_amounts[max_index].net_amount)
            ans_graph[min_index][max_index] = [transaction_amount, matching_type]
            list_of_net_amounts[min_index].net_amount += transaction_amount
            list_of_net_amounts[max_index].net_amount -= transaction_amount
            if list_of_net_amounts[min_index].net_amount == 0:
                num_zero_net_amounts += 1
            if list_of_net_amounts[max_index].net_amount == 0:
                num_zero_net_amounts += 1
    
    print_ans(ans_graph, num_banks, input)

if __name__ == "__main__":
    print("\n\t\t\t\t********************* Welcome to CASH FLOW MINIMIZER SYSTEM ***********************\n\n\n")
    print("This system minimizes the number of transactions among multiple banks in the different corners of the world that use different modes of payment. There is one world bank (with all payment modes) to act as an intermediary between banks that have no common mode of payment. \n\n")
    num_banks = int(input("Enter the number of banks participating in the transactions:\n"))
    
    input_data = []
    index_of = {}
    
    print("Enter the details of the banks and transactions as stated:\n")
    print("Bank name, the number of payment modes it has, and the payment modes.")
    print("Bank name and payment modes should not contain spaces.")
    
    max_num_types = 0
    for i in range(num_banks):
        if i == 0:
            print("World Bank: ", end="")
        else:
            print(f"Bank {i}: ", end="")
        name = input()
        index_of[name] = i
        num_types = (input("Number of payment modes: "))
        
        if i == 0:
            max_num_types = num_types
        
        types = set()
        print("Payment modes (separate with spaces): ")
        modes = input().split()
        for mode in modes:
            types.add(mode)
        
        input_data.append(Bank(name, 0, types))
    
    num_transactions = int(input("Enter the number of transactions:\n"))
    
    graph = [[0] * num_banks for _ in range(num_banks)]
    
    print("Enter the details of each transaction as stated:")
    print("Debtor Bank, Creditor Bank, and amount.")
    print("The transactions can be in any order.")
    for i in range(num_transactions):
        print(f"{i}th transaction: ", end="")
        s1, s2, amount = input().split()
        amount = int(amount)
        graph[index_of[s1]][index_of[s2]] = amount
    
    minimize_cash_flow(num_banks, input_data, index_of, num_transactions, graph, max_num_types)
