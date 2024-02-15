# terraform_tfstate_mv
The code will move the Terraform state to a new one. This is useful when it is necessary to refactor the Terraform code.

Example:
```
modules_to_move = [
    ("module.rds.aws_db_subnet_group.private", "module.rds.aws_db_subnet_group.private")
    ("module.rds.aws_rds_cluster.postgres", "module.rds.aws_rds_cluster.postgres") ]
```
In the main Terraform state file, there is a module called 'rds'. It is better to move from module to module.

Execute:
```
for old_module, new_module in modules_to_move:
    move_modules_to_new_state(existing_state_file, new_state_file, old_module, new_module)
```
