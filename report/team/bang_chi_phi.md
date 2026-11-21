# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (= 1 + 0,2) · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (= 1 / 0,8) · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (= 1,24 / 0,992) · ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công 4.472 đ gấp **16,3 lần** hoá đơn chia số yêu cầu (274,7 đ) [simulated]; tính cả 222 ca không thành công × 12.000 đ, chi phí cả hệ thống là **5.865 đ/yêu cầu = 0,49×** [simulated].
- Lớn nhất là **làm lại: 51,8%** tổng, rồi xem lại 40,7%; giờ nhân viên chiếm 92,5%, token 5,6%, tool 1,9% [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

- `quoc_te` không đáng chạy: 22.515 đ/việc = 1,88× của 12.000 đ, chỉ 27,3% thành công [simulated]; `doi_tac` (10.215 đ = 0,85×, 54,4% thành công, 1,88 lần/yc) sát ngưỡng và có điều khoản riêng nên thu hẹp pilot về `noi_dia + hang_nang`.
- Chạy lại không giúp cho `quoc_te`: trung bình 2,32 lần/yêu cầu nhưng tỉ lệ `ok` theo từng attempt tụt mạnh 30,0% → 11,4% → 2,2%, càng chạy lại càng tốn chi phí mà hầu như không cứu được ca nào.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 | 5.784 | 0,48× |

- Không đổi kết luận: cả hai mức vẫn dưới 12.000 đ (0,38× và 0,48×, chi phí biến đổi trong phạm vi 3.414 đ/việc) [simulated].
- Cố định tăng gấp đôi khi khối lượng giảm một nửa; chỉ hoà vốn khi còn khoảng 4.660 việc thành công/tháng (~6.200 yêu cầu/tháng) [simulated], nên hồ sơ phải ghi rõ số đã cộng cố định ở khối lượng nào.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ mỗi việc thành công [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

Kiểm tra tuyến tính: mức giảm khi "giảm một nửa" bằng nửa mức tăng khi "gấp đôi" (−2,8% / +5,6%; −20,3% / +40,7%; −25,9% / +51,8%). Mọi dòng là simulated.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ, +46,3% (= 5,6% + 40,7%, cộng thẳng vì mô hình tuyến tính) [simulated].
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%); giá token chỉ +5,6% [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + số yêu cầu không thành công × 12.000 đ.

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- Rẻ nhất cho công ty là **tối đa 2 lần**: 6.901.220 đ, thấp hơn 3 lần 136.365 đ và 1 lần 548.561 đ [simulated].
- Không trùng: chi phí mỗi việc thành công thấp nhất lại ở **1 lần** (4.111 đ), vì 319 ca bị đẩy sang nhân viên không nằm trong chỉ số này.

## B4 · Nếu phải xem lại tất cả

- Xem lại 100% (`noi_dia` + `hang_nang`, 948 ca × 5 phút, 48 ca làm lại × 9 phút): 11.743 đ = **0,98×** của 12.000 đ; dùng 15,3 phút làm lại như dữ liệu thì 12.415 đ = **1,03×** [simulated].
- Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (≤ 4,8 phút nếu làm lại 15,3 phút) [simulated].
- Pilot phải đo được tỉ lệ xem lại giảm an toàn xuống bao nhiêu và thời gian mỗi lần xem lại có dưới 5 phút không; xem lại 100% thì trợ lý không tiết kiệm được.
