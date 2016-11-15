from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import vmutils
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--username',
                    help='Username of the vcenter user that you want to login with. ')
parser.add_argument('--password',
                    help='Password of the vcenter user that you want to login with. ')
parser.add_argument('--vcenter',
                    help='Domain of the vsphere client. i.e.: somevcenter.yourhost.com ')
parser.add_argument('--vcenterport',
                    help='Port number of the vsphere client. Example: 443 ')
parser.add_argument('--vmname',
                    help='Name of virtual machine as it appears in vsphere. i.e.: example-mysqldb-server ')

ARGS = parser.parse_args()

try:
    si = SmartConnect(user=ARGS.username,
                      pwd=ARGS.password,
	                  host=ARGS.vcenter,
        	          port=ARGS.vcenterport)
except IOError, e:
    pass

# Finding source VM
vm = vmutils.get_vm_by_name(si, ARGS.vmname)

# does the actual vm reboot
try:
    vm.ResetGuest()
except:
    # forceably shutoff/on
    # need to do if vmware guest additions isn't running
    vm.ResetVM_Task()

Disconnect(si)