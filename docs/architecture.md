# II. Kiến trúc hệ thống (Architecture)

## 1. Giới thiệu

Tài liệu này mô tả kiến trúc tổng thể của dự án **AI Hardware Benchmark Suite**.

Mục tiêu của kiến trúc là tổ chức dự án theo hướng mô-đun (Modular Design), giúp việc phát triển, kiểm thử và bảo trì trở nên dễ dàng hơn. Mỗi thành phần trong hệ thống có một nhiệm vụ riêng biệt và có thể được mở rộng mà không ảnh hưởng đến các thành phần khác.

---

## 2. Cấu trúc dự án

```text
AI-Hardware-Benchmark/
│
├── benchmark/          # Mã nguồn các bài benchmark
│   ├── cpu.py
│   ├── gpu.py
│   ├── memory.py
│   ├── storage.py
│   └── ai.py
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   └── benchmark.py
├── scripts/            # Script thực thi
├── reports/            # Kết quả benchmark
├── logs/               # Nhật ký hoạt động
├── docs/               # Tài liệu dự án
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 3. Kiến trúc tổng thể

```text
                +----------------------+
                |      Người dùng      |
                +----------+-----------+
                           |
                           v
                  scripts/run_all.sh
                           |
                        main.py
                           |
                           v
             +---------------------------+
             |    Benchmark Framework    |
             +---------------------------+
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
    System Info      Hardware Benchmark    AI Benchmark
          |                |                |
          |         +-------+-------+       |
          |         |       |       |       |
          |         v       v       v       |
          |        GPU     CPU    Memory    |
          |                 |               |
          |                 v               |
          |              Storage            |
          +----------------+----------------+
                           |
                           v
                +-----------------------+
                |         core/         |
                |-----------------------|
                | config.py             |
                | logger.py             |
                | benchmark.py          |
                +-----------------------+
                           |
                           v
                 logs/            reports/
```

---

## 4. Luồng hoạt động

Hệ thống hoạt động theo trình tự sau:

1. Người dùng thực thi một script benchmark.
2. Thu thập thông tin hệ thống.
3. Thực hiện benchmark theo từng module.
4. Ghi nhật ký thực thi (Logging).
5. Xuất kết quả benchmark (Reporting).
6. Hoàn thành quá trình benchmark.

---

## 5. Các module chính

| Thư mục | Chức năng | Thành phần chính | Ghi chú |
|----------|-----------|------------------|----------|
| **benchmark/** | Chứa các module benchmark | CPU, GPU, Memory, Storage, AI | Mỗi module hoạt động độc lập |
| **core/** | Chứa các thành phần dùng chung | Config, Logger, Reporting, Benchmark Framework | Được tất cả module sử dụng |
| **scripts/** | Chứa các tập lệnh hỗ trợ | run_all.sh, benchmark_gpu.sh,... | Hỗ trợ tự động hóa |
| **reports/** | Lưu kết quả benchmark | TXT, CSV, JSON, Summary | Được sinh sau khi benchmark hoàn thành |
| **logs/** | Lưu nhật ký hoạt động | benchmark.log,... | Phục vụ Debug và theo dõi |
| **docs/** | Chứa tài liệu dự án | Roadmap, Architecture,... | Mô tả thiết kế và hướng dẫn sử dụng |

---

## 6. Quan hệ giữa các module

```text
scripts
    │
    ▼
benchmark
    │
    ├── GPU
    ├── CPU
    ├── Memory
    ├── Storage
    └── AI
    │
    ▼
Logging
    │
    ▼
Reporting
```

* `scripts/` chịu trách nhiệm điều khiển chương trình.
* `benchmark/` thực hiện các bài kiểm tra hiệu năng.
* `logs/` ghi lại quá trình thực thi.
* `reports/` lưu kết quả cuối cùng.

---

## 7. Nguyên tắc thiết kế

Dự án được xây dựng dựa trên các nguyên tắc sau:

* Thiết kế theo mô-đun (Modular Design).
* Mỗi module chỉ đảm nhiệm một chức năng.
* Dễ mở rộng và bảo trì.
* Tách biệt mã nguồn, tài liệu và kết quả benchmark.
* Hạn chế phụ thuộc giữa các module.
* Có thể bổ sung thêm benchmark mới mà không ảnh hưởng đến các module hiện có.

---

## 8. Khả năng mở rộng

Kiến trúc được thiết kế để dễ dàng bổ sung các module mới trong tương lai, ví dụ:

* Network Benchmark
* FPGA Benchmark
* NPU Benchmark
* Power Consumption Benchmark
* Thermal Benchmark
* Multi-GPU Benchmark

Việc mở rộng chỉ yêu cầu bổ sung module benchmark và cập nhật script thực thi mà không cần thay đổi kiến trúc tổng thể của hệ thống.
