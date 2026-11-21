"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: ba hàm dưới đây. k=None nghĩa là chạy lại đến khi đúng.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: mo_hinh. CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    hoa_don = tien_token.sum() + tien_tool.sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=hoa_don / len(reqs),
                n_yeu_cau=len(reqs), khong_thanh_cong=len(reqs) - thanh_cong)


def _in_kq(ten, cps, goc):
    print(f'{ten:28s} {cps:10,.0f} {(cps / goc - 1) * 100:+7.1f}%')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    # ----- A2 -----
    ket_qua = mo_hinh(runs, reqs)
    print('\n== A2 · Mô hình chi phí từ trace ==')
    nhan = {
        'token': 'đo từ trace',
        'tool': 'đo từ trace',
        'chay_lai': 'đo từ trace (attempt > 1)',
        'xem_lai': 'simulated',
        'lam_lai': 'simulated',
        'tong': 'có phần simulated',
        'thanh_cong': '',
        'cps': 'simulated',
        'hoa_don_moi_yc': 'đo từ trace',
    }
    for ten, gia_tri in ket_qua.items():
        if ten in ('n_yeu_cau', 'khong_thanh_cong'):
            continue
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:16s} {gia_tri:14,.1f}  {nhan[ten]}')
        elif ten == 'thanh_cong':
            print(f'{ten:16s} {gia_tri:14,.0f}')
        else:
            print(f'{ten:16s} {gia_tri:14,.0f}  {nhan[ten]}')
    gap = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    print(f'cps / hoa_don_moi_yc = {gap:.1f} lần')
    for khoan in ('lam_lai', 'xem_lai', 'token', 'tool'):
        print(f'  {khoan:10s} {ket_qua[khoan] / ket_qua["tong"] * 100:5.1f}% tổng')
    gio_nv = (ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong'] * 100
    print(f'  giờ nhân viên {gio_nv:.1f}% tổng')
    ca_he_thong = (ket_qua['tong'] + ket_qua['khong_thanh_cong'] * BASELINE) / ket_qua['n_yeu_cau']
    print(f'chi phí cả hệ thống / yêu cầu = {ca_he_thong:,.0f} đ '
          f'= {ca_he_thong / BASELINE:.2f}× của {BASELINE:,} đ  [simulated]')
    print(f'  (cộng {ket_qua["khong_thanh_cong"]} yêu cầu không thành công × {BASELINE:,} đ)')

    # ----- A3 -----
    print('\n== A3 · Tách theo loại yêu cầu ==')
    print(f'{"loai":12s} {"n":>6s} {"thanh_cong":>8s} {"ty_le":>8s} {"lan/yc":>8s} {"cps":>10s} {"so_voi_12k":>10s}')
    for loai in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        lan = len(runs[runs['request_id'].isin(sub['request_id'])]) / len(sub)
        print(f'{loai:12s} {len(sub):6d} {kq["thanh_cong"]:8d} {kq["thanh_cong"] / len(sub):8.1%} '
              f'{lan:8.2f} {kq["cps"]:10,.0f} {kq["cps"] / BASELINE:10.2f}×')
    hop = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    hop['ok'] = (hop['status'] == 'ok').astype(float)
    ti_le_ok = hop.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    print('Tỉ lệ status=ok theo attempt (chạy lại có giúp không):')
    print(ti_le_ok.reindex(['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']).to_string(float_format=lambda x: f'{x:.1%}'))

    # ----- A4 -----
    print('\n== A4 · Chi phí cố định (noi_dia + hang_nang) ==')
    CO_DINH_THANG = 40_000_000
    LUONG_THANG = 45_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    viec_thang = LUONG_THANG * kq_pv['thanh_cong'] / len(reqs)
    co_dinh = CO_DINH_THANG / viec_thang
    cps_pv = kq_pv['cps']
    print(f'phạm vi n={kq_pv["n_yeu_cau"]}  thanh_cong={kq_pv["thanh_cong"]}  '
          f'tong={kq_pv["tong"]:,.0f}  cps={cps_pv:,.0f}  [simulated]')
    print(f'việc thành công/tháng (đủ tải) = {LUONG_THANG:,} × {kq_pv["thanh_cong"]}/{len(reqs)} = {viec_thang:,.0f}')
    print(f'cố định/việc = {CO_DINH_THANG:,} / {viec_thang:,.0f} = {co_dinh:,.0f} đ')
    print(f'cps + cố định (đủ tải) = {cps_pv + co_dinh:,.0f} đ = {(cps_pv + co_dinh) / BASELINE:.2f}×  [simulated]')
    print(f'cps + cố định (một nửa tải) = {cps_pv + 2 * co_dinh:,.0f} đ = {(cps_pv + 2 * co_dinh) / BASELINE:.2f}×  [simulated]')

    # ----- B1 -----
    print('\n== B1 · Đổi từng yếu tố ==')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    print(f'{"Gốc (A2)":28s} {goc:10,.0f}')
    for ten, kw in kich_ban.items():
        _in_kq(ten, mo_hinh(runs, reqs, **kw)['cps'], goc)

    # ----- B2 -----
    print('\n== B2 · Đổi một cặp ==')
    cps_b2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    _in_kq('Token ×2 và xem lại ×2', cps_b2, goc)
    xep = sorted(
        ((ten, mo_hinh(runs, reqs, **kw)['cps']) for ten, kw in kich_ban.items()
         if 'giảm' not in ten and 'Tối đa' not in ten and 'Chỉ 1' not in ten),
        key=lambda x: abs(x[1] / goc - 1), reverse=True)
    print('Ba yếu tố tăng chi phí mạnh nhất:')
    for i, (ten, cps) in enumerate(xep[:3], 1):
        print(f'  {i}. {ten}: {cps:,.0f} đ ({(cps / goc - 1) * 100:+.1f}%)')

    # ----- B3 -----
    print('\n== B3 · Giới hạn chạy lại, chi phí cả hệ thống ==')
    print(f'{"gioi_han":10s} {"tong_tro_ly":>14s} {"khong_tc":>8s} {"ca_he_thong":>14s} {"cps":>10s}')
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        he_thong = kq['tong'] + kq['khong_thanh_cong'] * BASELINE
        print(f'{k:10d} {kq["tong"]:14,.0f} {kq["khong_thanh_cong"]:8d} {he_thong:14,.0f} {kq["cps"]:10,.0f}')

    # ----- B4 -----
    print('\n== B4 · Xem lại 100% (noi_dia + hang_nang) ==')
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    n_co_ok = pham_vi['request_id'].isin(set(runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'])).sum()
    n_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    n_tc = int((pham_vi['ket_qua'] == 'thanh_cong').sum())
    trace = (runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA
             + runs_pv['tool_calls'] * GIA_TOOL).sum()
    tb_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    print(f'yêu cầu có ≥1 lần ok: {n_co_ok} × 5 phút')
    print(f'ca lam_lai trong phạm vi: {n_lam_lai}')
    print(f'token+tool phạm vi: {trace:,.0f} đ')
    print(f'phút làm lại simulated, mọi ca lam_lai: n={len(tb_lam_lai)} '
          f'trung bình={tb_lam_lai.mean():.1f} trung vị={tb_lam_lai.median():.1f}  [simulated]')

    def _b4(phut_lam_lai, phut_xem=5):
        xem = n_co_ok * phut_xem * LUONG_PHUT
        lam = n_lam_lai * phut_lam_lai * LUONG_PHUT
        tong = trace + xem + lam
        return tong, tong / n_tc

    for phut in (9, round(float(tb_lam_lai.mean()), 1)):
        tong, cps = _b4(phut)
        print(f'làm lại {phut} phút/ca → tổng {tong:,.0f} đ → cps {cps:,.0f} đ '
              f'= {cps / BASELINE:.2f}×  [simulated]')
        du = BASELINE * n_tc - trace - n_lam_lai * phut * LUONG_PHUT
        hoa_von = du / (n_co_ok * LUONG_PHUT)
        print(f'  hoà vốn với 12.000 đ khi mỗi lần xem lại ≤ {hoa_von:.1f} phút')

    # Tỉ lệ mở lại hiện tại: TV1 ghi vào chú thích pilot_plan.yaml trước khi TV3 đặt luật an toàn.
    # Code cỡ mẫu D1 và ba chỉ số E1 để TV2 viết ở TODO CP4.
    print('\n== Tỉ lệ mo_lai_trong_7_ngay hiện tại (cho luật an toàn) ==')
    mo = reqs['mo_lai_trong_7_ngay'].astype(int)
    mo_pv = pham_vi['mo_lai_trong_7_ngay'].astype(int)
    print(f'toàn mẫu = {mo.mean():.2%} ({int(mo.sum())}/{len(reqs)})')
    print(f'noi_dia + hang_nang = {mo_pv.mean():.2%} ({int(mo_pv.sum())}/{len(pham_vi)})')

    # TODO CP4 · Nhiệm vụ D (TV2 viết code D1 và E1 vào đây).
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
    print('\n== Chờ TV2 · TODO CP4 (D1) và E1 ==')
    print('TV1 xong A1–A4 và B1–B4. Chưa viết cỡ mẫu D1 hay ba chỉ số E1.')
