# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

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
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
