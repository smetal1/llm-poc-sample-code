import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('hostname', 22, 'username', 'password')

stdin, stdout, stderr = client.exec_command('ls -l')

output = stdout.read().decode()
print(output)

client.close()
