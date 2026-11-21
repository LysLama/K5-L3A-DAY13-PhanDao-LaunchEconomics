# Báo cáo cá nhân — Nguyễn Đắc Tuấn Nghĩa-2A202603442

File này là bản của TV2. File mẫu `MSSV_HoTen.md` giữ nguyên.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đắc Tuấn Nghĩa
- MSSV: 2A202603442
- Email: 26ai.nghiandt@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số (CP1–CP2), sau giờ giải lao nhận vai Người viết code (CP3–CP5) (TV2)

## 2. Phần việc phụ trách

- Cài môi trường máy thứ 2 (`src/.venv`, Python 3.14) và chạy lại `src/lab13.py` độc lập với máy TV1.
- Tính tay đối chiếu A1, A2 và điền toàn bộ `report/team/bang_chi_phi.md` (A1–A4, B1–B4).
- Viết code D1 (cỡ mẫu a–e, power) và E1 (ba chỉ số) trong `src/lab13.py`.
- Điền số E1 và bảng rủi ro kinh tế E2 trong `report/team/chi_so.md`.
- Kiểm tra `report/team/pilot_plan.yaml` bằng `yaml.safe_load` và quét dấu `?` ngoài comment.
- Đề xuất cách phát hiện và khắc phục cho lỗi Ngầm và Do người dùng; trả lời phản biện ở Gate 2a.

## 3. Đóng góp cụ thể

Kiểm số độc lập: viết đoạn tính riêng bằng pandas, không gọi `mo_hinh`, và ra cùng số với TV1: 5.771,712 nghìn token vào và 734,774 nghìn token ra → 245.585 đ; 5.600 lần gọi tool → 84.000 đ; 890 phút xem lại → 1.780.000 đ và 1.132 phút làm lại → 2.264.000 đ [simulated]; 978 việc thành công trên 1.624 lần chạy. A1 tính tay: 1 + 0,2 = 1,20; 1 / 0,8 = 1,25; (1 + 0,2 + 0,04) / (1 − 0,2³) = 1,24 / 0,992 = 1,25.

Bảng chi phí: chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn 274,7 đ/yêu cầu; làm lại 51,8% tổng [simulated]. Thêm mức hoà vốn A4: 40.000.000 / (12.000 − 3.414) ≈ 4.660 việc thành công/tháng, tức khoảng 6.200 yêu cầu/tháng. B3: rẻ nhất cho công ty ở giới hạn 2 lần (6.901.220 đ), thấp hơn 3 lần 136.365 đ.

D1 (stdout `lab13.py`): a) 1.251 yêu cầu/nhóm; b) DE 2,48, n 3.103, 42 người/nhóm, tổng 84 > 40; c) trần 1.000 < 1.251; d) trần 300; e) 859/nhóm, m ≥ 299, DE 6,96; power 0,6417 nếu tác động thật chỉ +5 điểm. Câu m được tìm bằng vòng lặp, không giải tay, rồi đối chiếu với lời giải tay của TV1 (298,5 → 299).

E1 trong đợt chạy thử: chỉ số chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200).

E2: ba dòng rủi ro lấy số từ B1 (làm lại ×2 → 6.787 đ), B4 (0,98×–1,03×) và A4 (+1.185 đ / +2.370 đ mỗi việc), mỗi dòng một vai trò phụ trách. Tỉ lệ làm lại trong phạm vi là 4,9% (48/982).

Đề xuất cho bảng khắc phục, chưa ghi vào `bang_loi.md` vì TV3 và TV4 gắn nhãn độc lập; TV4 ghép sau khi có nhãn thống nhất:

| Loại | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --- | --- | --- | --- |
| Ngầm | Event `audit_sample_checked`: kiểm mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch tiền. Thêm cảnh báo khi chi phí token/yêu cầu theo tuần tăng > 50% | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |
| Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |

Chuẩn bị trả lời phản biện ở Gate 2a (1 phút):

- Xem lại 100% tuần đầu: 11.743 đ = 0,98×, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút; vì vậy pilot giảm xem lại theo bậc và hoà vốn khi mỗi lần xem lại ≤ 5,1 phút.
- Vì sao 20 + 20 nhân viên: chia theo depot chỉ có 6 cụm (trần 300); theo nhân viên có đủ 20 cụm mỗi nhóm, MDE 6 điểm với m ≥ 299.
- Power 0,64 ở mức 5 điểm: đánh đổi đã ghi trong `pilot_plan.yaml`, cần Giám đốc vận hành ký chấp nhận.
- Baseline mở lại 4,25% (3,97% trong phạm vi): ngưỡng tuyệt đối 3% sẽ dừng nhầm tuần 1, nên so với đối chứng (+2 điểm) kèm trần 6%.

## 4. Bằng chứng

- Commit `563a57c`: thông tin nhóm trong `TEAM.md`, khung `ho_so_launch_v0.md`.
- Commit `0ccf501`: A1–A4 trong `bang_chi_phi.md`, Mục 1 và 3 hồ sơ.
- Commit `c2d2c36`: B1–B4 trong `bang_chi_phi.md`, Mục 2 hồ sơ.
- `src/lab13.py`: hàm `co_mau`, khối D1 và E1.
- `report/team/chi_so.md`: số E1 và bảng E2.
- Máy thứ 2 (Linux, Python 3.14): `python lab13.py` chạy hết A1 → E1; `yaml.safe_load` đọc được `pilot_plan.yaml`; `git diff --stat` không có thay đổi ở `lab13_starter.py`, hai file CSV và `MSSV_HoTen.md`.

## 5. Công cụ AI đã dùng

Claude Code để đọc tài liệu, điền bảng markdown từ stdout và viết khối D1/E1. Tự kiểm tra: chạy đoạn pandas độc lập để đối chiếu A1–A2; đối chiếu D1 và E1 với số trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (1.251, 3.103, 859, 299, 6,96, 0,6417; 82,83%, 27,12%, 4,25%), đều khớp; số B4 lệch 1 đ so với tài liệu (12.415 so với 12.414) do làm tròn, dưới 2%.

## 6. Tự đánh giá

Phần kiểm số A–B, code D1/E1 và E2 đã xong, khớp đáp án trong sai số 2%. Còn chờ người khác:

- TV3 viết 3 luật dừng trong `pilot_plan.yaml` (hiện còn dấu `?`) và hai chỉ số tự đề xuất trong `chi_so.md`.
- TV4 ghép hai dòng khắc phục ở mục 3 vào `bang_loi.md` sau khi có nhãn thống nhất, và điền Mục 4–6 hồ sơ.
- Chạy lại kiểm tra cuối (YAML không còn `?`, không có từ cấm) sau khi TV3 điền luật dừng.
