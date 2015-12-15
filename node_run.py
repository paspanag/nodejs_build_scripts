import subprocess
import sys

def run(kernel_file, app_file, entry_file="index.js", ex_port=3000, in_port=3000, qemu_bin="qemu-system-x86_64", mac=None, kvm=False, memory=256):
    mac = mac if mac else "52:54:00:ec:fb:7b"

    sub_call = [
        qemu_bin,
        "-net",
        "nic,model=virtio,macaddr={0}".format(mac),
        "-net",
        "user,hostfwd=tcp::{0}-:{1}".format(ex_port, in_port),
        "-drive",
        "if=virtio,file={0}".format(app_file),
        "-m",
        "{0}".format(memory),
        "-kernel",
        "{0}".format(kernel_file),
        "-append",
        "'{,, \"net\" : {,, \"if\": \"vioif0\",, \"type\": \"inet\",, \"method\": \"dhcp\",, },, \"blk\" : {,, \"source\": \"dev\",, \"path\": \"/dev/ld0a\",, \"fstype\": \"blk\",, \"mountpoint\": \"/app\",, },, \"cmdline\": \""+kernel_file+" /app/"+entry_file+"\",, },'"
    ]
    subprocess.call(sub_call)



if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
