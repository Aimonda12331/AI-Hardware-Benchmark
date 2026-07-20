# V. CPU Benchmark

## 1. Giới thiệu

CPU Benchmark là module dùng để đánh giá hiệu năng xử lý của bộ vi xử lý (CPU).

Module này cung cấp các bài kiểm tra nhằm đo khả năng tính toán, hiệu suất đơn luồng, đa luồng và năng lực xử lý các phép toán số học của CPU. Kết quả benchmark giúp người dùng đánh giá và so sánh hiệu năng giữa các hệ thống khác nhau.

---

## 2. Mục tiêu

Module CPU Benchmark được xây dựng nhằm:

* Đánh giá hiệu năng tổng thể của CPU.
* Đo hiệu năng đơn luồng và đa luồng.
* Kiểm tra khả năng xử lý phép toán ma trận.
* Kiểm tra độ ổn định của CPU khi tải cao.
* Cung cấp dữ liệu phục vụ phân tích và so sánh.

---

## 3. Các bài Benchmark

Module bao gồm các bài kiểm tra sau:

* CPU Detection
* CPU Stress Test
* Single-thread Benchmark
* Multi-thread Benchmark
* Matrix Multiplication Benchmark

---

## 4. CPU Detection

### Mục đích

Thu thập thông tin phần cứng của CPU trước khi thực hiện benchmark.

### Thông tin cần thu thập

* Tên CPU
* Nhà sản xuất
* Kiến trúc CPU
* Số nhân vật lý (Physical Cores)
* Số luồng xử lý (Logical Threads)
* Xung nhịp cơ bản
* Xung nhịp tối đa
* Bộ nhớ đệm (L1, L2, L3)
* Mức sử dụng CPU hiện tại

---

## 5. CPU Stress Test

### Mục đích

Đưa CPU hoạt động ở mức tải cao trong một khoảng thời gian xác định nhằm đánh giá:

* Độ ổn định.
* Khả năng duy trì hiệu năng.
* Khả năng xử lý tải liên tục.

### Thông tin ghi nhận

* Mức sử dụng CPU (%)
* Thời gian thực thi
* Nhiệt độ CPU (nếu có thể thu thập)
* Tần số hoạt động

---

## 6. Single-thread Benchmark

### Mục đích

Đánh giá hiệu năng của một luồng xử lý duy nhất.

### Ứng dụng

Bài benchmark này phản ánh hiệu năng trong các ứng dụng phụ thuộc vào một luồng xử lý, chẳng hạn:

* Một số trò chơi.
* Các tác vụ văn phòng.
* Một số thuật toán tuần tự.

### Kết quả

* Thời gian thực hiện.
* Số phép tính mỗi giây.
* Điểm benchmark.

---

## 7. Multi-thread Benchmark

### Mục đích

Đánh giá hiệu năng khi CPU sử dụng đồng thời nhiều luồng xử lý.

### Ứng dụng

* Biên dịch chương trình.
* Xử lý dữ liệu lớn.
* Mô phỏng khoa học.
* Deep Learning.
* Render hình ảnh và video.

### Kết quả

* Hiệu suất đa luồng.
* Tốc độ xử lý.
* Mức sử dụng CPU.
* Điểm benchmark.

---

## 8. Matrix Multiplication Benchmark

### Mục đích

Đánh giá khả năng tính toán số học thông qua phép nhân ma trận.

Đây là bài kiểm tra phổ biến vì phép nhân ma trận được sử dụng rộng rãi trong:

* Trí tuệ nhân tạo (AI).
* Machine Learning.
* Deep Learning.
* Xử lý tín hiệu.
* Mô phỏng khoa học.

### Thông tin ghi nhận

* Kích thước ma trận.
* Thời gian thực hiện.
* Hiệu năng tính toán.
* Số phép toán mỗi giây.

---

## 9. Kết quả Benchmark

Sau khi hoàn thành, module sẽ tạo báo cáo trong thư mục:

```text
reports/cpu/
```

Ví dụ:

```text
reports/
└── cpu/
    └── cpu_result.txt
```

Thông tin báo cáo có thể bao gồm:

* Thông tin CPU.
* Kết quả từng bài benchmark.
* Thời gian thực thi.
* Tổng hợp điểm benchmark.

---

## 10. Logging

Trong quá trình thực thi, module sẽ ghi lại các sự kiện quan trọng vào hệ thống Logging.

Ví dụ:

* Bắt đầu benchmark.
* Thu thập thông tin CPU.
* Bắt đầu Stress Test.
* Hoàn thành Single-thread Benchmark.
* Hoàn thành Multi-thread Benchmark.
* Kết thúc benchmark.

---

## 11. Khả năng mở rộng

Trong tương lai, module có thể bổ sung:

* Benchmark dấu phẩy động (Floating Point).
* Benchmark số nguyên (Integer).
* Benchmark mã hóa và giải mã.
* Benchmark nén và giải nén dữ liệu.
* Benchmark SIMD (SSE, AVX, AVX2, AVX-512).
* So sánh hiệu năng giữa nhiều CPU.

---

## 12. Kết luận

CPU Benchmark là một trong những thành phần cốt lõi của AI Hardware Benchmark Suite. Module này cung cấp các bài kiểm tra toàn diện nhằm đánh giá khả năng xử lý của CPU, đồng thời tạo dữ liệu phục vụ việc phân tích, so sánh và tối ưu hóa hiệu năng hệ thống.
