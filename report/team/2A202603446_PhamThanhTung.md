# Báo cáo cá nhân — PhamThanhTung-2A202603446

File này là bản của TV3. File mẫu `MSSV_HoTen.md` giữ nguyên.

## 1. Thông tin thành viên

- Họ tên: Phạm Thanh Tùng
- MSSV: 2A202603446
- Email: 26ai.tungpt@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1 & QA / Spec (TV3)

## 2. Phần việc phụ trách

- Theo dõi điều kiện "Xong khi" trong `CHECKPOINTS.md` và tiêu chí chấm trong `RUBRIC.md` từ đầu buổi.
- **Chặng 1 (CP1 · Nhiệm vụ A — đã hoàn thành):**
  - Bước 1.1: Kiểm tra gate A1 (chỉ cho qua Bước 1.2 khi `src/lab13.py` in `ĐẠT` đủ 3 phép thử `1,20 · 1,25 · 1,25`).
  - Bước 1.2: Kiểm tra 2 lỗi hay gặp trong `mo_hinh` (tử số cộng mọi lần chạy kể cả lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`, đọc CSV với `keep_default_na=False`) và kiểm tra gắn nhãn `simulated`.
  - Bước 1.3: Rà soát câu trả lời A3 (`quoc_te` không đáng chạy và chạy lại 3 lần có giúp không, kèm dẫn chứng từ 2 cột giữa) và câu trả lời A4 trong `report/team/bang_chi_phi.md`.
  - Bước 1.4: Đối chiếu toàn bộ số A1–A4 với slide đáp án (sai số `≤ 2%`).
- **Chặng 2–8 (đang tiếp tục theo `TIMELINE.md`):** rà B3/B4; gắn độc lập 20 ca lỗi & bảng 5 ca ở CP3; soạn D2 và 3 luật dừng 4 vế ở CP4; chủ trì `chi_so.md` ở CP5; chấm chéo nhóm `n+1` ở Chặng 6; rà QA cuối buổi ở Chặng 7.

## 3. Đóng góp cụ thể

- Thiết lập `.venv` Python 3.12.10 trong `src/` trên máy thứ 2 của nhóm và chạy trực tiếp `src/lab13.py`:
  - Gate A1 in `Ba phép thử đáp án biết trước: ĐẠT` (`1,20 · 1,25 · 1,25`).
  - Đối chiếu số liệu gốc từ `logix_runs.csv` (1.624 lần chạy, 5.600 tool calls, chi phí lần chạy lại `attempt > 1` = 93.804 đ) và `logix_requests.csv` (1.200 yêu cầu: 978 `thanh_cong`, 148 `chuyen_nhan_vien`, 74 `lam_lai`; 890 phút xem lại và 1.132 phút làm lại simulated).
- Kiểm tra `mo_hinh` trong `src/lab13.py`: xác nhận đọc CSV có `keep_default_na=False`, tử số cộng toàn bộ token/tool của cả 1.624 lần chạy (chia 1.000 token trước khi nhân đơn giá), mẫu số chia đúng `978` việc thành công.
- Rà soát và bổ sung QA cho phần A của `report/team/bang_chi_phi.md`:
  - Gắn nhãn `[simulated]` ở tiêu đề cột chi phí giả lập của bảng A3, A4 và dòng ngưỡng hoà vốn A4 (~4.660 việc thành công/tháng).
  - Bổ sung số chi phí cả hệ thống khi cộng 222 ca không thành công × 12.000 đ = **5.865 đ/yêu cầu = 0,49×** [simulated] tại A2 để đồng bộ với Mục 3 trong `report/team/ho_so_launch_v0.md`.
  - Xác nhận câu trả lời A3 nêu đủ `quoc_te` không đáng chạy (`22.515 đ/việc = 1,88×`), dẫn chứng đủ 2 cột giữa (`27,3%` thành công và `2,32` lần chạy/yêu cầu), tỉ lệ `ok` theo attempt tụt `30,0% → 11,4% → 2,2%`, đồng thời nêu `doi_tac` (`10.215 đ = 0,85×`, `54,4%`, `1,88` lần/yc) sát ngưỡng nên thu hẹp pilot về `noi_dia + hang_nang` (`3.414 đ/việc`, cộng cố định `4.599 đ = 0,38×` ở đủ tải và `5.784 đ = 0,48×` ở nửa tải [simulated]).
- Đối chiếu toàn bộ số A1–A4 với slide chữa Nhiệm vụ A (slide 66) và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: toàn bộ con số trùng khớp (sai số 0%, đạt yêu cầu `≤ 2%`).

## 4. Bằng chứng

- Kết quả chạy `src/lab13.py` trên máy TV3 (`.venv` Python 3.12): in `Ba phép thử đáp án biết trước: ĐẠT` cùng các bảng A2, A3, A4.
- `report/team/bang_chi_phi.md` (phần A1–A4: đủ bảng, nhãn `simulated`, câu trả lời ≤ 3 dòng có số).
- `report/team/ho_so_launch_v0.md` (Mục 1 và Mục 3 đã điền đúng trạng thái `Giả lập`, nhãn `[simulated]`, phụ trách 1 vai trò `Người kiểm số`).
- `TEAM.md` và `TIMELINE.md` (đã cập nhật thông tin vai trò TV3 và phần đóng góp Chặng 1).

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI (Antigravity) để kiểm tra chéo công thức trong `src/lab13.py`, rà soát điều kiện QA theo `TIMELINE.md`/`CHECKPOINTS.md`/`RUBRIC.md` và chuẩn hoá nhãn `simulated` trong `report/team/bang_chi_phi.md`.
- Cách tự kiểm tra: tự tạo `.venv` trên máy TV3, chạy trực tiếp `src/lab13.py`, viết lệnh Python đọc thẳng `logix_runs.csv` và `logix_requests.csv` để kiểm tra lại tổng từng khoản, đối chiếu từng ô bảng A1–A4 với slide 66 trong `docs/Ngay13_Slide_Launch_Economics.pdf` và quét từ khoá cấm trên toàn bộ `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần việc của TV3 ở Chặng 0 (thiết lập vai trò) và Chặng 1 (CP1 · Nhiệm vụ A, 20 điểm theo `RUBRIC.md`).
- Sẵn sàng phối hợp cùng nhóm thực hiện tiếp Chặng 2 (rà B3/B4 và chuẩn bị đọc 20 ca lỗi cho CP3).
