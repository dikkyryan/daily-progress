Halo, kali ini saya akan membahas tentang Alibaba Cloud VPN Gateway. Apasih itu VPN Gateway ?? VPN Gateway adalah layanan yang menyediakan konektivitas jaringan aman antara berbagai sumber daya, seperti pusat data, cabang kantor, atau terminal internet, dengan Virtual Private Clouds (VPCs) melalui terowongan terenkripsi. Dengan VPN Gateway, kamu juga dapat membuat koneksi site-to-site menggunakan protokol IPsec-VPN atau koneksi point-to-site menggunakan protokol SSL-VPN.

Fitur ini memungkinkan untuk membangun jaringan yang aman dan terenkripsi di Alibaba Cloud, menghubungkan berbagai lokasi atau sumber daya secara fleksibel. Dengan adanya VPN Gateway, data yang dikirim antara sumber daya yang terhubung dan VPC dienkripsi, meningkatkan keamanan komunikasi jaringan kamu. Nah, Sekarang bagaimana cara untuk membuat dan mengkonfigurasi VPN Gateway di Alibaba Cloud ?? Simak tutorialnya berikut ini :


1. Yang pertama kamu masuk dulu kedalam console dan menuju ke Sub service **Hybrid Cloud Networking => VPN Gateway**

![](https://raw.githubusercontent.com/dikkyryan/daily-progress/main/posts/2023/12-december/19-december-2023/vpn0.png)

2. Selanjutnya pilih **Create VPC**

![](https://raw.githubusercontent.com/dikkyryan/daily-progress/main/posts/2023/12-december/19-december-2023/vpn1.png)

3. Didalam menu Create VPC, Kamu harus mengisi beberapa ketentuan yang bisa di sesuaikan dengan kebutuhan. Mulai dari Region, Nama, IPv4 CDR Block Subnet, dll.

![](https://raw.githubusercontent.com/dikkyryan/daily-progress/main/posts/2023/12-december/19-december-2023/vpn2.png)

![](https://raw.githubusercontent.com/dikkyryan/daily-progress/main/posts/2023/12-december/19-december-2023/vpn3.png)

4. Setelah semua sudah di isi sesuai kebutuhan maka di pojok kanan atas akan muncul **Architecture Preview**

![](https://raw.githubusercontent.com/dikkyryan/daily-progress/main/posts/2023/12-december/19-december-2023/vpn4.png)

5. Jika dirasa sudah sesuai, Kemudian pilih Create. Lalu akan muncul "**The VPC and vSwitches are created.**" maka tandanya VPC sudah berhasil dibuat.

![](https://raw.githubusercontent.com/dikkyryan/daily-progress/main/posts/2023/12-december/19-december-2023/vpn5.png)

6. Kemudian lanjut membuat **NAT Gateway**

![](https://raw.githubusercontent.com/dikkyryan/daily-progress/main/posts/2023/12-december/19-december-2023/vpn6.png)

7. Lalu kemudian mengisi data sesuai keperluan, seperti pembayaran, region, dll.

![](https://raw.githubusercontent.com/dikkyryan/daily-progress/main/posts/2023/12-december/19-december-2023/vpn7.png)

![](https://raw.githubusercontent.com/dikkyryan/daily-progress/main/posts/2023/12-december/19-december-2023/vpn8.png)

8. VPN Gateway berhasil dibuat di Alibaba Cloud.

Nah, Mudah bukan untuk membuat VPN Gateway di Alibaba Cloud. Semoga artikel ini dapat membantu kamu dalam membuat VPN Gateway di Alibaba Cloud ya.