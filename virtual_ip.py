import subprocess

# Set up the echo command and direct the output to a pipe
p1 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:1', '192.168.17.201'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:2', '192.168.17.202'], stdout=subprocess.PIPE)
p3 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:3', '192.168.17.203'], stdout=subprocess.PIPE)
p4 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:4', '192.168.17.204'], stdout=subprocess.PIPE)
p5 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:5', '192.168.17.205'], stdout=subprocess.PIPE)
p6 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:6', '192.168.17.206'], stdout=subprocess.PIPE)
p7 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:7', '192.168.17.207'], stdout=subprocess.PIPE)
p8 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:8', '192.168.17.208'], stdout=subprocess.PIPE)
p9 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:9', '192.168.17.209'], stdout=subprocess.PIPE)
p10 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:9', '192.168.17.210'], stdout=subprocess.PIPE)
p11 = subprocess.Popen(['sudo', 'ifconfig', 'enp3s0:9', '192.168.17.211'], stdout=subprocess.PIPE)

# Run the command
p1.communicate()[0]
p2.communicate()[0]
p3.communicate()[0]
p4.communicate()[0]
p5.communicate()[0]
p6.communicate()[0]
p7.communicate()[0]
p8.communicate()[0]
p9.communicate()[0]
p10.communicate()[0]
p11.communicate()[0]