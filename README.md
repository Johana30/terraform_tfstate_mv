# terraform_tfstate_mv
The code will move the tfstate to a new one.

This is usefull whe it is necesary to refactor the terraform code.

Example:

modules_to_move = [
    ("module.rds.aws_db_subnet_group.private", "module.rds.aws_db_subnet_group.private")
    ("module.rds.aws_rds_cluster.postgres", "module.rds.aws_rds_cluster.postgres") ]

there is a module called rds in the main tfstate file, it is better move from module to module

Execute:
for old_module, new_module in modules_to_move:
    move_modules_to_new_state(existing_state_file, new_state_file, old_module, new_module)
