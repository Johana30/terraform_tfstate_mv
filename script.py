import os
import subprocess

def move_modules_to_new_state(existing_state_file, new_state_file, module_mappings):
    current_directory = os.getcwd()
    os.chdir(os.path.dirname(existing_state_file))
    
    for old_module, new_module in module_mappings:
        print("print oldmodule")
        print("terraform", "state", "mv", "-state-out=" + os.path.join(current_directory, new_state_file), old_module.strip(), new_module.strip())
        command = ["terraform", "state", "mv", "-state-out=" + os.path.join(current_directory, new_state_file), old_module.strip(), new_module.strip()]
        subprocess.run(command)
    
    os.chdir(current_directory)

def move_state(module_mappings):
    current_directory = os.getcwd()
    #os.chdir(os.path.dirname(existing_state_file))
    
    for old_module, new_module in module_mappings:
        command = ["terraform", "state", "mv", old_module.strip(), new_module.strip()]
        subprocess.run(command)
    
    os.chdir(current_directory)

def main():
    print("**** Welcome to Terraform State helper **** \n it is dificult to change the tfstate file, this can help you\n")
    print("example of the file: aws_s3_bucket.site, aws_s3_bucket.site \n It is better to called the same\n")
    print("** What do you want to use **\n \n1. terraform state mv -state-out \n2. terraform state mv \n")
    
    op = input("Enter your option: \n")

    if op == 1 :
        existing_state_file = input("Enter path to existing state file: ")
        new_state_file = input("Enter path for new state file: ")
        modules_file = input("Enter path to the file containing old and new modules/resources: ")

        module_mappings = []
        with open(modules_file, 'r') as f:
            for line in f:
                old_module, new_module = map(str.strip, line.split(','))
                module_mappings.append((old_module, new_module))

        move_modules_to_new_state(existing_state_file, new_state_file, module_mappings)
    else :
        modules_file = input("Enter path to the file containing old and new modules/resources: ")
        module_mappings = []
        with open(modules_file, 'r') as f:
            for line in f:
                old_module, new_module = map(str.strip, line.split(','))
                module_mappings.append((old_module, new_module))

        move_state(module_mappings)
        
if __name__ == "__main__":
    main()
