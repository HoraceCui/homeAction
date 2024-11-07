import dns.resolver
import ipaddress
import sys

# sudo apt install python3-pip
# pip install dnspython
def get_aaaa_record(domain):
    """
    获取指定域名的 AAAA 记录
    参数:
        domain (str): 要查询的域名
    返回:
        list: 返回包含 AAAA 记录的列表，如果没有记录或查询失败，返回 None
    """
    try:
        # 查询AAAA记录
        answers = dns.resolver.resolve(domain, 'AAAA')
        #return [answer.to_text() for answer in answers]
        #return answers[0].to_text()
        #return ipaddress.IPv6Address(answers[0].to_text())#.compressed
        return ipaddress.ip_address(answers[0].to_text()).exploded
    except dns.resolver.NoAnswer:
        return None  # 没有 AAAA 记录
    except dns.resolver.NXDOMAIN:
        return None  # 域名不存在
    except Exception as e:
        print(f"查询时出错: {e}")
        return None

def main():
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("用法: python dns_query.py <域名>")
        sys.exit(1)

    domain = sys.argv[1]
    aaaa_records = get_aaaa_record(domain)
    #return get_aaaa_record(domain)

    if aaaa_records:
        print("AAAA 记录:", aaaa_records)
    else:
        print("未找到 AAAA 记录或查询失败")

if __name__ == "__main__":
    main()
