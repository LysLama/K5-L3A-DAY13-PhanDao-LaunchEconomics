# Báo cáo cá nhân — LyThanhLam-2A202603475

File này là bản của TV4. File mẫu `MSSV_HoTen.md` giữ nguyên.

## 1. Thông tin thành viên

- Họ tên: Lý Thanh Lâm
- MSSV: 2A202603475
- Email: 26ai.lamlt@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2, kiêm giữ hồ sơ / Leader (TV4)

## 2. Phần việc phụ trách

Theo bảng phân công trong `TIMELINE.md` và `TEAM.md`:
- **Chặng 0 (Khởi động):** Thiết lập repo nhóm `K5-L3A-DAY13-PhanDao-LaunchEconomics`, điền thông tin nhóm và phân vai 4 thành viên trong `TEAM.md` & `TIMELINE.md`; khởi tạo khung 7 mục và gán sẵn vai trò phụ trách (1 vai trò/mục, không ghi `"cả đội"`) trong `report/team/ho_so_launch_v0.md`.
- **Chặng 1 & Chặng 2 (CP1–CP2 · Nhiệm vụ A & B):** Phối hợp rà câu trả lời giải thích A2–A4, B1–B4 trong `report/team/bang_chi_phi.md` (đảm bảo `≤ 3 dòng/câu`, có số và gắn nhãn `simulated`); cập nhật **Mục 1** (Chi phí mỗi việc thành công), **Mục 2** (Ba yếu tố nhạy nhất), **Mục 3** (So với nhân viên tự làm) và **Mục 7** (Rủi ro kinh tế) vào `report/team/ho_so_launch_v0.md` ở trạng thái `Giả lập`.
- **Chặng 3 (CP3 · Nhiệm vụ C):** Đóng vai **Người gắn nhãn 2**, đọc độc lập 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và gắn nhãn theo nguyên nhân gốc (5 loại Google PAIR: *Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm*) mà không trao đổi trước với TV3; thiết kế phương án phát hiện & khắc phục cho ca lỗi **Ngữ cảnh** (ca 18) và chuẩn bị ghép cùng 4 dòng khắc phục của TV1 (Hệ thống, Giới hạn hệ thống) và TV2 (Ngầm, Do người dùng) vào `report/team/bang_loi.md` ngay khi so nhãn với TV3.
- **Chặng 4 & Chặng 5 (CP4–CP5 · Nhiệm vụ D & E):** Soạn giải trình **đánh đổi cỡ mẫu** cho kế hoạch pilot (`20 + 20` nhân viên ở MDE 6 điểm, chấp nhận `power = 0,64` ở mức 5 điểm); tổng hợp `report/team/group_report.md` và chuẩn bị sẵn nội dung chốt Mục 4, 5, 6 cùng Đề xuất `Go có điều kiện` cho `report/team/ho_so_launch_v0.md`.

## 3. Đóng góp cụ thể

### 3.1. Quản lý Hồ sơ Launch v0 (CP1–CP2 & E2)
- Khởi tạo và cập nhật chính xác 4 mục có yếu tố giả lập trong `report/team/ho_so_launch_v0.md` (trạng thái `Giả lập`, nhãn `[simulated]`):
  - **Mục 1 (Chi phí mỗi việc thành công):** `4.472 đ` toàn mẫu (gấp `16,3×` hoá đơn `274,7 đ/yc`; làm lại chiếm `51,8%` tổng); phạm vi `noi_dia + hang_nang` là `3.414 đ`, cộng chi phí cố định `40 triệu đ/tháng` ở đủ tải (`33.750` việc/tháng) là `4.599 đ` [simulated].
  - **Mục 2 (Ba yếu tố nhạy nhất):** 1. Số ca làm lại `×2` (`+51,8%` → `6.787 đ`) · 2. Tỉ lệ xem lại `×2` (`+40,7%` → `6.292 đ`) · 3. Lương nhân viên `+25%` (`+23,1%` → `5.506 đ`), trong khi giá token `×2` chỉ `+5,6%`; nếu tuần đầu xem lại 100% thì chi phí tăng lên `11.743 đ = 0,98×` (với 9 phút làm lại) đến `12.415 đ = 1,03×` (với 15,3 phút làm lại) [simulated].
  - **Mục 3 (So với nhân viên tự làm 12.000 đ):** Phạm vi pilot `0,38×` ở đủ tải (`0,48×` ở nửa tải `5.784 đ`); cả hệ thống toàn mẫu `5.865 đ/yc = 0,49×`; riêng `quoc_te` `22.515 đ = 1,88×` (`27,3%` thành công, tỉ lệ `ok` theo attempt giảm `30,0% → 11,4% → 2,2%`) nên loại khỏi phạm vi pilot [simulated].
  - **Mục 7 (Rủi ro kinh tế):** Tổng hợp 3 kịch bản bất lợi từ B1 (làm lại `×2` → `6.787 đ`), B4 (xem lại 100% → `0,98×–1,03×`) và A4 (nửa khối lượng → cố định `+2.370 đ/việc`) [simulated].

