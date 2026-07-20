# X. Quy trình phát triển dự án (Development Workflow)

## Mục đích

Tài liệu này mô tả quy trình phát triển của dự án nhằm đảm bảo:

- Dễ quản lý mã nguồn.
- Dễ theo dõi tiến độ.
- Hạn chế lỗi khi phát triển.
- Giữ nhánh `main` luôn ở trạng thái ổn định.

---

# Mô hình Branch

```
main
│
├── feature/project-foundation
├── feature/system-info
├── feature/cpu-benchmark
├── feature/memory-benchmark
├── feature/storage-benchmark
├── feature/gpu-benchmark
└── feature/ai-benchmark
```

---

# Quy trình làm việc

Mỗi chức năng được phát triển trên một branch riêng.

Quy trình thực hiện:

```
main
   │
   ├── Tạo feature branch
   │
   ▼
feature/...
   │
   ├── Viết mã nguồn
   ├── Commit nhiều lần
   ├── Kiểm tra
   ├── Hoàn thành
   │
   ▼
Merge vào main
```

---

# Tiến trình phát triển

| Giai đoạn | Branch | Trạng thái |
|-----------|--------|:---------:|
| Project Foundation | `feature/project-foundation` | 🔄 |
| System Information | `feature/system-info` | ⬜ |
| CPU Benchmark | `feature/cpu-benchmark` | ⬜ |
| Memory Benchmark | `feature/memory-benchmark` | ⬜ |
| Storage Benchmark | `feature/storage-benchmark` | ⬜ |
| GPU Benchmark | `feature/gpu-benchmark` | ⬜ |
| AI Benchmark | `feature/ai-benchmark` | ⬜ |

**Chú thích**

- ⬜ Chưa bắt đầu
- 🔄 Đang thực hiện
- ✅ Hoàn thành

---

# Quy trình Commit

Trong quá trình phát triển một feature:

```
feature/project-foundation

├── Commit 1
├── Commit 2
├── Commit 3
├── ...
└── Commit cuối
```

Sau khi hoàn thành:

```
git checkout main
git pull
git merge feature/project-foundation
git push origin main
```

---

# Quy tắc Commit

Sử dụng chuẩn Conventional Commits.

Ví dụ:

```
feat: add benchmark framework
feat: implement cpu benchmark
feat: implement gpu benchmark

fix: fix logger bug
fix: correct memory benchmark

docs: update architecture
docs: add reporting documentation

refactor: improve benchmark manager

test: add benchmark unit tests
```

---

# Tiến độ hiện tại

## Documentation

| Công việc | Trạng thái |
|-----------|:---------:|
| README | ✅ |
| Roadmap | ✅ |
| Architecture | ✅ |
| Logging | ✅ |
| Reporting | ✅ |
| CPU Benchmark | ✅ |
| Memory Benchmark | ✅ |
| Storage Benchmark | ✅ |
| GPU Benchmark | ✅ |
| AI Benchmark | ✅ |

---

## Development

| Giai đoạn | Trạng thái |
|-----------|:---------:|
| Project Structure | ✅ |
| Documentation | ✅ |
| Project Foundation | ⬜ |
| System Information | ⬜ |
| CPU Benchmark | ⬜ |
| Memory Benchmark | ⬜ |
| Storage Benchmark | ⬜ |
| GPU Benchmark | ⬜ |
| AI Benchmark | ⬜ |

---

# Nguyên tắc phát triển

- Mỗi feature phát triển trên một branch riêng.
- Không phát triển trực tiếp trên `main`.
- Chỉ merge vào `main` khi feature đã hoàn thành.
- Mỗi commit nên thực hiện một thay đổi rõ ràng.
- Luôn cập nhật tài liệu khi có thay đổi lớn.
- Sau mỗi giai đoạn hoàn thành, cập nhật bảng tiến độ trong tài liệu này.

---

# Lộ trình

```
Documentation
        │
        ▼
Project Foundation
        │
        ▼
System Information
        │
        ▼
CPU Benchmark
        │
        ▼
Memory Benchmark
        │
        ▼
Storage Benchmark
        │
        ▼
GPU Benchmark
        │
        ▼
AI Benchmark
        │
        ▼
Release v1.0
```