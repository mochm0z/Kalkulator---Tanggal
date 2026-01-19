import streamlit as st
from datetime import date

# Konfigurasi Halaman
st.set_page_config(page_title="Kalkulator Tanggal", page_icon="📅")

st.title("📅 Kalkulator Selisih Tanggal")
st.write("Hitung jarak hari, bulan, dan tahun dengan mudah.")

# Kamus Nama Bulan
bulan_opsi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
bulan_ke_angka = {b: i+1 for i, b in enumerate(bulan_opsi)}

# Layout Kolom
col1, col2 = st.columns(2)

with col1:
    st.subheader("Tanggal Awal")
    tgl1 = st.number_input("Tanggal", min_value=1, max_value=31, value=19, key="t1")
    bln1_nama = st.selectbox("Bulan", bulan_opsi, index=0, key="b1")
    thn1 = st.number_input("Tahun", min_value=1900, max_value=2100, value=2026, key="th1")

with col2:
    st.subheader("Tanggal Target")
    tgl2 = st.number_input("Tanggal", min_value=1, max_value=31, value=25, key="t2")
    bln2_nama = st.selectbox("Bulan", bulan_opsi, index=5, key="b2")
    thn2 = st.number_input("Tahun", min_value=1900, max_value=2100, value=2035, key="th2")

if st.button("Hitung Selisih Sekarang"):
    try:
        d1 = date(int(thn1), bulan_ke_angka[bln1_nama], int(tgl1))
        d2 = date(int(thn2), bulan_ke_angka[bln2_nama], int(tgl2))

        # Logika Hitung
        awal, akhir = (d1, d2) if d1 < d2 else (d2, d1)
        total_hari = (akhir - awal).days
        
        y = akhir.year - awal.year
        m = akhir.month - awal.month
        d = akhir.day - awal.day

        if d < 0:
            m -= 1
            d += 30
        if m < 0:
            y -= 1
            m += 12

        # Tampilkan Hasil
        st.success(f"### Hasil Analisis:")
        st.write(f"**Total Selisih:** {total_hari} Hari")
        st.info(f"**Rincian Kalender:** {y} Tahun, {m} Bulan, {d} Hari")
        
        nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        st.write(f"Tanggal target jatuh pada hari: **{nama_hari[d2.weekday()]}**")

    except ValueError:
        st.error("Tanggal yang Anda masukkan tidak valid (misal: 31 Februari).")

st.markdown("---")
st.caption("Dibuat dengan Python & Streamlit")