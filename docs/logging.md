# III. Hệ thống Logging

## 1. Giới thiệu

Hệ thống Logging được sử dụng để ghi lại toàn bộ quá trình thực thi của chương trình trong suốt quá trình benchmark.

Các bản ghi (Log) giúp theo dõi tiến trình thực thi, hỗ trợ phát hiện lỗi, phân tích nguyên nhân sự cố và lưu lại lịch sử hoạt động của hệ thống.

---

## 2. Mục đích

Hệ thống Logging được xây dựng nhằm các mục tiêu sau:

* Ghi lại quá trình thực thi của chương trình.
* Theo dõi trạng thái của từng module benchmark.
* Hỗ trợ phát hiện và phân tích lỗi.
* Lưu lịch sử chạy benchmark.
* Hỗ trợ quá trình kiểm thử và bảo trì.
* Cung cấp thông tin phục vụ việc phân tích kết quả benchmark.

---

## 3. Cấu trúc thư mục

Toàn bộ file log được lưu trong thư mục:

```text
logs/
```

Trong tương lai, hệ thống có thể mở rộng thành:

```text
logs/
├── benchmark.log
├── system.log
├── gpu.log
├── cpu.log
├── memory.log
├── storage.log
└── ai.log
```

Mỗi module benchmark sẽ có thể ghi log riêng nhằm thuận tiện cho việc theo dõi và phân tích.

---

## 4. Vị trí trong kiến trúc hệ thống

Hệ thống Logging được triển khai trong thư mục `core/` và được sử dụng chung bởi toàn bộ các module benchmark.

```text
core/
├── logger.py
└── config.py

## 5. Mức độ Logging

Hệ thống sử dụng các mức log phổ biến.

| Level   | Ý nghĩa                                            |
| ------- | ---------------------------------------------------|
| INFO    | Thông tin quá trình thực thi                       |
| WARNING | Cảnh báo nhưng chương trình vẫn tiếp tục           |
| ERROR   | Xuất hiện lỗi làm ảnh hưởng đến chương trình       |
| DEBUG   | Thông tin chi tiết phục vụ phát triển và gỡ lỗi    |
| CRITICAL| Lỗi nghiêm trọng, chương trình khó có thể tiếp tục |

---

## 6. Nội dung bản ghi

Mỗi bản ghi nên bao gồm các thông tin sau:

* Thời gian thực thi (Timestamp)
* Mức độ Log (Level)
* Tên module
* Nội dung thông báo

Ví dụ:

```text
2026-07-20 10:30:12 | INFO    | GPU     | GPU Benchmark Started
2026-07-20 10:30:15 | INFO    | GPU     | CUDA Device Detected
2026-07-20 10:31:10 | WARNING | GPU     | GPU Temperature High
2026-07-20 10:31:40 | INFO    | GPU     | Benchmark Completed
```

---

## 7. Thời điểm ghi Log

Log sẽ được ghi tại các thời điểm quan trọng trong quá trình thực thi.

Ví dụ:

* Bắt đầu chương trình.
* Bắt đầu benchmark.
* Kết thúc benchmark.
* Phát hiện phần cứng.
* Phát hiện lỗi.
* Hoàn thành chương trình.

Việc ghi log giúp xác định chính xác chương trình đang thực hiện bước nào.

---

## 8. Nguyên tắc thiết kế

Hệ thống Logging được thiết kế theo các nguyên tắc sau:

* Mỗi module có thể ghi log độc lập.
* Toàn bộ hệ thống sử dụng chung một Logger được triển khai trong `core/logger.py`.
* Định dạng log thống nhất trong toàn bộ dự án.
* Không làm ảnh hưởng đáng kể đến hiệu năng benchmark.
* Dễ dàng mở rộng khi bổ sung module mới.
* Dễ dàng tích hợp với hệ thống báo cáo trong tương lai.

---

## 9. Mối quan hệ với Reporting

Logging và Reporting có mục đích khác nhau.

| Logging                                  | Reporting                         |
| ---------------------------------------- | --------------------------------- |
| Ghi lại quá trình thực thi               | Lưu kết quả benchmark             |
| Phục vụ Debug                            | Phục vụ đánh giá hiệu năng        |
| Ghi liên tục trong khi chương trình chạy | Sinh sau khi benchmark hoàn thành |
| Chủ yếu dành cho lập trình viên          | Chủ yếu dành cho người sử dụng    |

---

## 10. Khả năng mở rộng

Trong tương lai, hệ thống Logging có thể được mở rộng với các tính năng như:

* Ghi log theo từng phiên chạy (Session).
* Tự động xoay vòng file log (Log Rotation).
* Lưu log theo ngày.
* Ghi log dưới định dạng JSON.
* Xuất log phục vụ phân tích hoặc giám sát.
* Hỗ trợ nhiều Logger Handler (Console, File, Remote Logging).

---

## 11. Kết luận

Hệ thống Logging là một thành phần quan trọng của AI Hardware Benchmark Suite.

Việc thiết kế một hệ thống Logging thống nhất giúp quá trình phát triển, kiểm thử và bảo trì trở nên dễ dàng hơn, đồng thời cung cấp đầy đủ thông tin để theo dõi và phân tích hoạt động của toàn bộ hệ thống benchmark.