### 3.2. Bộ nhãn độc lập 20 ca lỗi của Người gắn nhãn 2 (CP3)
Đọc độc lập 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và phân loại theo **nguyên nhân gốc** (chưa ghi vào `report/team/bang_loi.md` cho tới khi TV3 hoàn thành bộ nhãn độc lập của Người gắn nhãn 1 để đảm bảo quy tắc không trao đổi trước khi so nhãn):

| Ca | Tóm tắt nguyên nhân gốc | Nhãn độc lập của Người gắn nhãn 2 (TV4) |
| --: | --- | --- |
| 1 | Khách nhập số tài khoản thiếu 2 chữ số → ngân hàng trả lỗi | Do người dùng |
| 2 | Kiện 28 kg nhưng agent gọi tool với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ | Hệ thống |
| 3 | Thiết kế hoàn về ví LogiX trong 5 phút nhưng khách chờ ở tài khoản ngân hàng | Ngữ cảnh |
| 4 | Chặng do hãng nước ngoài giao, LogiX không có dữ liệu, agent chuyển nhân viên | Giới hạn hệ thống |
| 5 | Kiểm mẫu cuối tuần mới phát hiện 14 đơn có mã giảm giá bị hoàn theo giá trước giảm (thừa 12.000 đ/đơn) | Ngầm |
| 6 | Khách chọn nhầm mục "Hoàn phí giao trễ" trong khi mô tả hàng bị vỡ | Do người dùng |
| 7 | API sổ cái lỗi 503 cả 3 lần nhưng agent vẫn báo khách "đã hoàn tiền thành công" | Hệ thống |
| 8 | Agent trích dẫn "Điều 7.2" không tồn tại trong chính sách hiện hành (lỗi hiển thị lộ ra, dù tiền đúng) | Hệ thống |
| 9 | Khách nhập mã đơn sàn TMĐT thay vì mã vận đơn LogiX | Do người dùng |
| 10 | Từ chối hoàn do bão đúng điều khoản bất khả kháng, nhưng app vẫn hiện banner "cam kết giao 24 giờ" | Ngữ cảnh |
| 11 | Khách gửi tin nhắn thoại 40 giây, agent chỉ xử lý được văn bản | Giới hạn hệ thống |
| 12 | Tool của depot D05 thiếu 1 trường khiến agent gọi lặp lại, tốn gấp 3 lần token suốt 3 tuần không ai biết | Ngầm |
| 13 | Khách hỏi bảo hiểm hàng hoá của đối tác (ngoài phạm vi trợ lý), dù agent trả lời chung chung chưa khéo | Giới hạn hệ thống |
| 14 | Khách bấm nhầm nút "Xác nhận đã nhận tiền" khi chưa nhận khiến yêu cầu bị đóng | Do người dùng |
| 15 | Đơn trễ 26 giờ (chính sách hoàn 50%) nhưng agent tính hoàn 100%, nhân viên xem lại bắt được | Hệ thống |
| 16 | Thiết kế "gửi ngay khi xong" khiến Zalo gửi thông báo lúc 2:14 sáng làm phiền khách | Ngữ cảnh |
| 17 | Bảng giá đổi từ 01/11 nhưng cache vẫn giữ bản cũ cho đơn < 2 kg, lệch 1.000–2.000 đ trên 212 đơn không ai mở lại | Ngầm |
| 18 | Tính đúng 30.000 đ × 50% = 15.000 đ nhưng tin nhắn không ghi cách tính khiến khách tưởng thiếu và mở lại | Ngữ cảnh |
| 19 | Đơn từ 14 tháng trước vượt quá giới hạn truy cập dữ liệu 12 tháng của hệ thống | Giới hạn hệ thống |
| 20 | Khách gửi lại sau 10 phút, lệnh thứ hai thiếu khoá chống trùng (`idempotency_key`) nên hoàn tiền 2 lần | Hệ thống |

- **Tổng hợp theo loại (Người gắn nhãn 2):** Do người dùng (4 ca: `1, 6, 9, 14`) · Hệ thống (5 ca: `2, 7, 8, 15, 20`) · Ngữ cảnh (4 ca: `3, 10, 16, 18`) · Giới hạn hệ thống (4 ca: `4, 11, 13, 19`) · Ngầm (3 ca: `5, 12, 17`).

