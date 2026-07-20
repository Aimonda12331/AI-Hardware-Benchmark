# VII. Storage Benchmark

## 1. Giới thiệu

Storage Benchmark là module dùng để đánh giá hiệu năng của thiết bị lưu trữ như SSD, NVMe SSD và HDD.

Module này thực hiện các bài kiểm tra nhằm đo tốc độ đọc, ghi, khả năng xử lý truy cập ngẫu nhiên và số lượng thao tác vào/ra mỗi giây (IOPS). Kết quả benchmark giúp đánh giá hiệu năng của hệ thống lưu trữ trong các tác vụ như khởi động hệ điều hành, sao chép dữ liệu, huấn luyện mô hình AI và xử lý dữ liệu lớn.

---

## 2. Mục tiêu

Module Storage Benchmark được xây dựng nhằm:

* Đánh giá hiệu năng tổng thể của thiết bị lưu trữ.
* Đo tốc độ đọc tuần tự.
* Đo tốc độ ghi tuần tự.
* Đo tốc độ đọc ngẫu nhiên.
* Đo tốc độ ghi ngẫu nhiên.
* Đo chỉ số IOPS.
* Hỗ trợ phân tích và so sánh giữa các thiết bị lưu trữ.

---

## 3. Các bài Benchmark

Module bao gồm các bài kiểm tra sau:

* Storage Detection
* Sequential Read Benchmark
* Sequential Write Benchmark
* Random Read Benchmark
* Random Write Benchmark
* IOPS Benchmark

---

## 4. Storage Detection

### Mục đích

Thu thập thông tin của thiết bị lưu trữ trước khi thực hiện benchmark.

### Thông tin cần thu thập

* Tên thiết bị.
* Loại thiết bị (HDD, SATA SSD, NVMe SSD).
* Dung lượng.
* Chuẩn giao tiếp.
* Điểm gắn kết (Mount Point).
* Hệ thống tập tin (File System).
* Dung lượng đã sử dụng và còn trống.

---

## 5. Sequential Read Benchmark

### Mục đích

Đo tốc độ đọc tuần tự từ thiết bị lưu trữ.

### Ý nghĩa

Bài kiểm tra phản ánh hiệu năng khi đọc các tệp có kích thước lớn.

Ví dụ:

* Đọc video.
* Đọc mô hình AI.
* Sao lưu dữ liệu.

### Thông tin ghi nhận

* Kích thước dữ liệu kiểm tra.
* Thời gian thực hiện.
* Tốc độ đọc (MB/s hoặc GB/s).

---

## 6. Sequential Write Benchmark

### Mục đích

Đo tốc độ ghi tuần tự vào thiết bị lưu trữ.

### Ý nghĩa

Bài kiểm tra phản ánh hiệu năng khi ghi các tệp dung lượng lớn.

Ví dụ:

* Ghi video.
* Lưu checkpoint mô hình AI.
* Sao chép dữ liệu.

### Thông tin ghi nhận

* Kích thước dữ liệu.
* Thời gian thực hiện.
* Tốc độ ghi (MB/s hoặc GB/s).

---

## 7. Random Read Benchmark

### Mục đích

Đo tốc độ đọc ngẫu nhiên trên nhiều vị trí của thiết bị lưu trữ.

### Ý nghĩa

Đây là bài kiểm tra quan trọng đối với:

* Khởi động hệ điều hành.
* Cơ sở dữ liệu.
* Ứng dụng có nhiều tệp nhỏ.

### Thông tin ghi nhận

* Kích thước khối dữ liệu (Block Size).
* Thời gian thực hiện.
* Tốc độ đọc.
* IOPS.

---

## 8. Random Write Benchmark

### Mục đích

Đo tốc độ ghi ngẫu nhiên.

### Ý nghĩa

Bài kiểm tra đánh giá khả năng xử lý nhiều yêu cầu ghi đồng thời.

### Thông tin ghi nhận

* Kích thước khối dữ liệu.
* Thời gian thực hiện.
* Tốc độ ghi.
* IOPS.

---

## 9. IOPS Benchmark

### Mục đích

Đo số lượng thao tác vào/ra mà thiết bị có thể xử lý trong một giây.

### Ý nghĩa

IOPS là chỉ số quan trọng đối với:

* Máy chủ.
* Cơ sở dữ liệu.
* Máy ảo.
* Hệ thống AI.
* Ứng dụng yêu cầu truy cập dữ liệu liên tục.

### Thông tin ghi nhận

* Read IOPS.
* Write IOPS.
* Queue Depth.
* Block Size.

---

## 10. Kết quả Benchmark

Sau khi hoàn thành, module sẽ tạo báo cáo trong thư mục:

```text
reports/storage/
```

Ví dụ:

```text
reports/
└── storage/
    └── storage_result.txt
```

Báo cáo có thể bao gồm:

* Thông tin thiết bị lưu trữ.
* Kết quả từng bài benchmark.
* Thời gian thực hiện.
* Tổng hợp hiệu năng.

---

## 11. Logging

Trong quá trình benchmark, module sẽ ghi lại các sự kiện quan trọng vào hệ thống Logging.

Ví dụ:

* Bắt đầu benchmark.
* Thu thập thông tin thiết bị.
* Bắt đầu Sequential Read.
* Hoàn thành Sequential Write.
* Hoàn thành Random Read.
* Hoàn thành IOPS Benchmark.
* Kết thúc benchmark.

---

## 12. Công cụ Benchmark

Dự án ưu tiên sử dụng các công cụ phổ biến trên Linux để thực hiện benchmark thiết bị lưu trữ.

Ví dụ:

* fio
* dd (đối với các bài kiểm tra đơn giản)
* lsblk
* df
* nvme-cli (đối với thiết bị NVMe)

Các công cụ có thể thay đổi hoặc được mở rộng trong các phiên bản tiếp theo.

---

## 13. Khả năng mở rộng

Trong tương lai, module có thể bổ sung:

* Benchmark nhiều ổ đĩa đồng thời.
* Kiểm tra độ trễ (Latency).
* Benchmark theo nhiều Queue Depth.
* Benchmark với nhiều Block Size khác nhau.
* So sánh hiệu năng giữa nhiều thiết bị lưu trữ.
* Theo dõi nhiệt độ SSD (nếu phần cứng hỗ trợ).

---

## 14. Kết luận

Storage Benchmark là thành phần quan trọng của AI Hardware Benchmark Suite, giúp đánh giá toàn diện hiệu năng của thiết bị lưu trữ. Kết quả benchmark hỗ trợ người dùng phân tích, tối ưu và so sánh khả năng lưu trữ của các hệ thống trong nhiều môi trường và khối lượng công việc khác nhau.
