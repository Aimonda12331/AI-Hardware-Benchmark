# I. Roadmap

## Tổng quan

Roadmap này mô tả kế hoạch phát triển của dự án **AI Hardware Benchmark Suite**.

Dự án được chia thành nhiều giai đoạn (Phase), mỗi giai đoạn tập trung vào một nhóm chức năng cụ thể. Việc phát triển theo từng bước giúp dễ quản lý, kiểm thử và mở rộng hệ thống trong tương lai.

---

## Các giai đoạn phát triển

## Ghi chú
* [x] Hoàn thành
* [/] Đang thực hiện
* [ ] Chưa thực thiện

### Phase 1 - Nền tảng dự án (Project Foundation)

Thiết lập cấu trúc dự án và môi trường phát triển.

* [x] Cấu trúc dự án
* [x] README.md
* [x] requirements.txt
* [x] .gitignore
* [x] Tệp cấu hình chung (config.py)
* [x] Điểm khởi chạy chương trình (main.py)
* [/] Hệ thống Logging
* [ ] Hệ thống Reporting
* [ ] Hệ thống quản lý benchmark (Benchmark Framework)
* [ ] Kiểm tra môi trường phát triển

---

### Phase 2 - Thu thập thông tin hệ thống (System Information)

Xây dựng các module thu thập thông tin phần cứng và môi trường phần mềm.

* [ ] Thông tin hệ thống
* [ ] Thông tin CPU
* [ ] Thông tin GPU
* [ ] Thông tin RAM
* [ ] Thông tin thiết bị lưu trữ
* [ ] Thông tin CUDA
* [ ] Thông tin môi trường PyTorch

---

### Phase 3 - Benchmark GPU

Xây dựng các bài kiểm tra và đánh giá hiệu năng GPU.

* [ ] Phát hiện GPU
* [ ] Kiểm tra tải GPU (GPU Stress Test)
* [ ] Kiểm tra bộ nhớ VRAM
* [ ] Benchmark FP32
* [ ] Benchmark FP16
* [ ] Benchmark Tensor Core
* [ ] Benchmark CUDA

---

### Phase 4 - Benchmark CPU

Xây dựng các bài kiểm tra hiệu năng CPU.

* [ ] CPU Stress Test
* [ ] Benchmark đơn luồng
* [ ] Benchmark đa luồng
* [ ] Benchmark nhân ma trận

---

### Phase 5 - Benchmark bộ nhớ (Memory Benchmark)

Xây dựng các bài kiểm tra hiệu năng RAM.

* [ ] Đo tốc độ đọc RAM
* [ ] Đo tốc độ ghi RAM
* [ ] Đo tốc độ sao chép RAM
* [ ] Đo băng thông bộ nhớ

---

### Phase 6 - Benchmark thiết bị lưu trữ (Storage Benchmark)

Xây dựng các bài kiểm tra hiệu năng SSD/HDD.

* [ ] Đọc tuần tự (Sequential Read)
* [ ] Ghi tuần tự (Sequential Write)
* [ ] Đọc ngẫu nhiên (Random Read)
* [ ] Ghi ngẫu nhiên (Random Write)
* [ ] Benchmark IOPS

---

### Phase 7 - Benchmark AI

Xây dựng các bài benchmark dành cho AI và Deep Learning.

* [ ] Benchmark huấn luyện mô hình
* [ ] Benchmark suy luận (Inference)
* [ ] Benchmark CNN
* [ ] Benchmark theo Batch Size
* [ ] Benchmark Mixed Precision (AMP)

---

### Phase 8 - Hệ thống báo cáo (Reporting)

Xây dựng hệ thống xuất kết quả benchmark.

* [ ] Báo cáo TXT
* [ ] Báo cáo JSON
* [ ] Báo cáo CSV
* [ ] Tổng hợp kết quả Benchmark
* [ ] Tổng hợp cấu hình phần cứng

---

### Phase 9 - Tính năng nâng cao (Advanced Features)

Phát triển các tính năng mở rộng của hệ thống.

* [ ] Benchmark nhiều GPU
* [ ] Giám sát nhiệt độ
* [ ] Giám sát công suất tiêu thụ
* [ ] Lưu lịch sử Benchmark
* [ ] Tham số dòng lệnh (Command Line Arguments)
* [ ] Tệp cấu hình (Configuration File)

---

## Tiến độ dự án

| Phase | Module             |     Trạng thái     |
| :---: | ------------------ | :----------------: |
|   1   | Project Foundation | 🟡 Đang phát triển |
|   2   | System Information |   ⏳ Chưa bắt đầu   |
|   3   | GPU Benchmark      |   ⏳ Chưa bắt đầu   |
|   4   | CPU Benchmark      |   ⏳ Chưa bắt đầu   |
|   5   | Memory Benchmark   |   ⏳ Chưa bắt đầu   |
|   6   | Storage Benchmark  |   ⏳ Chưa bắt đầu   |
|   7   | AI Benchmark       |   ⏳ Chưa bắt đầu   |
|   8   | Reporting          |   ⏳ Chưa bắt đầu   |
|   9   | Advanced Features  |   ⏳ Chưa bắt đầu   |

---

## Ghi chú

* Roadmap này là kế hoạch phát triển tổng thể của dự án.
* Các chức năng có thể được bổ sung, điều chỉnh hoặc thay đổi tùy theo quá trình phát triển.
* Mỗi giai đoạn nên được hoàn thành và kiểm thử trước khi chuyển sang giai đoạn tiếp theo.
* Chi tiết thiết kế và cách triển khai của từng module sẽ được trình bày trong các tài liệu tương ứng trong thư mục `docs/`.
