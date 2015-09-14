import paramiko

''' password
ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.72.128', 22, 'root', 'Ncchina123')
stdin, stdout, stderr = ssh.exec_command('ls sb')
print stdout.read()
ssh.close()
'''

'''   public_key
import paramiko
private_file_path = '/root/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_file_path)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.121', username='root', port=22, pkey=key)
stdin, stdout, stderr = ssh.exec_command('ifconfig')
print stdout.read()
ssh.close()
'''

private_file_path = '/root/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_file_path)
t = paramiko.Transport(('192.168.1.121',22))
t.connect(username='root',pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/gubaoer.txt', '/tmp/gubaoer.txt')
t.close()