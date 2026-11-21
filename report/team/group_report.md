# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: PhanDao
- Lớp: L3A
- Thành viên: xem [TEAM.md](../../TEAM.md) (`Phạm Trung Kiên - 2A202603479`, `Nguyễn Đắc Tuấn Nghĩa - 2A202603442`, `Phạm Thanh Tùng - 2A202603446`, `Lý Thanh Lâm - 2A202603475`)

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để trình hội đồng Gate 2a dựa trên mẫu dữ liệu giả lập `1.200` yêu cầu (`1.624` lần chạy của agent trong 2 tuần tại 6 depot), nhằm trả lời 4 câu hỏi cốt lõi:
1. **Có đáng chạy không?** Tính chi phí thật cho mỗi việc thành công từ trace (gồm cả giờ nhân viên xem lại, làm lại và chi phí cố định), đối chiếu với chi phí nhân viên tự làm `12.000 đ/yêu cầu` (6 phút).
2. **Nhân viên có dùng không?** Đặc tả hệ thống chỉ số (chính, dùng, an toàn) và danh sách event gắn `trace_id` để đo lường thực tế trong pilot.
3. **Khi hỏng thì sao?** Phân loại độc lập 20 ca lỗi theo 5 nhóm nguyên nhân gốc của Google PAIR và thiết lập cơ chế phát hiện đo được kèm 1 vai trò phụ trách cho từng nhóm lỗi.
4. **Pilot thiết kế thế nào để ra quyết định?** Tính cỡ mẫu theo cụm có hiệu chỉnh `ICC = 0,02`, chọn thiết kế đối chứng ngẫu nhiên phân tầng theo depot và đặt các luật dừng 4 vế (`NẾU – TRONG – THÌ – KHÔNG THÌ`).

## 3. Giải pháp

Tóm tắt cách nhóm thực hiện từng nhiệm vụ A–E và liên kết tới file hồ sơ tương ứng:
- **Nhiệm vụ A (Mô hình chi phí — [src/lab13.py](../../src/lab13.py), [bang_chi_phi.md](bang_chi_phi.md)):** Kiểm chứng 3 phép thử lý thuyết A1 (`p = 0,8`), sau đó viết hàm `mo_hinh` cộng toàn bộ chi phí token (`26 đ/1k in`, `130 đ/1k out`) và tool (`15 đ/lần`) của mọi lần chạy (kể cả lần lỗi) ở tử số, cộng thời gian nhân viên xem lại và làm lại (`2.000 đ/phút`, nhãn `simulated`), chia cho số yêu cầu có `ket_qua == 'thanh_cong'` ở mẫu số. Tách chi phí theo 4 loại yêu cầu (A3) và phân bổ chi phí cố định `40 triệu đ/tháng` cho phạm vi pilot `noi_dia + hang_nang` (A4).
- **Nhiệm vụ B (Bảng độ nhạy — [src/lab13.py](../../src/lab13.py), [bang_chi_phi.md](bang_chi_phi.md)):** Chạy 9 kịch bản đơn biến (B1), kịch bản tổ hợp tuyến tính `token ×2 + xem lại ×2` (B2), bài toán tối ưu chi phí cả hệ thống theo giới hạn `1, 2, 3` lần chạy (B3) và kịch bản kiểm chứng tuần đầu xem lại 100% trong phạm vi `noi_dia + hang_nang` (B4).
- **Nhiệm vụ C (Bảng lỗi & khắc phục — [bang_loi.md](bang_loi.md)):** Hai người gắn nhãn (TV3 và TV4) phân loại độc lập 20 ca lỗi theo nguyên nhân gốc (*Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm*), tính tỉ lệ đồng thuận, chốt quy tắc phân biệt và ghép bảng khắc phục 5 ca đại diện (mỗi ca có event/ngưỡng phát hiện đo được và 1 vai trò phụ trách).
- **Nhiệm vụ D (Kế hoạch pilot — [src/lab13.py](../../src/lab13.py), [pilot_plan.yaml](pilot_plan.yaml)):** Tính cỡ mẫu hai tỉ lệ (`baseline = 0,70`, `alpha = 0,05`, `power = 0,80`, `ICC = 0,02`) cho 5 câu D1 a–e; đối chiếu 5 câu hỏi tách tác động D2; chọn chia theo nhân viên (`20 + 20` cụm, `MDE = 0,06`, `m ≥ 299` yêu cầu/người, `DE = 6,96`) và thiết lập luật dừng dựa trên baseline mở lại thực tế (`4,25%` toàn mẫu, `3,97%` trong phạm vi).
- **Nhiệm vụ E (Chỉ số, rủi ro & Hồ sơ v0 — [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md), [phieu_cham.md](phieu_cham.md)):** Tính thử 3 chỉ số E1 trên 1.200 yêu cầu, thiết kế 10 event có `trace_id` kèm kiểm tra chéo, lập bảng rủi ro kinh tế E2 từ kết quả độ nhạy và tổng hợp thành 1 trang hồ sơ Gate 2a.

