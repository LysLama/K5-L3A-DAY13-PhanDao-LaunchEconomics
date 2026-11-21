# Báo cáo cá nhân — Phạm Trung Kiên-2A202603479

File này là bản của TV1. File mẫu `MSSV_HoTen.md` giữ nguyên.

## 1. Thông tin thành viên

- Họ tên: Phạm Trung Kiên
- MSSV: 2A202603479
- Email: 26ai.kienpt@vinuni.edu.vn
- Vai trong nhóm: Người viết code giai đoạn 1 (TV1)

## 2. Phần việc phụ trách

- Viết và chạy `src/lab13.py` cho nhiệm vụ A (A1–A4) và nhiệm vụ B (B1–B4).
- Kiểm tay câu D1.e và power khi tác động thật là 5 điểm.
- Điền `report/team/pilot_plan.yaml`, trừ 3 luật dừng.
- Liệt kê event và viết kiểm tra chéo trong `report/team/chi_so.md`.
- Đề xuất cách phát hiện và khắc phục cho lỗi Hệ thống và Giới hạn hệ thống, để TV4 ghép sau khi có nhãn thống nhất.

## 3. Đóng góp cụ thể

`python lab13.py` (Python 3.12, thư mục `src/`) in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25). Các số dưới đây lấy từ stdout của lần chạy đó. Số phút `_simulated` mang nhãn simulated.

A2: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ). Làm lại chiếm 51,8% tổng, xem lại 40,7%. Chi phí cả hệ thống (4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/yêu cầu = 0,49× [simulated].

A3: `quoc_te` 22.515 đ = 1,88×, thành công 27,3%. Tỉ lệ `ok` của quốc tế giảm theo lần chạy: 30,0% → 11,4% → 2,2%, nên chạy lại tới 3 lần không giúp. `doi_tac` 0,85×, sát ngưỡng.

A4, phạm vi `noi_dia` + `hang_nang`: 3.414 đ + cố định 1.185 đ = 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng. Một nửa khối lượng thì cố định thành 2.370 đ/việc, tổng 5.784 đ = 0,48× [simulated]. Cố định không đổi kết luận ở đủ tải, nhưng nặng hơn khi khối lượng nhỏ.

B1 tự kiểm tuyến tính: giảm một nửa đúng bằng nửa mức tăng của gấp đôi (token 5,6% và 2,8%; xem lại 40,7% và 20,3%). B2: token ×2 cùng xem lại ×2 = 6.543 đ (+46,3%). Ba yếu tố mạnh nhất: làm lại, xem lại, lương. B3: cả hệ thống rẻ nhất ở giới hạn 2 lần (6.901.220 đ), còn chi phí mỗi việc thành công thấp nhất ở 1 lần (4.111 đ). B4: xem lại 100% với 9 phút làm lại = 11.743 đ = 0,98×; với 15,3 phút làm lại (trung bình simulated, 74 ca) thương số đúng là 12.414,79 đ = 1,03×. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút hoặc ≤ 4,8 phút.

D1.e tính tay: `co_mau(0,70; 0,76) = 859`. Giải `20m / (1+(m−1)×0,02) ≥ 859` được m ≥ 298,5, lấy 299. DE = 6,96. `NormalIndPower` với chênh 5 điểm và n = 859 cho power 0,6417.

Đề xuất sẵn cho bảng khắc phục, chưa ghi vào `bang_loi.md` vì chưa có hai bộ nhãn độc lập:

| Loại | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --- | --- | --- | --- |
| Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi sổ cái ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| Giới hạn hệ thống | Event `handoff_to_staff` với reason = `thieu_du_lieu`, theo loại yêu cầu | Giữ cách chuyển kèm tóm tắt; đưa `quoc_te` ra khỏi pilot | PM trợ lý hoàn phí |

Bản nháp nói 1 phút, chốt lại khi TV4 khóa đề xuất trong hồ sơ: chi phí 4.472 đ [simulated], gấp 16,3 lần hoá đơn, cả hệ thống bằng 0,49× nhân viên tự làm; quốc tế 1,88× nên loại. Nhạy nhất là làm lại, xem lại, lương. Xem lại 100% còn 0,98× đến 1,03×. Pilot 20 + 20 nhân viên, MDE 6 điểm vì 40 người không đủ mẫu ở 5 điểm; nếu tác động thật chỉ 5 điểm thì power 0,64. Đề xuất dự kiến là Go có điều kiện, và phải nói thẳng power 0,64 cùng mức xem lại 100%.

## 4. Bằng chứng

- `src/lab13.py` chạy hết A1–B4, dừng ở dòng chờ TV2 (`TODO CP4`).
- `report/team/pilot_plan.yaml` đã điền; `yaml.safe_load` đọc được. Ba dòng `stop_rules` còn dấu `?`.
- `report/team/chi_so.md`: 10 event, mỗi event có `trace_id`, và mục kiểm tra chéo.
- Máy này dùng Python 3.12. Python 3.15.0a3 cài được thư viện nhưng NumPy báo `unknown slot ID 85`, không chạy bài.

## 5. Công cụ AI đã dùng

Cursor (Grok) để viết hàm theo công thức trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và `docs/du_lieu_va_cong_thuc.md`. Số trong hồ sơ không lấy từ câu trả lời của AI: A1–B4 in từ `src/lab13.py`, câu D1.e giải từ công thức cỡ mẫu rồi đối chiếu `NormalDist` (1.251 và 859) và `statsmodels` (power 0,6417).

## 6. Tự đánh giá

Phần code A–B và các trường YAML TV1 phụ trách đã chạy và khớp số đối chiếu trong hướng dẫn, sai số dưới 2%. Đã rà bảng A và B: số khớp stdout, câu trả lời không quá 3 dòng, cột chi phí có nhãn `[simulated]`. D1 của TV2 in ra 1.251 · 3.103 · 1.000 · 300 · m ≥ 299, DE 6,96, power 0,6417, khớp chú thích `pilot_plan.yaml`. E1 in 82,83% · 27,12% · 4,25%, khớp `chi_so.md`. Ba dòng E2 khớp B1 (6.787 đ, +51,8%), B4 (11.743 đ = 0,98× và 12.415 đ = 1,03×) và A4 (1.185 đ, 2.370 đ), mỗi dòng một vai trò. Các việc dưới đây dừng vì cần người khác viết tiếp:

- TV3 viết 3 luật dừng trong `pilot_plan.yaml` và hai chỉ số tự đề xuất trong `chi_so.md`.
- TV3 gắn nhãn độc lập 20 ca. TV4 đã có bộ nhãn của mình và bản ghép 5 ca, nhưng `bang_loi.md` vẫn để trống để chờ so nhãn. Chưa ghi vào file đó.
- TV4 khóa Mục 4, 5, 6 và đề xuất trong `ho_so_launch_v0.md`. Bản nói 1 phút ở mục 3 chỉ chốt sau đề xuất đó.
