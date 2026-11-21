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
|   3 | Nguyễn Thanh Tùng        | 2A202603446 | 26ai.tungpt@vinuni.edu.vn   | [github.com/hunter2996](https://github.com/hunter2996)      | TV3 · Người gắn nhãn 1 & QA / Spec |
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

## Nguyễn Thanh Tùng — 2A202603446 (TV3)

### Phần việc phụ trách

Người gắn nhãn 1 & QA / Spec (`TIMELINE.md`):

- **Chặng 0–2 (CP1–CP2 · Nhiệm vụ A & B):** theo dõi điều kiện "Xong khi" trong `CHECKPOINTS.md` và `RUBRIC.md`; kiểm tra gate A1 (`ĐẠT` đủ 3 phép thử), kiểm tra 2 lỗi hay gặp ở A2 (`keep_default_na=False`, tử số mọi lần chạy, mẫu số chỉ đếm `thanh_cong`), nhãn `simulated`, câu trả lời A3–A4; kiểm tra B3 (phân biệt `2 lần` rẻ nhất hệ thống vs `1 lần` thấp nhất CPS) và B4 (đủ cả `9` phút & `15,3` phút + mức hoà vốn).
- **Chặng 3 (CP3 · Nhiệm vụ C):** đọc và gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (`Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm`), so nhãn tính tỉ lệ đồng thuận, rà bảng khắc phục 5 ca (event/ngưỡng/tần suất đo được, 1 vai trò phụ trách) trong `report/team/bang_loi.md`.
- **Chặng 4 (CP4 · Nhiệm vụ D):** kiểm tra 5 câu tách tác động D2 và soạn + QA 3 luật dừng 4 vế (`NẾU – TRONG – THÌ – KHÔNG THÌ`) trong `report/team/pilot_plan.yaml`.
- **Chặng 5 (CP5 · Nhiệm vụ E):** chủ trì `report/team/chi_so.md` (bổ sung 1 chỉ số dùng & 1 chỉ số an toàn tự đề xuất + kiểm tra chéo event có `trace_id`), phối hợp TV1 kiểm tra khớp số E2 với `bang_chi_phi.md` và nhãn `simulated`.
- **Chặng 6–7 (Duyệt chéo & QA cuối):** chạy kiểm chứng kỹ thuật toàn bộ `report/team/` (quét từ cấm, quét dấu `?` ngoài comment YAML, rà nhãn `simulated`, kiểm tra không ghi `"cả đội"` làm người phụ trách) và cùng TV4 chấm nhóm `n + 1` vào `report/team/phieu_cham.md` ở phiên 17:00.

### Đóng góp cụ thể

- **Chặng 1–2 (CP1–CP2):** cài `.venv` Python 3.12 trên máy thứ 2 chạy `src/lab13.py` qua gate A1 (`1,20 · 1,25 · 1,25 · ĐẠT`); đối chiếu số liệu thô `logix_runs.csv` (`1.624` runs, `5.600` tool calls) và `logix_requests.csv` (`1.200` reqs, `978` thành công, `890` phút xem lại và `1.132` phút làm lại simulated); bổ sung nhãn `[simulated]` và chi phí cả hệ thống (`5.865 đ/yc = 0,49×`) trong `report/team/bang_chi_phi.md`; QA xác nhận B3 (`6.901.220 đ` ở 2 lần vs `4.111 đ` ở 1 lần) và B4 (`0,98×` / `1,03×`, hoà vốn `≤ 5,1` / `≤ 4,8` phút).
- **Chặng 3 (CP3):** gắn nhãn độc lập 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (`4` Do người dùng · `5` Hệ thống · `4` Ngữ cảnh · `4` Giới hạn hệ thống · `3` Ngầm), đối chiếu bộ nhãn của TV4 đạt đồng thuận `20/20 = 100%` (`≥ 80%`) và hoàn thiện `report/team/bang_loi.md` gồm bảng 2 bộ nhãn, quy tắc phân biệt các ca dễ nhầm và bảng khắc phục 5 ca (`Ca 9, 7, 18, 4, 17`) có ngưỡng đo được và đúng 1 vai trò phụ trách/dòng.
- **Chặng 4 (CP4):** QA 5 câu D2 (`identifiability`) và viết đủ 3 luật dừng 4 vế (`An toàn`: đối chứng `+2 điểm` / trần `6%` / trùng lặp `>= 1` trong `3 ngày`, Giám đốc vận hành tắt trong 30 phút; `Chi phí`: `> 8.000 đ` hoặc làm lại `> 7%` trong `2 tuần`, PM thu hẹp về `noi_dia` + giới hạn 2 lần; `Sử dụng`: bỏ qua `> 40%` hoặc mở trợ lý `< 50%` trong `1 tuần`, Trưởng nhóm CSKH phỏng vấn 5 nhân viên trong 3 ngày) trong `report/team/pilot_plan.yaml`.
- **Chặng 5 & Chặng 7 (CP5 & QA):** bổ sung 2 chỉ số tự đề xuất vào `report/team/chi_so.md` (*Tỉ lệ độ sâu sử dụng trợ lý* qua `agent_suggestion_shown` / `refund_request_created`, và *Tỉ lệ hoàn sai tiền qua kiểm mẫu hằng tuần* qua `audit_sample_checked`), cập nhật kiểm tra chéo event có `trace_id`, kiểm tra E2 khớp 100% với B1/B4/A4; chạy kiểm chứng toàn diện `lab13.py` (A1–E1), `yaml.safe_load`, quét dấu `?` và từ cấm.

### Bằng chứng

- Commit `0dc1df6` (Chặng 1) và commit hoàn thiện CP3–CP5 & QA
- `TIMELINE.md` (cập nhật tên & MSSV TV3)
- `report/team/bang_chi_phi.md` (QA A1–A4, B1–B4)
- `report/team/bang_loi.md` (2 bộ nhãn độc lập `20/20 = 100%`, bảng khắc phục 5 ca)
- `report/team/pilot_plan.yaml` (3 luật dừng 4 vế, pass `yaml.safe_load`, hết dấu `?`)
- `report/team/chi_so.md` (đủ 5 chỉ số E1, kiểm tra chéo 10 event có `trace_id`, QA E2)
- `report/team/2A202603446_NguyenThanhTung.md`

## Lý Thanh Lâm — 2A202603475 (TV4)

### Phần việc phụ trách

Người gắn nhãn 2 kiêm giữ hồ sơ / PM (`TIMELINE.md`):

- **Chặng 0–2 (CP1–CP2):** thiết lập thông tin nhóm và khung 4 thành viên trong `TEAM.md`; khởi tạo và cập nhật `report/team/ho_so_launch_v0.md` (Mục 1, 2, 3, 7 ở trạng thái `Giả lập`, gắn nhãn `[simulated]` và gán đúng 1 vai trò phụ trách); phối hợp kiểm tra câu trả lời A2–A4, B1–B4 trong `report/team/bang_chi_phi.md` (≤ 3 dòng/câu, có số).
- **Chặng 3 (CP3 · Nhiệm vụ C):** gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (Vai Người gắn nhãn 2), so nhãn với TV3 (`Nguyễn Thanh Tùng`) đạt đồng thuận `20/20 = 100%`, hoàn thiện phương án khắc phục cho ca lỗi **Ngữ cảnh** (`Ca 18`) và ghép 5 ca vào `report/team/bang_loi.md`.
- **Chặng 4–7 (CP4–CP5 & Đóng gói):** soạn thảo giải trình đánh đổi cỡ mẫu D1 (chấp nhận MDE 6 điểm với 20 + 20 nhân viên, power 0,64 ở mức 5 điểm); tổng hợp `report/team/group_report.md` và hoàn thiện đầy đủ 7 mục cùng đề xuất cuối `Go có điều kiện` trong `report/team/ho_so_launch_v0.md` sẵn sàng cho phiên duyệt chéo Gate 2a.

### Đóng góp cụ thể (tính tới thời điểm hiện tại)

- Hoàn thiện thông tin phân vai trong `TEAM.md` và `TIMELINE.md`; cập nhật đầy đủ 7 mục trong `report/team/ho_so_launch_v0.md`: Mục 1–3 & 7 (trạng thái `Giả lập`, nhãn `[simulated]`), Mục 4–6 (trạng thái `Xong, có bằng chứng` từ `chi_so.md`, `bang_loi.md`, `pilot_plan.yaml`), và chốt đề xuất **Go có điều kiện** cho phạm vi `noi_dia + hang_nang` (nêu thẳng các con số bất lợi: xem lại 100% `0,98×–1,03×` [simulated], `power = 0,64` ở mức +5 điểm, mở lại nền `4,25%` / `3,97%` phạm vi) kèm 4 điều kiện có vai trò phụ trách và ngày kiểm tra cụ thể.
- Hoàn thành gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc (Google PAIR: *Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm*) của Người gắn nhãn 2, đối chiếu với TV3 (`Nguyễn Thanh Tùng`) đạt đồng thuận `20/20 = 100%` (khớp `20/20`), và đóng góp phương án khắc phục ca lỗi **Ngữ cảnh** (`Ca 18`, phụ trách `Trưởng nhóm CSKH`) vào `report/team/bang_loi.md`.
- Soạn giải trình đánh đổi cỡ mẫu CP4 (40 nhân viên chia 20 + 20 có trần hiệu dụng 1.000 < 1.251 ở MDE 5 điểm nên chọn MDE 6 điểm cần 859/nhóm, m ≥ 299 yêu cầu/người, DE = 6,96, chấp nhận power 0,6417 ở mức 5 điểm) và hoàn thiện báo cáo nhóm `report/team/group_report.md` (8 mục, dẫn đủ số chính từ CP1–CP5).

### Bằng chứng

- `TEAM.md`, `TIMELINE.md`
- `report/team/ho_so_launch_v0.md` (đủ 7 mục, đúng trạng thái `Giả lập` / `Xong, có bằng chứng`, mỗi mục 1 vai trò, chốt đề xuất `Go có điều kiện` 1 trang)
- `report/team/bang_loi.md` (bộ nhãn độc lập Người gắn nhãn 2, đồng thuận `20/20 = 100%` cùng TV3, ca lỗi Ngữ cảnh `Ca 18`)
- `report/team/group_report.md` (báo cáo tổng hợp nhóm 8 mục cho toàn bộ phần A–E)
- `report/team/2A202603475_LyThanhLam.md` (báo cáo cá nhân, bộ nhãn độc lập 20 ca và đối chiếu Gate 2a)
