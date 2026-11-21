# Team

## Thông tin nhóm

- Tên nhóm: PhanDao
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-PhanDao-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: https://github.com/LysLama/K5-L3A-DAY13-PhanDao-LaunchEconomics
- Nhánh nộp: `main`
- Commit chốt: (điền khi push bản cuối)

## Thành viên

| STT | Họ tên                   | MSSV        | Email                       | GitHub                                                     | Vai trò |
| --: | -------------------------- | ----------- | --------------------------- | ---------------------------------------------------------- | -------- |
|   1 | Phạm Trung Kiên          | 2A202603479 | 26ai.kienpt@vinuni.edu.vn   | [github.com/kienpham0607](https://github.com/kienpham0607)  | Người viết code GĐ1 (TV1) |
|   2 | Nguyễn Đắc Tuấn Nghĩa | 2A202603442 | 26ai.nghiandt@vinuni.edu.vn | [github.com/dacnghia-lx](https://github.com/dacnghia-lx)    | TV2 · Người kiểm số (CP1–CP2) → Người viết code (CP3–CP5) |
|   3 | Phạm Thanh Tùng          | 2A202603446 | 26ai.tungpt@vinuni.edu.vn   | [github.com/hunter2996](https://github.com/hunter2996)      |          |
|   4 | Lý Thanh Lâm             | 2A202603475 | 26ai.lamlt@vinuni.edu.vn    | [github.com/LysLama](https://github.com/LysLama)            | Leader   |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Phạm Trung Kiên — 2A202603479 (TV1)

### Phần việc phụ trách

Người viết code giai đoạn 1: `src/lab13.py` cho nhiệm vụ A và B; điền `report/team/pilot_plan.yaml` (trừ 3 luật dừng của TV3); liệt kê event và kiểm tra chéo trong `report/team/chi_so.md`; đề xuất khắc phục hai loại lỗi Hệ thống và Giới hạn hệ thống để TV4 ghép vào `bang_loi.md` sau khi có nhãn.

### Đóng góp cụ thể

- Viết A1, `mo_hinh`, A3, A4, B1–B4 trong `src/lab13.py` và chạy trên máy này tới khi A1 in ĐẠT.
- Kiểm tay câu D1.e (m ≥ 299, DE = 6,96) và điền D1, D2, đánh đổi, các trường YAML.
- Liệt kê 10 event có `trace_id` và mục kiểm tra chéo chỉ số ↔ event.

### Bằng chứng

- `src/lab13.py`
- `report/team/pilot_plan.yaml` (3 dòng `stop_rules` còn `?`, chờ TV3)
- `report/team/chi_so.md` (mục Danh sách event và Kiểm tra chéo)
- `report/team/2A202603479_PhamTrungKien.md`

## Nguyễn Đắc Tuấn Nghĩa — 2A202603442 (TV2)

### Phần việc phụ trách

Người kiểm số ở CP1–CP2 (`report/team/bang_chi_phi.md`), nhận vai Người viết code từ CP3: code D1 và E1 trong `src/lab13.py`, điền E1 và E2 trong `report/team/chi_so.md`, kiểm tra `pilot_plan.yaml`, chạy lại toàn bộ trên máy thứ 2; đề xuất khắc phục lỗi Ngầm và Do người dùng; trả lời phản biện Gate 2a.

### Đóng góp cụ thể

- Tính độc lập đối chiếu A1–A2 (token 245.585 đ, tool 84.000 đ, xem lại 1.780.000 đ, làm lại 2.264.000 đ [simulated]) và điền đủ A1–A4, B1–B4.
- Viết `co_mau`, D1 a–e (1.251 · 3.103 · 1.000 · 300 · m ≥ 299, DE 6,96, power 0,6417) và E1 (82,83% · 27,12% · 4,25%).
- Điền 3 dòng rủi ro kinh tế E2 lấy số từ A4, B1, B4.

### Bằng chứng

- Commit `563a57c`, `0ccf501`, `c2d2c36` và commit CP4–CP5
- `src/lab13.py` (khối D1, E1), `report/team/bang_chi_phi.md`, `report/team/chi_so.md`
- `report/team/2A202603442_NguyenDacTuanNghia.md`