## 4. Kết quả

- **A1–A4 (Chi phí & Phạm vi):** Ba phép thử A1 đạt `1,20 · 1,25 · 1,25` (`ĐẠT`). Trên toàn mẫu, chi phí mỗi việc thành công là **4.472 đ** [simulated] (`978` việc thành công / `4.373.585 đ` tổng chi phí), gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (`274,7 đ/yêu cầu`). Giờ nhân viên chiếm **92,5%** tổng chi phí (làm lại `51,8%`, xem lại `40,7%` [simulated]). Khi cộng `222` ca không thành công × `12.000 đ`, chi phí cả hệ thống là **5.865 đ/yêu cầu = 0,49×** [simulated]. Tách theo loại (A3): `noi_dia` `2.696 đ` (`0,22×`, `95,0%` thành công), `hang_nang` `8.221 đ` (`0,69×`, `74,1%`), `doi_tac` `10.215 đ` (`0,85×`, `54,4%`), riêng `quoc_te` lên tới **22.515 đ = 1,88×** (`27,3%` thành công, tỉ lệ `ok` theo attempt tụt `30,0% → 11,4% → 2,2%`) nên bị loại khỏi phạm vi pilot. Trong phạm vi `noi_dia + hang_nang` (`3.414 đ/việc`), khi cộng chi phí cố định `40 triệu đ/tháng` thì đạt **4.599 đ = 0,38×** ở đủ tải (`33.750` việc/tháng) và **5.784 đ = 0,48×** ở nửa tải [simulated].
- **B1–B4 (Độ nhạy):** Ba yếu tố làm tăng chi phí mạnh nhất là: **1. Số ca làm lại** (`+51,8%` → `6.787 đ`), **2. Tỉ lệ xem lại** (`+40,7%` → `6.292 đ`), **3. Lương nhân viên +25%** (`+23,1%` → `5.506 đ`), trong khi giá token gấp đôi chỉ làm tăng `+5,6%` (`4.723 đ`) [simulated]. Ở B3, giới hạn rẻ nhất cho cả hệ thống là **tối đa 2 lần chạy** (`6.901.220 đ`), khác với mức tối ưu cục bộ chi phí/việc thành công ở 1 lần chạy (`4.111 đ` nhưng đẩy `319` ca sang nhân viên). Ở B4 (bằng chứng bất lợi), nếu tuần đầu phải xem lại 100% trong phạm vi `noi_dia + hang_nang`, chi phí vọt lên **11.743 đ = 0,98×** (với 9 phút làm lại) hoặc **12.415 đ = 1,03×** (với trung bình `15,3 phút` làm lại từ dữ liệu) [simulated]; hoà vốn khi thời gian xem lại `≤ 5,1 phút` (hoặc `≤ 4,8 phút`).
- **D1–D2 (Cỡ mẫu & Thiết kế pilot):** Để phát hiện mức chênh `+5 điểm` (`0,70 → 0,75`), chia theo yêu cầu cần `1.251` yêu cầu/nhóm; chia theo nhân viên (`m = 75`, `DE = 2,48`) cần `3.103` yêu cầu/nhóm (`42` người/nhóm, tổng `84 > 40` người); với `20` nhân viên/nhóm, cỡ mẫu hiệu dụng tối đa bị chặn ở `20 / 0,02 = 1.000 < 1.251`; với `6` depot/nhóm, trần chỉ đạt `300`. Nhóm chọn chia theo nhân viên `20 + 20` ở **MDE = 6 điểm** (`n_e = 859`/nhóm, cần `m ≥ 299` yêu cầu/người, `DE = 6,96`) và nêu rõ đánh đổi: nếu tác động thật chỉ là `+5 điểm`, lực thống kê (power) giảm còn **0,6417 (~0,64)**.
- **E1–E3 (Chỉ số, Rủi ro & Đề xuất):** Trong đợt chạy thử (chưa có đối chứng), chỉ số chính đạt `82,83%` (`994/1.200`), tỉ lệ bỏ qua gợi ý `27,12%` (`48/177`), tỉ lệ mở lại trong 7 ngày `4,25%` (`51/1.200`; riêng phạm vi pilot là `3,97%`). Nhóm thiết kế 10 event có `trace_id`, 3 dòng rủi ro kinh tế (làm lại ×2, xem lại 100% kéo dài, hụt nửa khối lượng) và định hướng đề xuất **Go có điều kiện** cho phạm vi `noi_dia + hang_nang`. *(Kết quả chấm chéo Gate 2a sẽ được cập nhật ngay sau phiên hội đồng 17:00–17:45).*

