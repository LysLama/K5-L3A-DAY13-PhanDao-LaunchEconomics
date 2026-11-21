# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Thanh Tùng (TV3) · Người gắn nhãn 2: Lý Thanh Lâm (TV4) (gắn độc lập trong 8 phút, không trao đổi trước khi so)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (đạt ngưỡng ≥ 80%; khớp 20/20 với bảng phân loại Google PAIR).

## Quy tắc phân biệt cho các ca không trùng

Không có ca lệch giữa hai bộ nhãn độc lập (0/20 ca không trùng). Ghi chú nguyên tắc phân biệt đã rà thống nhất cho các ca dễ nhầm:

- Ca 6, 9 là **Do người dùng** (không phải Hệ thống): gốc lỗi do khách chọn sai mục hoặc nhập sai định dạng mã; việc trợ lý chưa gợi ý định dạng là giải pháp khắc phục.
- Ca 13 là **Giới hạn hệ thống** (không phải Hệ thống): yêu cầu bảo hiểm đối tác nằm ngoài phạm vi trợ lý, kể cả khi câu trả lời chung chung chưa khéo.
- Ca 8, 15 là **Hệ thống** (không phải Ngầm): sai sót đã lộ ra ngay cho nhân viên/khách nhìn thấy trước hoặc lúc gửi; **Ngầm** chỉ dùng cho lỗi không ai nhận ra cho tới khi kiểm mẫu/chi phí (ca 5, 12, 17).
- Ca 18 là **Ngữ cảnh** (không phải Hệ thống): số tiền `30.000 đ × 50% = 15.000 đ` đúng chính sách, chỉ thiếu diễn giải công thức trong ngữ cảnh tin nhắn khiến khách tưởng thiếu.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo theo ngày khi vượt `> 2%` tổng số yêu cầu | Nhận diện định dạng mã sàn TMĐT để tự tra sang mã vận đơn LogiX; không tra được thì hỏi lại kèm hướng dẫn và ảnh mẫu | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa thông báo "đã hoàn" và event `refund_ledger_write` có `ket_qua == 'ok'` cùng `trace_id`; ngưỡng `> 0 ca` lệch | Chỉ báo "đã hoàn" khi sổ cái trả `ok`; nếu lỗi 503 sau 3 lần thử thì báo "đang xử lý" và bắn `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ event `ticket_reopened` có `reason = thac_mac_so_tien` mà đối chiếu sổ cái tính đúng chính sách, thống kê theo tuần; ngưỡng `> 1%` | Cập nhật mẫu tin nhắn hoàn phí luôn hiển thị rõ công thức: `30.000 đ × 50% (trễ 24–48h) = 15.000 đ` | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu`, theo dõi tỉ lệ theo từng loại yêu cầu mỗi ngày; cảnh báo nếu `> 10%` trong `noi_dia + hang_nang` | Giữ cơ chế chuyển thẳng cho nhân viên kèm bản tóm tắt thông tin đã thu thập; loại loại `quoc_te` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked`: kiểm mẫu ngẫu nhiên `100 đơn/tuần` so với bảng giá hiện hành; ngưỡng `> 1%` đơn lệch tiền (kèm cảnh báo khi token/yêu cầu theo tuần tăng `> 50%`) | Tự động xoá bộ nhớ đệm khi phát hành bảng giá mới, ghi `pricing_version` vào mọi `trace_id` và hoàn bù cho các đơn bị lệch | Kế toán trưởng |