### 3.3. Đề xuất khắc phục lỗi Ngữ cảnh & Bản ghép 5 ca (CP3)
Thiết kế dòng khắc phục cho lỗi **Ngữ cảnh** (ca 18) và chuẩn bị bảng ghép 5 ca đại diện đủ 5 loại (kết hợp với đề xuất của TV1 ở `2A202603479_PhamTrungKien.md` và TV2 ở `2A202603442_NguyenDacTuanNghia.md`) để điền vào `report/team/bang_loi.md` ngay khi đối chiếu nhãn với TV3:

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi vượt `2%` số yêu cầu/ngày | Nhận diện định dạng mã sàn TMĐT để tự tra sang mã vận đơn; nếu không tra được thì hiện hướng dẫn kèm ảnh mẫu | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa tin nhắn báo "đã hoàn" và event `refund_ledger_write` có `ket_qua == 'ok'` cùng `trace_id`; ngưỡng `0 ca` lệch | Chỉ gửi thông báo "đã hoàn" khi sổ cái trả `ok`; nếu lỗi 503 sau 3 lần thử thì báo "đang xử lý" và bắn `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ event `ticket_reopened` có `reason = thac_mac_so_tien` mà đối chiếu sổ cái thấy tính đúng chính sách, thống kê theo tuần (ngưỡng `> 1%`) | Cập nhật mẫu tin nhắn hoàn phí luôn hiển thị rõ công thức và mức phần trăm: `30.000 đ × 50% (trễ 24–48h) = 15.000 đ` | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu`, theo dõi tỉ lệ theo từng loại yêu cầu mỗi ngày | Giữ cơ chế chuyển thẳng cho nhân viên kèm bản tóm tắt thông tin đã thu thập; loại `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked`: kiểm mẫu ngẫu nhiên `100 đơn/tuần` đối chiếu bảng giá hiện hành; ngưỡng `> 1%` đơn lệch tiền | Tự động xoá cache bảng giá khi phát hành bảng giá mới và ghi `pricing_version` vào mọi `trace_id` | Kế toán trưởng |

### 3.4. Giải trình đánh đổi cỡ mẫu D1 & Chốt Hồ sơ Launch v0 (CP4–CP5)
- **Giải trình đánh đổi cỡ mẫu (đã đồng bộ vào `report/team/pilot_plan.yaml`):** Với 40 nhân viên CSKH chia đều `20` can thiệp + `20` đối chứng và `ICC = 0,02`, cỡ mẫu hiệu dụng tối đa bị chặn bởi trần `c / ICC = 20 / 0,02 = 1.000 < 1.251`, nên không thể đạt `power = 0,80` ở mức chênh `MDE = 5 điểm`. Nhóm chọn thiết kế `20 + 20` nhân viên ở **MDE = 6 điểm** (`n_e = 859` yêu cầu hiệu dụng/nhóm → mỗi nhân viên xử lý `m ≥ 299` yêu cầu, `DE = 6,96`), và ghi nhận rõ con số bất lợi: nếu tác động thật chỉ là `+5 điểm` thì `power = 0,6417 (~0,64)`.
- **Hoàn thiện Mục 4, 5, 6 và Đề xuất cuối trong `report/team/ho_so_launch_v0.md` (đã ghép hoàn chỉnh sau khi TV3 hoàn tất 3 luật dừng, 2 chỉ số tự đề xuất và đối chiếu `bang_loi.md`):**
  - *Mục 4 (Chỉ số chính, dùng, an toàn):* Đợt chạy thử (chưa có đối chứng): chính `82,83%` (`994/1.200`), bỏ qua gợi ý `27,12%` (`48/177`), mở lại 7 ngày `4,25%` (`51/1.200`; phạm vi pilot `3,97%`); kèm 2 chỉ số tự đề xuất và 10 event có `trace_id` (`Xong, có bằng chứng` · `Người gắn nhãn 1`).
  - *Mục 5 (Bảng lỗi & khắc phục):* 20 ca phân theo 5 loại Google PAIR đạt đồng thuận `20/20 = 100%` cùng TV3 (`Nguyễn Thanh Tùng`), 5 ca đại diện đủ 5 loại có event/ngưỡng đo được và 1 vai trò phụ trách (`Xong, có bằng chứng` · `Người gắn nhãn 2, kiêm giữ hồ sơ`).
  - *Mục 6 (Pilot plan):* Chia ngẫu nhiên `20 + 20` nhân viên phân tầng cùng depot, rollout `0,10 → 0,25 → 0,50`, `MDE = 0,06` (`m ≥ 299`/người, `DE = 6,96`, `n = 859`/nhóm; bất lợi: `power = 0,64` ở mức `+5 điểm`), 3 luật dừng 4 vế, chốt ngày `2027-01-05` (`Xong, có bằng chứng` · `Người viết code`).
  - *Đề xuất đã chốt:* **Go có điều kiện** cho phạm vi `noi_dia + hang_nang` (loại `quoc_te` `1,88×` và `doi_tac` `0,85×`), nêu thẳng 3 con số bất lợi (`power = 0,64` ở MDE 5 điểm; xem lại 100% tốn `11.743–12.415 đ = 0,98×–1,03×` [simulated]; mở lại nền `4,25%` / `3,97%` phạm vi) kèm 4 điều kiện có 1 vai trò phụ trách và ngày kiểm tra cụ thể (`2026-11-30`, `2026-12-08`, `2026-12-15`).
