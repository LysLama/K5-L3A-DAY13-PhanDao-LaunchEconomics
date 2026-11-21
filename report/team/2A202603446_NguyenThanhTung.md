# Báo cáo cá nhân — NguyenThanhTung-2A202603446

File này là bản của TV3. File mẫu `MSSV_HoTen.md` giữ nguyên.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thanh Tùng
- MSSV: 2A202603446
- Email: 26ai.tungpt@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1 & QA / Spec (TV3)

## 2. Phần việc phụ trách

Theo bảng phân công trong `TIMELINE.md` và `TEAM.md`:

- **Chặng 0 & Chặng 1 (CP1 · Nhiệm vụ A):** mở `CHECKPOINTS.md` và `RUBRIC.md` theo dõi điều kiện "Xong khi"; kiểm tra gate A1 (`ĐẠT` đủ 3 phép thử trước khi qua 1.2); kiểm tra 2 lỗi hay gặp ở A2 (`keep_default_na=False`, tử số cộng mọi lần chạy kể cả lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`) và nhãn `simulated`; rà soát câu trả lời A3 (dẫn chứng từ 2 cột giữa) và A4; đối chiếu slide đáp án (`≤ 2%`).
- **Chặng 2 (CP2 · Nhiệm vụ B):** đọc trước 20 ca lỗi & 5 loại Google PAIR; kiểm tra B3 phân biệt giới hạn rẻ nhất cả hệ thống (`2 lần`) với chi phí/việc thành công thấp nhất (`1 lần`); kiểm tra B4 ghi đủ cả 2 con số (`9` phút và `15,3` phút) và mức hoà vốn.
- **Chặng 3 (CP3 · Nhiệm vụ C):** gắn nhãn độc lập 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, so nhãn tính tỉ lệ đồng thuận (`≥ 80%`), rà quy tắc phân biệt các ca dễ nhầm và bảng khắc phục 5 ca trong `report/team/bang_loi.md` (phát hiện đo được, 1 vai trò phụ trách).
- **Chặng 4 (CP4 · Nhiệm vụ D):** rà soát 5 câu D2 "tách được tác động", soạn 3 luật dừng 4 vế (`NẾU – TRONG – THÌ – KHÔNG THÌ`) trong `report/team/pilot_plan.yaml`, kiểm tra hết dấu `?` và pass `yaml.safe_load`.
- **Chặng 5 (CP5 · Nhiệm vụ E):** chủ trì `report/team/chi_so.md` (điền 2 chỉ số tự đề xuất và kiểm tra chéo event có `trace_id`, dùng đúng cụm *"chỉ số trong đợt chạy thử là…"*) và cùng TV1 rà khớp số E2 với `bang_chi_phi.md`.
- **Chặng 6–7 (Duyệt chéo & QA cuối):** chạy kiểm chứng kỹ thuật toàn bộ `report/team/` theo checklist `TIMELINE.md` Bước 7.2; phối hợp TV4 chấm nhóm `n + 1` vào `report/team/phieu_cham.md` ở phiên duyệt chéo 17:00.

## 3. Đóng góp cụ thể

### 3.1. QA Chặng 1–2 (CP1–CP2 · `bang_chi_phi.md` & `src/lab13.py`)
- Thiết lập `.venv` Python 3.12.10 trong `src/` trên máy thứ 2 của nhóm và chạy trực tiếp `src/lab13.py`: gate A1 in `Ba phép thử đáp án biết trước: ĐẠT` (`1,20 · 1,25 · 1,25`), chạy thông suốt qua A1–E1.
- Kiểm tra `mo_hinh` trong `src/lab13.py` và đối chiếu trực tiếp từ `logix_runs.csv` (`1.624` lần chạy, `5.600` tool calls, `attempt > 1` = `93.804 đ`) và `logix_requests.csv` (`1.200` yêu cầu, đọc với `keep_default_na=False`: `978` `thanh_cong`, `148` `chuyen_nhan_vien`, `74` `lam_lai`; `890` phút xem lại và `1.132` phút làm lại simulated).
- Rà và chuẩn hoá QA trong `report/team/bang_chi_phi.md`: gắn nhãn `[simulated]` ở tiêu đề cột giả lập bảng A3, A4 và dòng hoà vốn A4; bổ sung chi phí cả hệ thống (`5.865 đ/yêu cầu = 0,49×` [simulated]) tại A2; rà câu A3 đủ dẫn chứng 2 cột giữa (`27,3%` thành công, `2,32` lần/yc, `ok` theo attempt `30,0% → 11,4% → 2,2%`) và nêu `doi_tac` (`0,85×`) sát ngưỡng; xác nhận B3 (`6.901.220 đ` ở 2 lần vs `4.111 đ` ở 1 lần) và B4 (`11.743 đ = 0,98×` / `12.415 đ = 1,03×`, hoà vốn `≤ 5,1` / `≤ 4,8` phút).

### 3.2. Gắn nhãn độc lập 20 ca lỗi & QA Bảng khắc phục (CP3 · `bang_loi.md`)
- Đọc độc lập 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và phân loại theo nguyên nhân gốc (Google PAIR):
  - **Do người dùng (4 ca):** `1, 6, 9, 14`
  - **Hệ thống (5 ca):** `2, 7, 8, 15, 20`
  - **Ngữ cảnh (4 ca):** `3, 10, 16, 18`
  - **Giới hạn hệ thống (4 ca):** `4, 11, 13, 19`
  - **Ngầm (3 ca):** `5, 12, 17`
- Đối chiếu với bộ nhãn độc lập của Người gắn nhãn 2 (TV4): đồng thuận `20 / 20 = 100%` (`≥ 80%`) và khớp 20/20 với bảng phân loại Google PAIR.
- Hoàn thiện `report/team/bang_loi.md` với 2 bộ nhãn độc lập, tỉ lệ đồng thuận, ghi chú nguyên tắc phân biệt cho các ca dễ nhầm (`6, 8, 9, 12, 13, 15, 18`) và rà bảng khắc phục 5 ca (`Ca 9, 7, 18, 4, 17`) đảm bảo mỗi dòng có event + ngưỡng + tần suất đo được và đúng 1 vai trò phụ trách.

### 3.3. QA Thiết kế pilot & 3 Luật dừng 4 vế (CP4 · `pilot_plan.yaml`)
- Kiểm tra đủ 5 câu tách tác động D2 (`concurrent_control`, `randomized: true`, `spillover_risk`, `predeclared`, `clusters_per_arm: 20`) và baseline mở lại thực tế (`4,25%` toàn mẫu, `3,97%` trong phạm vi `noi_dia + hang_nang`).
- Viết đủ 3 luật dừng 4 vế (`NẾU – TRONG – THÌ – KHÔNG THÌ`) vào `report/team/pilot_plan.yaml`, xoá toàn bộ dấu `?`:
  - **An toàn:** `mo_lai_trong_7_ngay` cao hơn đối chứng `>= 2 điểm` hoặc vượt trần `6%`, hoặc `>= 1` ca hoàn trùng lặp trong `3 ngày liên tiếp` → `Giám đốc vận hành LogiX-VN` tắt trong 30 phút; không thì không được mở bước tiếp theo.
  - **Chi phí:** chi phí mỗi việc thành công đo thật (chưa gồm cố định) `> 8.000 đ` hoặc tỉ lệ làm lại `> 7%` trong `2 tuần liên tiếp` → `PM trợ lý hoàn phí` thu hẹp về `noi_dia` và giới hạn 2 lần chạy; không thì không được mở rộng `hang_nang` hoặc tăng lên bước `0.50`.
  - **Sử dụng:** tỉ lệ bỏ qua gợi ý `> 40%` hoặc tỉ lệ mở trợ lý `< 50%` trong `1 tuần (7 ngày)` → `Trưởng nhóm CSKH` dừng mở rộng và phỏng vấn tối thiểu 5 nhân viên trong 3 ngày; không thì không được chuyển bước rollout hoặc giảm tỉ lệ xem lại.

### 3.4. Chủ trì `chi_so.md` & QA E2 (CP5)
- Bổ sung 2 chỉ số tự đề xuất vào `report/team/chi_so.md`:
  - **Chỉ số dùng tự đề xuất:** *Tỉ lệ độ sâu sử dụng trợ lý (% yêu cầu nhóm can thiệp có mở gợi ý)* — đo bằng `agent_suggestion_shown` / `refund_request_created` (`arm == 'treatment'`).
  - **Chỉ số an toàn tự đề xuất:** *Tỉ lệ hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm)* — đo bằng `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung`, tối thiểu `100 đơn/tuần`).
- Hoàn thiện phần kiểm tra chéo nối trực tiếp 2 chỉ số tự đề xuất vào danh sách 10 event có `trace_id`, đảm bảo toàn bộ 5 chỉ số đều đo được; rà E1 dùng đúng mẫu *"trong đợt chạy thử là…"*, không viết *"đã nâng"*; kiểm tra 3 dòng E2 khớp số với B1 (`6.787 đ`), B4 (`11.743 đ = 0,98×` / `12.415 đ = 1,03×`) và A4 (`+1.185 đ` / `+2.370 đ`) [simulated], mỗi dòng 1 vai trò phụ trách.

## 4. Bằng chứng

- Kết quả chạy `src/lab13.py` trên máy TV3 (`.venv` Python 3.12): in `Ba phép thử đáp án biết trước: ĐẠT` và toàn bộ các bảng A2–E1.
- `report/team/bang_chi_phi.md` (QA phần A và phần B).
- `report/team/bang_loi.md` (2 bộ nhãn độc lập `20/20 = 100%`, quy tắc phân biệt và bảng khắc phục 5 ca).
- `report/team/pilot_plan.yaml` (3 luật dừng 4 vế, pass `yaml.safe_load`, không còn dấu `?` ngoài comment).
- `report/team/chi_so.md` (đủ 5 chỉ số E1, kiểm tra chéo event có `trace_id`, QA E2).
- `TEAM.md` và `TIMELINE.md` (cập nhật vai trò, đóng góp và bằng chứng của TV3).

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI (Antigravity) để kiểm tra chéo công thức trong `src/lab13.py`, rà soát điều kiện QA theo `TIMELINE.md`/`CHECKPOINTS.md`/`RUBRIC.md`, chuẩn hoá nhãn `simulated`, kiểm tra syntax YAML và rà các quy tắc 4 vế của luật dừng.
- Cách tự kiểm tra: tự tạo `.venv` trên máy TV3 và chạy `src/lab13.py` từ A1 đến E1; viết script Python đọc trực tiếp `logix_runs.csv` và `logix_requests.csv` để đối chiếu số thô; tự đọc và phân loại 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`; chạy `yaml.safe_load` kiểm tra `report/team/pilot_plan.yaml`; quét toàn bộ `report/team/*` để đảm bảo không có từ cấm, không còn dấu `?` ngoài comment YAML và không ghi `"cả đội"` làm người phụ trách.

## 6. Tự đánh giá

- Đã hoàn thành toàn bộ phần việc của TV3 từ Chặng 0 đến Chặng 5 và các bước kiểm chứng kỹ thuật Chặng 7 theo `TIMELINE.md`, đồng thời đối chiếu đáp án toàn bộ phần A–E đạt sai số `≤ 2%`.
- Sẵn sàng phối hợp cùng TV4 khoá Mục 4, 5, 6 + Đề xuất cuối trong `report/team/ho_so_launch_v0.md` trước 17:00 và cùng nhóm thực hiện chấm chéo nhóm `n + 1` vào `report/team/phieu_cham.md` ở Chặng 6.
