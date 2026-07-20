# IV. Hệ thống Reporting

## 1. Giới thiệu

Hệ thống Reporting chịu trách nhiệm tổng hợp và lưu trữ kết quả của các bài benchmark sau khi chương trình thực thi hoàn tất.

Các báo cáo giúp người dùng đánh giá hiệu năng phần cứng, so sánh kết quả giữa các lần benchmark và lưu trữ thông tin phục vụ phân tích trong tương lai.

---

## 2. Mục đích

Hệ thống Reporting được xây dựng nhằm các mục tiêu sau:

* Lưu kết quả benchmark.
* Tổng hợp kết quả từ nhiều module.
* Chuẩn hóa định dạng báo cáo.
* Hỗ trợ phân tích và so sánh kết quả.
* Làm cơ sở cho việc đánh giá hiệu năng phần cứng.

---

## 3. Cấu trúc thư mục

Toàn bộ báo cáo được lưu trong thư mục:

```text
reports/
```

Trong tương lai, hệ thống có thể được tổ chức như sau:

```text
reports/
├── system/
│   └── system_info.txt
│
├── gpu/
│   └── gpu_result.txt
│
├── cpu/
│   └── cpu_result.txt
│
├── memory/
│   └── memory_result.txt
│
├── storage/
│   └── storage_result.txt
│
├── ai/
│   └── ai_result.txt
│
└── summary/
    ├── summary.txt
    ├── summary.csv
    └── summary.json
```

Mỗi module sẽ lưu kết quả vào thư mục tương ứng nhằm giúp việc quản lý và tra cứu trở nên thuận tiện.

---

## 4. Vị trí trong kiến trúc hệ thống

Hệ thống Reporting được triển khai trong thư mục `core/` và được sử dụng chung bởi tất cả các module Benchmark.

```text
core/
├── reporting.py
└── config.py

## 5. Nội dung báo cáo

Mỗi báo cáo nên bao gồm các thông tin cơ bản sau:

* Thời gian thực hiện benchmark.
* Thông tin phần cứng.
* Thông tin phần mềm.
* Cấu hình benchmark.
* Kết quả đo được.
* Thời gian thực thi.

Ví dụ:

```text
Benchmark Time : 2026-07-20 10:30:00

GPU            : NVIDIA RTX 3060
CUDA Version   : 13.0

FP32           : 12.5 TFLOPS
FP16           : 24.8 TFLOPS

Execution Time : 35.6 s
```

---

## 6. Định dạng báo cáo

## 5. Định dạng báo cáo

Hệ thống hỗ trợ nhiều định dạng báo cáo nhằm đáp ứng các mục đích sử dụng khác nhau.

| Định dạng | Mô tả | Phù hợp với |
|-----------|-------|-------------|
| **TXT** | Định dạng văn bản đơn giản, dễ đọc và dễ lưu trữ. | - Kiểm tra nhanh<br>- Chia sẻ kết quả<br>- Lưu trữ lâu dài |
| **CSV** | Định dạng dữ liệu dạng bảng, tương thích với nhiều công cụ xử lý dữ liệu. | - Microsoft Excel<br>- LibreOffice Calc<br>- Phân tích dữ liệu |
| **JSON** | Định dạng dữ liệu có cấu trúc, thuận tiện cho việc trao đổi và xử lý tự động. | - Tích hợp hệ thống<br>- Phân tích bằng Python<br>- Xây dựng Dashboard |
---

## 7. Báo cáo tổng hợp

Ngoài báo cáo của từng module, hệ thống sẽ tạo báo cáo tổng hợp.

Ví dụ:

* Cấu hình hệ thống.
* Kết quả GPU.
* Kết quả CPU.
* Kết quả Memory.
* Kết quả Storage.
* Kết quả AI.

Báo cáo tổng hợp giúp người dùng có cái nhìn toàn diện về hiệu năng của hệ thống.

---

## 8. Nguyên tắc thiết kế

Hệ thống Reporting được thiết kế theo các nguyên tắc sau:

* Chuẩn hóa định dạng báo cáo.
* Mỗi module tạo báo cáo riêng.
* Toàn bộ hệ thống sử dụng chung một Reporting Engine.
* Báo cáo dễ đọc và dễ phân tích.
* Hỗ trợ nhiều định dạng xuất dữ liệu.
* Dễ dàng mở rộng khi bổ sung module benchmark mới.

---

## 9. Mối quan hệ với Logging

Logging và Reporting có vai trò khác nhau trong hệ thống.

| Logging                                 | Reporting                             |
| --------------------------------------- | ------------------------------------- |
| Ghi lại quá trình thực thi              | Lưu kết quả benchmark                 |
| Phục vụ Debug                           | Phục vụ đánh giá hiệu năng            |
| Được ghi liên tục khi chương trình chạy | Được tạo sau khi benchmark hoàn thành |
| Chủ yếu dành cho lập trình viên         | Chủ yếu dành cho người sử dụng        |

---

## 10. Khả năng mở rộng

Trong tương lai, hệ thống Reporting có thể được mở rộng với các tính năng:

* Xuất báo cáo HTML.
* Xuất báo cáo PDF.
* Sinh biểu đồ hiệu năng.
* So sánh nhiều lần benchmark.
* Lưu lịch sử benchmark.
* Tự động tạo Dashboard.
* Hỗ trợ Dashboard thời gian thực.
* Hỗ trợ xuất dữ liệu sang cơ sở dữ liệu (SQLite, PostgreSQL...).
* Hỗ trợ API để tích hợp với hệ thống bên ngoài.

---

## 11. Kết luận

Hệ thống Reporting là thành phần tổng hợp kết quả của toàn bộ AI Hardware Benchmark Suite.

Việc chuẩn hóa cấu trúc và định dạng báo cáo giúp người dùng dễ dàng theo dõi, phân tích và so sánh hiệu năng của các hệ thống phần cứng trong nhiều môi trường khác nhau.
