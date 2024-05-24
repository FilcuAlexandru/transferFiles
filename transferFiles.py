###########################################################
# A python script to transfer files between multiple vm's #
# Use the script as the 'root' user                       #
# Author: Alexandru Filcu                                 #
###########################################################

##############################
# Import the necessary tools #
##############################

import subprocess

#############################################
# The "copy_file_to_multiple_vms" function  #
#############################################

def copy_file_to_multiple_vms(master_vm_ip, file_path, destination_vm_ips, destination_path):
    '''Copies a file from the master VM to multiple destination VMs using SCP'''
    for destination_vm_ip in destination_vm_ips:
        scp_command = [
            'scp',
            '-o', 'StrictHostKeyChecking=no',
            file_path,
            'root@{}:{}'.format(destination_vm_ip, destination_path)
        ]
        subprocess.call(scp_command)

#########
# Usage #
#########

master_vm_ip = '***.***.***.***'  # Replace with the IP address of the VM you want to copy the file from
file_path = '/path/to/your/file'  # Replace with the path of the file you want to copy
destination_vm_ips = [  # Replace with the IP addresses of the VMs where you want the file to be copied
    '***.***.***.***',
    '***.***.***.***',
    '***.***.***.***',
    '***.***.***.***'
]
destination_path = '/path/to/destination/file'  # Replace with the path where you want the file to be copied on the other VMs

################################################################################
# Call the function to copy the file from the master VM to the destination VMs #
################################################################################

copy_file_to_multiple_vms(master_vm_ip, file_path, destination_vm_ips, destination_path)
