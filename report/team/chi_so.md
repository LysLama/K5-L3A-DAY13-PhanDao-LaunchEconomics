# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%; tỉ lệ bỏ qua trong đợt chạy thử là 27,12%; tỉ lệ mở lại trong đợt chạy thử là 4,25% (`src/lab13.py`, mục E1).

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

TV1 liệt kê. Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu hoàn phí |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| staff_review_decision | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| staff_rework_completed | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ cái |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển việc cho nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi mở lại yêu cầu |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Khi kiểm mẫu hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính (đóng trong 24 giờ và không mở lại trong 7 ngày): `ticket_closed.closed_at` so với `refund_request_created`, và không có `ticket_reopened` trong 7 ngày. Cả hai event có `trace_id`, nên đo được.
- Chỉ số dùng (tỉ lệ bỏ qua gợi ý): `staff_review_decision` với quyet_dinh `sua` hoặc `bo`, chia số event `agent_suggestion_shown`. Đo được.
- Chỉ số an toàn (mở lại trong 7 ngày): số `ticket_reopened` trong 7 ngày chia số `refund_request_created`. Đo được.
- Hai chỉ số nhóm tự đề xuất ở bảng E1 do TV3 đặt tên. Khi đã có tên, nối tiếp vào danh sách event trên; nếu không gắn được event có `trace_id` thì chỉ số đó chưa đo được.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công lên 6.787 đ (B1) [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% = 48/982 trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) (B4) [simulated] | % yêu cầu được xem lại còn > 50% ở cuối bước rollout 0.25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yc/tháng, +2.370 đ/việc nếu còn một nửa (A4) [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
