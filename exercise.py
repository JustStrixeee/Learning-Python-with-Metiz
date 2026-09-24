incoming_ips = ["192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.2"]
trusted_ips = ["192.168.1.1", "172.16.0.2"]
banned_ips = []
for ip in incoming_ips:
    if ip not in trusted_ips:
        banned_ips.append(ip)

print(banned_ips)

gb_sizes = [1.5, 4.0, 0.5, 10.2]
mb_sizes = []

for i in gb_sizes:
    i= i * 1024
    mb_sizes.append(i)
print(mb_sizes)


torrents = {
    "avatar": "Раздается",
    "interstellar": "Скачивается",
    "matrix": "Готово"
}

user_request = input('Че надобно,старче!? >>>').strip().lower()
status_torrent = torrents.get(user_request, f"Торрент не найден")
print(status_torrent)