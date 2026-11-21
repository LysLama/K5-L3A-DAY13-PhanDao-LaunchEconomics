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
|   3 | Phạm Thanh Tùng          | 2A202603446 | 26ai.tungpt@vinuni.edu.vn   | [github.com/hunter2996](https://github.com/hunter2996)      | TV3 · Người gắn nhãn 1 & QA / Spec |
|   4 | Lý Thanh Lâm             | 2A202603475 | 26ai.lamlt@vinuni.edu.vn    | [github.com/LysLama](https://github.com/LysLama)            | TV4 · Người gắn nhãn 2 kiêm giữ hồ sơ / Leader |

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
- Rà bảng A và B, đối chiếu D1, E1, E2 với stdout của `lab13.py`.

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

- Commit `563a57c` (Chặng 0), `0ccf501` (A1–A4), `c2d2c36` (B1–B4), `0b3d279` (D1, E1, E2)
- `src/lab13.py` (khối D1, E1), `report/team/bang_chi_phi.md`, `report/team/chi_so.md`
- `report/team/2A202603442_NguyenDacTuanNghia.md`

## Phạm Thanh Tùng — 2A202603446 (TV3)

### Phần việc phụ trách

Người gắn nhãn 1 & QA / Spec (`TIMELINE.md`):

- **Chặng 0 & Chặng 1 (CP1 · Nhiệm vụ A — đã hoàn thành):** mở `CHECKPOINTS.md` và `RUBRIC.md` theo dõi điều kiện "Xong khi"; kiểm tra gate A1 (đủ 3 phép thử ĐẠT trước khi sang A2); kiểm tra 2 lỗi hay gặp ở A2 (`keep_default_na=False`, tử số tính mọi lần chạy kể cả lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`); kiểm tra gắn nhãn `simulated`; rà soát câu trả lời A3 (kèm dẫn chứng từ 2 cột giữa) và A4; đối chiếu toàn bộ số A1–A4 với slide đáp án (sai số `≤ 2%`).
- **Các chặng tiếp theo (CP2–CP5 & Duyệt chéo):** rà B3/B4 ở Chặng 2; gắn độc lập 20 ca lỗi và chọn 5 ca bảng khắc phục ở Chặng 3; soạn D2 và 3 luật dừng 4 vế trong `pilot_plan.yaml` ở Chặng 4; chủ trì `chi_so.md` ở Chặng 5; chấm chéo nhóm `n+1` vào `phieu_cham.md` ở Chặng 6; rà QA cuối buổi ở Chặng 7.

### Đóng góp cụ thể (Chặng 1)

- Cài đặt môi trường `.venv` (Python 3.12.10) trên máy thứ 2 trong nhóm và chạy kiểm chứng `src/lab13.py`: gate A1 in `Ba phép thử đáp án biết trước: ĐẠT` (`1,20 · 1,25 · 1,25`).
- Kiểm tra logic hàm `mo_hinh` trong `src/lab13.py` và đối chiếu trực tiếp trên `logix_runs.csv` (1.624 lần chạy, 5.600 tool calls, tổng phần chạy lại `attempt > 1` = 93.804 đ) & `logix_requests.csv` (1.200 yêu cầu, đọc với `keep_default_na=False`: 978 `thanh_cong`, 148 `chuyen_nhan_vien`, 74 `lam_lai`; 890 phút xem lại và 1.132 phút làm lại simulated).
- Soát và bổ sung chuẩn QA cho phần A trong `report/team/bang_chi_phi.md`: gắn nhãn `[simulated]` cho cột giá trị giả lập của bảng A3, A4 và ngưỡng hoà vốn A4; bổ sung chi phí cả hệ thống (5.865 đ/yêu cầu = 0,49× [simulated]) khớp với `ho_so_launch_v0.md`; rà câu trả lời A3 đầy đủ dẫn chứng 2 cột giữa (`27,3%` thành công, `2,32` lần/yêu cầu, tỉ lệ `ok` theo attempt `30,0% → 11,4% → 2,2%`) và phạm vi thu hẹp `noi_dia + hang_nang`.
- Đối chiếu toàn bộ số A1–A4 với slide chữa Nhiệm vụ A (slide 66) và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: khớp hoàn toàn trong ngưỡng sai số `≤ 2%`; kiểm tra không có từ cấm trong `report/team/`.

### Bằng chứng

- `TIMELINE.md` (cập nhật tên & MSSV TV3)
- `report/team/bang_chi_phi.md` (QA phần A1–A4, nhãn `simulated`, câu trả lời ≤ 3 dòng có số)
- `report/team/ho_so_launch_v0.md` (đối chiếu Mục 1 & Mục 3 trạng thái `Giả lập`, người phụ trách 1 vai trò)
- `report/team/2A202603446_PhamThanhTung.md`

## Lý Thanh Lâm — 2A202603475 (TV4)

### Phần việc phụ trách

Người gắn nhãn 2 kiêm giữ hồ sơ / PM (`TIMELINE.md`):

- **Chặng 0–2 (CP1–CP2):** thiết lập thông tin nhóm và khung 4 thành viên trong `TEAM.md`; khởi tạo và cập nhật `report/team/ho_so_launch_v0.md` (Mục 1, 2, 3, 7 ở trạng thái `Giả lập`, gắn nhãn `[simulated]` và gán đúng 1 vai trò phụ trách); phối hợp kiểm tra câu trả lời A2–A4, B1–B4 trong `report/team/bang_chi_phi.md` (≤ 3 dòng/câu, có số).
- **Chặng 3 (CP3 · Nhiệm vụ C):** gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (Vai Người gắn nhãn 2); chuẩn bị phương án khắc phục cho ca lỗi **Ngữ cảnh** (ca 18) và sẵn sàng tổng hợp hai bộ nhãn độc lập + 5 ca khắc phục (ghép với đề xuất của TV1, TV2, TV3) vào `report/team/bang_loi.md` và cập nhật Mục 5 hồ sơ sau khi đối chiếu với TV3.
- **Chặng 4–7 (CP4–CP5 & Đóng gói):** soạn thảo giải trình đánh đổi cỡ mẫu D1 (chấp nhận MDE 6 điểm với 20 + 20 nhân viên, power 0,64 ở mức 5 điểm); tổng hợp `report/team/group_report.md` và hoàn thiện Mục 4, 5, 6 cùng đề xuất cuối trong `report/team/ho_so_launch_v0.md`.

### Đóng góp cụ thể (tính tới thời điểm hiện tại)

- Hoàn thiện thông tin phân vai trong `TEAM.md` và `TIMELINE.md`; kiểm tra và duy trì `report/team/ho_so_launch_v0.md` cho các mục đã có số liệu từ CP1–CP2 & E2 (Mục 1: 4.472 đ toàn mẫu, 3.414 đ trong phạm vi, cộng cố định 4.599 đ [simulated]; Mục 2: Làm lại +51,8%, Xem lại +40,7%, Lương +23,1%, xem lại 100% lên 0,98×–1,03× [simulated]; Mục 3: 0,38× ở đủ tải, 0,48× ở nửa tải, toàn hệ thống 0,49×, loại `quoc_te` 1,88× [simulated]; Mục 7: 3 dòng rủi ro kinh tế từ B1, B4, A4 [simulated]).
- Thực hiện gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc (Google PAIR: *Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm*) của Người gắn nhãn 2 và ghi nhận vào báo cáo cá nhân `report/team/2A202603475_LyThanhLam.md` (giữ nguyên `report/team/bang_loi.md` chờ so nhãn với TV3 để đảm bảo quy tắc độc lập).
- Soạn sẵn dòng khắc phục cho ca lỗi **Ngữ cảnh** (Ca 18: phát hiện qua tỉ lệ `ticket_reopened` với lý do thắc mắc số tiền hoàn dù kiểm tra sổ cái thấy tính đúng theo tuần; khắc phục bằng mẫu thông báo luôn hiển thị rõ công thức `30.000 đ × 50% = 15.000 đ`; phụ trách: `Trưởng nhóm CSKH`) để ghép cùng đề xuất của TV1 (Hệ thống, Giới hạn hệ thống) và TV2 (Ngầm, Do người dùng).
- Soạn giải trình đánh đổi cỡ mẫu CP4 (40 nhân viên chia 20 + 20 có trần hiệu dụng 1.000 < 1.251 ở MDE 5 điểm nên chọn MDE 6 điểm cần 859/nhóm, m ≥ 299 yêu cầu/người, DE = 6,96, chấp nhận power 0,6417 ở mức 5 điểm) và khởi tạo toàn bộ nội dung A, B, D1, E1, E2 vào `report/team/group_report.md`.

### Bằng chứng

- `TEAM.md`, `TIMELINE.md`
- `report/team/ho_so_launch_v0.md` (khung 7 mục và các mục 1, 2, 3, 7 đã khóa số liệu `[simulated]`)
- `report/team/group_report.md` (tổng hợp mục 1–8 cho các phần A, B, D1, E1, E2 đã hoàn thành)
- `report/team/2A202603475_LyThanhLam.md` (bộ nhãn độc lập 20 ca của Người gắn nhãn 2, đề xuất khắc phục lỗi Ngữ cảnh, giải trình đánh đổi D1 và bản nháp Mục 4–6 + Đề xuất `Go có điều kiện`)
