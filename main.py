from agent1 import main as agent1_main

if __name__ == "__main__":
    command = "Give me the account summary for the current month"
    response = agent1_main(command)
    print(response)