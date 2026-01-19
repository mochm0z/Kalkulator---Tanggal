import streamlit as st
from datetime import date

# 1. Konfigurasi Halaman & Gaya Visual (CSS)
st.set_page_config(page_title="Hitung Mundur Momen Kita", page_icon="✨", layout="centered")

# CSS Kustom untuk membuat tampilan lebih estetik
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        border: none;
    }
    .hasil-box {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header yang Lebih Personal
st.title("⏳ Mari Hitung Waktunya")
st.markdown("""
Halo! Seringkali kita penasaran seberapa jauh sih jarak antara dua momen penting dalam hidup kita? 
Cukup pilih tanggalnya di bawah, dan biarkan aplikasi ini menghitung sisa perjalanannya untukmu. 😊
""")

# 3. Kamus Nama Bulan
bulan_opsi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
bulan_ke_angka = {b: i+1 for i, b in enumerate(bulan_opsi)}

# 4. Input dengan Bahasa yang Lebih Santai
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 📅 Titik Awal")
        tgl1 = st.number_input("Tanggal", 1, 31, 19)
        bln1_nama = st.selectbox("Bulan", bulan_opsi, index=0, key="b1")
        thn1 = st.number_input("Tahun", 1900, 2100, 2026)

    with col2:
        st.write("### 🚀 Titik Tujuan")
        tgl2 = st.number_input("Tanggal", 1, 31, 25, key="t2")
        bln2_nama = st.selectbox("Bulan", bulan_opsi, index=5, key="b2")
        thn2 = st.number_input("Tahun", 1900, 2100, 2035, key="th2")

st.write("") # Spasi

if st.button("Cek Selisih Waktunya ✨"):
    try:
        d1 = date(int(thn1), bulan_ke_angka[bln1_nama], int(tgl1))
        d2 = date(int(thn2), bulan_ke_angka[bln2_nama], int(tgl2))

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

        # 5. Output yang Informatif dan Hangat
        nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        hari_target = nama_hari[d2.weekday()]

        st.markdown(f"""
        <div class="hasil-box">
            <h2 style='color: #FF4B4B;'>Wah, Perjalanannya Cukup Jauh!</h2>
            <p style='font-size: 1.2em;'>Total waktu yang ditempuh adalah <strong>{total_hari:,} hari</strong>.</p>
            <hr>
            <p>Atau jika dirinci menjadi:</p>
            <h3>✨ {y} Tahun, {m} Bulan, dan {d} Hari ✨</h3>
            <p>Catat ya, tanggal tujuanmu itu jatuh pada hari <strong>{hari_target}</strong>.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if d2 > d1:
            st.balloons() # Efek balon jika ke masa depan

    except ValueError:
        st.error("Aduh, sepertinya tanggal yang kamu masukkan nggak ada di kalender (misal: 31 Februari). Coba cek lagi ya!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Dibuat dengan ❤️ untuk membantu merencanakan masa depanmu.</p>", unsafe_allow_html=True)
