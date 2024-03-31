def ip_transform(ip):
    ips = ip.split(".")  # [223,243,0,0] 32位二进制数
    ip_num = 0
    for i in ips:
        ip_num = int(i) | ip_num << 8
    return ip_num


if __name__ == '__main__':
    print(ip_transform('10.86.176.1'))
    print(ip_transform('10.86.174.1'))
    print(ip_transform('10.86.175.255'))