- **Tổng hợp báo cáo nhóm:** Cập nhật đầy đủ 8 mục trong `report/team/group_report.md` dẫn lại toàn bộ số liệu chính từ A1–E3.

## 4. Bằng chứng

- `TEAM.md` và `TIMELINE.md`: cập nhật thông tin phân vai và chi tiết phần đóng góp của TV4 (`Lý Thanh Lâm - 2A202603475`).
- `report/team/ho_so_launch_v0.md`: hoàn thiện đủ 7 mục (Mục 1, 2, 3, 7 `Giả lập` có nhãn `[simulated]`; Mục 4, 5, 6 `Xong, có bằng chứng`), mỗi mục 1 vai trò phụ trách, chốt đề xuất `Go có điều kiện` gói gọn trong 1 trang.
- `report/team/bang_loi.md`: bộ nhãn độc lập 20 ca của Người gắn nhãn 2 đạt đồng thuận `20/20 = 100%` với TV3 (`Nguyễn Thanh Tùng`) và ca khắc phục lỗi Ngữ cảnh (`Ca 18`).
- `report/team/phieu_cham.md`: đánh giá hồ sơ nhóm `QuanHocOnline` (`QuanHocOnline_HoSo_Gate2a.zip`), chấm `30/30` theo 3 tiêu chí hội đồng Gate 2a kèm dẫn chứng số và câu hỏi phản biện.
- `report/team/group_report.md`: báo cáo tổng hợp nhóm 8 mục (dưới 2 trang, dẫn lại đầy đủ số chính từ CP1–CP5 và nhãn `simulated`).
- `report/team/2A202603475_LyThanhLam.md`: báo cáo cá nhân, bộ nhãn độc lập 20 ca của Người gắn nhãn 2 và bằng chứng đối chiếu.

## 5. Công cụ AI đã dùng

- Công cụ: Trợ lý AI (Antigravity / Gemini) để tra cứu cấu trúc tài liệu đề bài, kiểm tra chéo tính nhất quán số liệu giữa `src/lab13.py`, `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md` và rà soát 5 quy tắc vàng của Lab 13.
- Cách tự kiểm tra:
  - Chạy trực tiếp `src/lab13.py` để đối chiếu từng con số trong `ho_so_launch_v0.md` và `group_report.md` (sai số `0%` so với đáp án hướng dẫn).
  - Tự đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và đối chiếu từng ca với câu hỏi nhận diện nguyên nhân gốc của 5 loại Google PAIR.
  - Chạy lệnh kiểm tra `yaml.safe_load`, quét dấu `?` ngoài comment, quét từ khoá cấm theo quy tắc 5 của `README.md` trên toàn bộ `report/team/` và kiểm tra `git diff --stat` đảm bảo không chạm vào các file dữ liệu gốc (`logix_runs.csv`, `logix_requests.csv`, `lab13_starter.py`, `MSSV_HoTen.md`).

## 6. Tự đánh giá

- Đã hoàn thành toàn bộ phần việc của TV4 từ Chặng 0 đến Chặng 7 (tổng hợp đóng gói trước hạn nộp LMS):
  - Hoàn tất `TEAM.md`, `TIMELINE.md`, `report/team/ho_so_launch_v0.md` (đủ 7 mục + đề xuất `Go có điều kiện` 1 trang), `report/team/phieu_cham.md` (hoàn chỉnh chấm nhóm `QuanHocOnline` `30/30` kèm lý do số, câu hỏi phản biện và giải trình đối chiếu hồ sơ), `report/team/group_report.md`, `report/team/2A202603475_LyThanhLam.md` và hoàn tất đối chiếu `report/team/bang_loi.md` đạt đồng thuận `20/20 = 100%` cùng TV3 (`Nguyễn Thanh Tùng`).
  - Sẵn sàng để cả 4 thành viên nộp link repo `https://github.com/LysLama/K5-L3A-DAY13-PhanDao-LaunchEconomics` lên LMS trước `23:59 GMT+7`.
