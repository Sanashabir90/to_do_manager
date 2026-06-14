def main():
    # Colors for professional UI
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print(f"\n{BLUE}" + "="*50)
    print(f"    ✨ DECODELABS: TO-DO MANAGER (v2.1) ✨      ")
    print("="*50 + f"{RESET}")
    
    my_tasks = []
    
    while True:
        print(f"\n{YELLOW}[1] ➕ Add Task\n[2] 📋 View Tasks\n[3] ❌ Quit{RESET}")
        choice = input(f"\n{GREEN}Select an action (1-3): {RESET}")
        
        if choice == '1':
            task = input("Enter task name: ")
            desc = input("Enter task description: ")
            my_tasks.append(f"{task} | Desc: {desc}")
            print(f"{GREEN}✅ Task added successfully!{RESET}")
            
        elif choice == '2':
            print(f"\n{BLUE}--- YOUR CURRENT TASKS ---{RESET}")
            if not my_tasks:
                print("   ( List is empty )")
            else:
                for idx, item in enumerate(my_tasks, start=1):
                    print(f" {idx}. {item}")
            print(f"{BLUE}--------------------------{RESET}")
                
        elif choice == '3':
            print(f"{YELLOW}🚀 Exiting application. Keep coding!{RESET}")
            break
        else:
            print(f"\033[91m⚠️ Invalid choice. Please select 1, 2, or 3.{RESET}")

if __name__ == "__main__":
    main()
