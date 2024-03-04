def move_state(module_mappings):
    current_directory = os.getcwd()
    #os.chdir(os.path.dirname(existing_state_file))
    
    for old_module, new_module in module_mappings:
        command = ["terraform", "state", "mv", old_module.strip(), new_module.strip()]
        subprocess.run(command)
    
    os.chdir(current_directory)

def list_state():
    current_directory = os.getcwd()
    command = ["terraform", "state", "list"]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    #subprocess.run(command)

def rm_state(resourse_name):
    command = ["terraform", "state", "rm", resourse_name]
    subprocess.run(command)

def main():
    print("**** Welcome to Terraform State helper **** \n it is dificult to change the tfstate file, this can help you\n")
    print("example of the file: aws_s3_bucket.site, aws_s3_bucket.site \n It is better to called the same\n")
    print("** What do you want to use **\n \n1. terraform state list \n2. terraform state mv -state-out \n3. terraform state mv \n4. terraform rm")
    
    op = input("Enter your option: \n")

    if op == "1":
        list_state()
       
    elif op == "2":
        existing_state_file = input("Enter path to existing state file: ")
        new_state_file = input("Enter path for new state file: ")
        modules_file = input("Enter path to the file containing old and new modules/resources: ")

        module_mappings = []
        with open(modules_file, 'r') as f:
            for line in f:
                old_module, new_module = map(str.strip, line.split(','))
                module_mappings.append((old_module, new_module))

        move_modules_to_new_state(existing_state_file, new_state_file, module_mappings)
    elif op == "3":
    
        modules_file = input("Enter path to the file containing old and new modules/resources: ")
        module_mappings = []
        with open(modules_file, 'r') as f:
            for line in f:
                old_module, new_module = map(str.strip, line.split(','))
                module_mappings.append((old_module, new_module))

        move_state(module_mappings)
    else:
        reso = input("type the resource-id: ")
        rm_state(reso)
        
if __name__ == "__main__":
    main()
