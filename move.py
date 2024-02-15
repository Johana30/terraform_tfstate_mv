import os
import subprocess

def move_modules_to_new_state(existing_state_file, new_state_file, old_module, new_module):
    # Get the current working directory
    current_directory = os.getcwd()
    
    # Change directory to where the existing state file is located
    os.chdir(os.path.dirname(existing_state_file))
 
    # Generate terraform state command to move module/resource to a new state file
    command = ["terraform", "state", "mv", "-state-out=" + os.path.join(current_directory, new_state_file), old_module, new_module]
    
    # Execute the terraform state command
    subprocess.run(command)
    
    # Change directory back to the original directory
    os.chdir(current_directory)



# Example usage:
existing_state_file = "path-of-existing/terraform.tfstate"
new_state_file = "path-of-new-state/terraform.tfstate"
modules_to_move = [
    ("module.rds.aws_db_subnet_group.private", "module.rds.aws_db_subnet_group.private")
    ("module.rds.aws_rds_cluster.postgres", "module.rds.aws_rds_cluster.postgres")
    ]
   

for old_module, new_module in modules_to_move:
    move_modules_to_new_state(existing_state_file, new_state_file, old_module, new_module)
