# Alibaba ECS Configuration

Cloud servers uses LINUX server system for best performance. It does not have a GUI for easy usage and requires command line to browse and modify files.
One of the most common procedure is to connect to the cloud instance using SSH connection, it requires key pairing for security purpose, since every IPs by default are allowed to connect to the instance.
Although we can use the web console, it is slow and non-responsive compare to client app.

1. Create an ECS instance
![]('https://i.ibb.co/NSmWw44/Screenshot-2020-12-13-at-8-00-59-AM.png')
<img src="https://i.ibb.co/NSmWw44/Screenshot-2020-12-13-at-8-00-59-AM.png" alt="p1">
2. Create key paring to the instance
![]('https://i.ibb.co/s1QVKHf/Screenshot-2020-12-13-at-8-01-21-AM.png')
<img src="https://i.ibb.co/s1QVKHf/Screenshot-2020-12-13-at-8-01-21-AM.png" alt="p1">
3. Check for connection TCP22 allowed
![]('https://i.ibb.co/D1K2GLn/Screenshot-2020-12-13-at-8-02-16-AM.png')
<img src="https://i.ibb.co/D1K2GLn/Screenshot-2020-12-13-at-8-02-16-AM.png" alt="p1">
4. chmod 400 Key.pem

5. Connect using ssh -i Key.pem root@42.abc.xyz
![]('https://i.ibb.co/3NgR0Kx/Screenshot-2020-12-13-at-8-08-29-AM.png')
<img src="https://i.ibb.co/3NgR0Kx/Screenshot-2020-12-13-at-8-08-29-AM.png" alt="p1">

