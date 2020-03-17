# Code-python-ping-latency-wan.
Script check latency vs paket loss từng đường WAN FTTH

# Logic code check latency network từng wan.
- mỗi script check network latency chạy từng interface.
- mỗi interface tương ứng một virtual ip , route vip cố định trên một wan.
- mỗi script ping đến đống thời 3 domain, get kết quả latency, packet loss ở từng wan.
- cảnh báo đồng thời 3 host vượt ngưỡng latency cao vs packet loss.
- mỗi script sleep 10s vs running lần tiếp theo
- quản lý các process của th