## 5. Khó khăn và cách xử lý

- **Cạm bẫy đọc dữ liệu CSV:** Cột `quyet_dinh_xem_lai` có ô trống cho các yêu cầu không xem lại; nhóm thống nhất dùng `pd.read_csv(..., keep_default_na=False)` ngay từ đầu để tránh bị biến thành `NaN`.
- **Tương thích phiên bản Python trên các máy:** Máy TV1 chạy Python 3.15.0a3 bị lỗi C-extension của NumPy (`unknown slot ID 85`), đã xử lý bằng cách chuyển sang môi trường `.venv` Python 3.12 và kiểm chứng độc lập trên máy thứ 2 (Python 3.12 / 3.14).
- **Giới hạn 40 nhân viên trong bài toán cỡ mẫu cụm (D1):** Trần hiệu dụng `c / ICC = 1.000` không thể đạt `1.251` của MDE 5 điểm. Nhóm giải bất phương trình tìm `m ≥ 299` ở MDE 6 điểm (`n = 859`) và tính chính xác power thực tế (`0,6417`) bằng `statsmodels.stats.power.NormalIndPower` để báo cáo minh bạch với hội đồng.

## 6. Tổng hợp đóng góp

Chi tiết vai trò, phần việc và bằng chứng commit/file của cả 4 thành viên (`TV1: Phạm Trung Kiên`, `TV2: Nguyễn Đắc Tuấn Nghĩa`, `TV3: Phạm Thanh Tùng`, `TV4: Lý Thanh Lâm`) được ghi đầy đủ trong [TEAM.md](../../TEAM.md) và 4 file báo cáo cá nhân `report/team/<MSSV>_<HoTen>.md`.

## 7. Hạn chế và hướng cải thiện

- **Phụ thuộc vào số phút giả lập (`_simulated`):** Hai yếu tố nhạy nhất (làm lại `51,8%` và xem lại `40,7%`) hiện dựa trên cột `_simulated`. Ngay trong tuần 1 của pilot, nhóm phải đo thời gian thật qua hai event `staff_review_decision.phut_xem_lai` và `staff_rework_completed.phut_lam_lai` để hiệu chỉnh mô hình chi phí.
- **Lực thống kê ở mức chênh 5 điểm còn thấp (`power = 0,64`):** Do số lượng nhân viên cố định ở 40 người (`20 + 20` cụm), khả năng bỏ sót tác động thật 5 điểm là `36%`. Có thể cải thiện bằng cách dùng phân tích hiệp phương sai (ANCOVA) kiểm soát tỉ lệ baseline của từng nhân viên trước pilot để giảm phương sai giữa các cụm.

## 8. Tài liệu tham khảo

1. Erol và cộng sự (2025), *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359).
2. Google PAIR, *People + AI Guidebook — Errors + Graceful Failure*, [pair.withgoogle.com](https://pair.withgoogle.com).
3. Tài liệu đề bài và hướng dẫn Lab 13: [docs/du_lieu_va_cong_thuc.md](../../docs/du_lieu_va_cong_thuc.md), [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
4. Thư viện `statsmodels` (`NormalIndPower`, `proportion_effectsize`).
