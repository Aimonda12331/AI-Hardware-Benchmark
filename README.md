# AI Hardware Benchmark Suite

AI Hardware Benchmark Suite là bộ công cụ benchmark mã nguồn mở được phát triển bằng Python nhằm đánh giá hiệu năng của toàn bộ hệ thống phần cứng phục vụ các tác vụ Trí tuệ nhân tạo (AI), Machine Learning (ML) và Deep Learning (DL).

Dự án cung cấp các bài benchmark cho CPU, GPU, bộ nhớ, thiết bị lưu trữ và các tác vụ AI thực tế, đồng thời tạo báo cáo giúp phân tích và so sánh hiệu năng giữa các hệ thống.

---

## Tính năng

* Benchmark CPU
* Benchmark GPU
* Benchmark Memory
* Benchmark Storage
* Benchmark AI
* Thu thập thông tin hệ thống
* Logging quá trình thực thi
* Sinh báo cáo kết quả
* Kiến trúc module dễ mở rộng

---

## Cấu trúc dự án

```text
AI-Hardware-Benchmark/
│
├── benchmark/
├── core/               # Thành phần dùng chung
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   └── benchmark.py
├── scripts/
├── reports/
├── logs/
├── docs/
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Yêu cầu

* Python 3.10 trở lên
* Linux (khuyến nghị Ubuntu)
* NVIDIA Driver (đối với GPU NVIDIA)
* CUDA Toolkit (nếu sử dụng GPU Benchmark)
* Các thư viện trong `requirements.txt`

---

## Cài đặt

```bash
git clone https://github.com/<your-account>/AI-Hardware-Benchmark.git

cd AI-Hardware-Benchmark

pip install -r requirements.txt
```

---

## Cách sử dụng

Ví dụ chạy toàn bộ benchmark:

```bash
python main.py
```

Hoặc chạy từng module riêng:

```bash
python benchmark/cpu.py
python benchmark/memory.py
python benchmark/storage.py
python benchmark/gpu.py
python benchmark/ai.py
```

> Các lệnh trên là ví dụ và sẽ được cập nhật khi dự án hoàn thiện.

---

## Tài liệu

Tài liệu thiết kế được lưu trong thư mục `docs/`.

| Tài liệu             | Mô tả                       |
| -------------------- | --------------------------- |
| roadmap.md           | Lộ trình phát triển dự án   |
| architecture.md      | Kiến trúc tổng thể          |
| logging.md           | Thiết kế hệ thống Logging   |
| reporting.md         | Thiết kế hệ thống Reporting |
| cpu_benchmark.md     | Thiết kế CPU Benchmark      |
| memory_benchmark.md  | Thiết kế Memory Benchmark   |
| storage_benchmark.md | Thiết kế Storage Benchmark  |
| gpu_benchmark.md     | Thiết kế GPU Benchmark      |
| ai_benchmark.md      | Thiết kế AI Benchmark       |

---

## Lộ trình

Các giai đoạn phát triển được mô tả chi tiết trong:

```text
docs/roadmap.md
```

---

## Đóng góp

Mọi đóng góp nhằm cải thiện dự án đều được hoan nghênh.

Nếu phát hiện lỗi hoặc có đề xuất mới, vui lòng tạo Issue hoặc Pull Request.

---

## Giấy phép

Dự án được phát hành theo giấy phép MIT License.
