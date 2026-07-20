# AI Hardware Benchmark Suite

Bộ công cụ benchmark dành cho máy tính AI, Deep Learning và Embedded Linux.

Hỗ trợ đánh giá hiệu năng:

- GPU
- CPU
- RAM
- SSD
- CUDA
- PyTorch
- Linux Environment

---

# Cấu trúc dự án

```text
AI-Hardware-Benchmark/
│
├── benchmark/
│   ├── gpu_stress_test.py
│   ├── gpu_benchmark.py
│   ├── cpu_benchmark.py
│   └── ram_benchmark.py
│
├── scripts/
│   ├── run_gpu_test.sh
│   ├── monitor_gpu.sh
│   ├── benchmark_gpu.sh
│   ├── benchmark_cpu.sh
│   ├── benchmark_ram.sh
│   ├── benchmark_disk.sh
│   ├── system_info.sh
│   ├── run_all.sh
│   └── install_tools.sh
│
├── reports/
├── logs/
├── requirements.txt
└── README.md
```

---

# Chức năng

| Thành phần | Mục đích |
|------------|----------|
| **GPU Stress Test** | Stress GPU, kiểm tra VRAM, CUDA và độ ổn định |
| **GPU Benchmark** | Benchmark FP32, FP16, Tensor Core, GFLOPS/TFLOPS |
| **CPU Benchmark** | Đánh giá hiệu năng CPU đơn luồng và đa luồng |
| **RAM Benchmark** | Kiểm tra tốc độ đọc, ghi, sao chép và băng thông RAM |
| **Disk Benchmark** | Đo tốc độ SSD (Sequential, Random, IOPS) bằng `fio` |
| **System Info** | Thu thập thông tin phần cứng và môi trường |
| **Run All** | Chạy toàn bộ benchmark và xuất báo cáo |

---

# Kết quả

## Reports

```
reports/
├── system_info.txt
├── gpu_result.txt
├── cpu_result.txt
├── ram_result.txt
├── disk_result.txt
└── summary.txt
```

## Logs

```
logs/
```

---

# Yêu cầu

- Ubuntu 22.04+
- Python 3.10+
- CUDA Toolkit
- NVIDIA Driver
- PyTorch (CUDA)

---

# Cài đặt

Tạo môi trường:

```bash
python3 -m venv .venv
source .venv/bin/activate
```
Cài thư viện:
```bash
pip install -r requirements.txt
```
Cài công cụ benchmark:
```bash
chmod +x scripts/install_tools.sh
./scripts/install_tools.sh
```

---

# Sử dụng

Benchmark GPU

```bash
./scripts/benchmark_gpu.sh
```

Benchmark CPU

```bash
./scripts/benchmark_cpu.sh
```

Benchmark RAM

```bash
./scripts/benchmark_ram.sh
```

Benchmark SSD

```bash
./scripts/benchmark_disk.sh
```

Thông tin hệ thống

```bash
./scripts/system_info.sh
```

Chạy toàn bộ

```bash
./scripts/run_all.sh
```

---

# Roadmap

## Phase 1 - Project Foundation

- [ ] Project structure
- [ ] README.md
- [ ] requirements.txt
- [ ] .gitignore
- [ ] Logging system
- [ ] Report directory

---

## Phase 2 - System Information

- [ ] System Information
- [ ] CPU Information
- [ ] GPU Information
- [ ] RAM Information
- [ ] Storage Information
- [ ] CUDA Information
- [ ] PyTorch Environment

---

## Phase 3 - GPU Benchmark

- [ ] GPU Detection
- [ ] GPU Stress Test
- [ ] VRAM Stress Test
- [ ] FP32 Benchmark
- [ ] FP16 Benchmark
- [ ] Tensor Core Benchmark
- [ ] CUDA Benchmark

---

## Phase 4 - CPU Benchmark

- [ ] CPU Stress Test
- [ ] Single-thread Benchmark
- [ ] Multi-thread Benchmark
- [ ] Matrix Multiplication Benchmark

---

## Phase 5 - Memory Benchmark

- [ ] RAM Read Benchmark
- [ ] RAM Write Benchmark
- [ ] RAM Copy Benchmark
- [ ] Memory Bandwidth Benchmark

---

## Phase 6 - Storage Benchmark

- [ ] Sequential Read
- [ ] Sequential Write
- [ ] Random Read
- [ ] Random Write
- [ ] IOPS Benchmark

---

## Phase 7 - AI Benchmark

- [ ] AI Training Benchmark
- [ ] AI Inference Benchmark
- [ ] CNN Benchmark
- [ ] Batch Size Benchmark
- [ ] Mixed Precision (AMP) Benchmark

---

## Phase 8 - Reporting

- [ ] TXT Report
- [ ] JSON Report
- [ ] CSV Report
- [ ] Benchmark Summary
- [ ] Hardware Summary

---

## Phase 9 - Advanced Features

- [ ] Multi-GPU Benchmark
- [ ] Temperature Monitoring
- [ ] Power Consumption Monitoring
- [ ] Benchmark History
- [ ] Command Line Arguments
- [ ] Configuration File

---

# License

MIT License