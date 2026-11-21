# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: PhanDao · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ toàn mẫu (gấp 16,3× hoá đơn 274,7 đ/yc; làm lại 51,8% tổng); phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 4.599 đ [simulated] | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2 +51,8% · Xem lại ×2 +40,7% · Lương +25% +23,1% (token ×2 chỉ +5,6%); xem lại 100% đẩy lên 0,98×–1,03× [simulated] | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Phạm vi pilot 0,38× của 12.000 đ (0,48× ở nửa khối lượng); toàn hệ thống 0,49×; quoc_te 1,88× → loại khỏi phạm vi [simulated] | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử (chưa có đối chứng): chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200; phạm vi pilot 3,97%); thêm 2 chỉ số tự đề xuất (độ sâu dùng, kiểm mẫu sai tiền) và 10 event có `trace_id` | Xong, có bằng chứng | Người gắn nhãn 1 |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi phân 5 loại Google PAIR đạt đồng thuận 20/20 = 100% (≥ 80%), khớp 20/20; bảng khắc phục 5 ca (Ca 9, 7, 18, 4, 17) đủ event/ngưỡng đo được và 1 vai trò phụ trách/dòng | Xong, có bằng chứng | Người gắn nhãn 2, kiêm giữ hồ sơ |
| 6 · Pilot plan | Chia ngẫu nhiên 20 + 20 nhân viên phân tầng depot; rollout 0,10 → 0,25 → 0,50; MDE 0,06 (n=859/nhóm, m≥299, DE=6,96; bất lợi: power 0,64 nếu chênh 5 điểm); 3 luật dừng 4 vế; quyết định 2027-01-05 | Xong, có bằng chứng | Người viết code |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ (+51,8%); xem lại 100% → 0,98×–1,03×; nửa khối lượng → cố định +2.370 đ/việc [simulated] | Giả lập | Người kiểm số |

**Đề xuất: Go có điều kiện** — Mở pilot cho phạm vi `noi_dia + hang_nang` (loại `quoc_te` 1,88× và `doi_tac` 0,85×). **Con số bất lợi đã tính:** tuần đầu xem lại 100% đẩy chi phí lên `11.743–12.415 đ` (`0,98×–1,03×`) [simulated]; trần 40 nhân viên làm `power = 0,64` ở mức +5 điểm; tỉ lệ mở lại nền `4,25%` (`3,97%` phạm vi). Điều kiện bắt buộc:

- Sửa khoá chống trùng (`idempotency_key`) và đối soát sổ cái tự động hàng giờ (Ca 7, 20) — **Phụ trách:** Kỹ sư trưởng agent · **Ngày kiểm tra:** `2026-11-30`.
- Ký chấp nhận đánh đổi `MDE = 6 điểm` (`power = 0,64` ở +5 điểm) và ngưỡng dừng an toàn so với đối chứng (`+2 điểm`, trần `6%`) — **Phụ trách:** Giám đốc vận hành LogiX-VN · **Ngày kiểm tra:** `2026-11-30`.
- Bật đủ 10 event có `trace_id` (gồm `audit_sample_checked` 100 đơn/tuần) và thay phút `_simulated` bằng phút đo thật sau tuần 1 — **Phụ trách:** Kỹ sư trưởng agent · **Ngày kiểm tra:** `2026-12-08`.
- Áp dụng lộ trình giảm tỉ lệ xem lại theo bậc (mở khi sửa + bỏ `< 15%`) và giữ thời gian xem lại `≤ 5,1 phút/lần` — **Phụ trách:** Trưởng nhóm CSKH · **Ngày kiểm tra:** `2026-12-15`.
