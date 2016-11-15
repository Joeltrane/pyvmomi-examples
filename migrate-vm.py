from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import vmutils
import random
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--username',
                    help='Username of the vcenter user that you want to login with. ')
parser.add_argument('--password',
                    help='Password of the vcenter user that you want to login with. ')
parser.add_argument('--vcenter',
                    help='Domain of the vsphere client. Example: somevcenter.yourhost.com ')
parser.add_argument('--vcenterport',
                    help='Port number of the vsphere client. Example: 443 ')
parser.add_argument('--vmname',
                    help='Name of virtual machine as it appears in vsphere. i.e.: example-mysqldb-server ')
parser.add_argument('--esx_host',
                    help='Fully qualfied domain name of ESXi Host a VM should be migrated to ')

try:
    si = SmartConnect(user=ARGS.username,
                      pwd=ARGS.password,
	                  host=ARGS.vcenter,
        	          port=ARGS.vcenterport,
                      port = ARGS.esx_host)
    except IOError, e:
    pass

if esx_host == '':
    all_hosts = vmutils.get_hosts(si)
    esx_host = vmutils.get_host_by_name(si, random.choice(all_hosts.values()))
else:
    esx_host = vmutils.get_host_by_name(si, ARGS.esx_host)

# Finding source VM
vm = vmutils.get_vm_by_name(si, vm_name)

# relocate spec, to migrate to another host
# this can do other things, like storage and resource pool
# migrations
relocate_spec = vim.vm.RelocateSpec(host=ARGS.esx_host)

# does the actual migration to host
vm.Relocate(relocate_spec)

Disconnect(si)
