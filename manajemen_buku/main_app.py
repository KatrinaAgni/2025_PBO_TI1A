# main_app.py
import streamlit as st
import pandas as pd
from database import fetch_query, execute_query
from model import BukuFisik, BukuDigital
from manager import KoleksiBuku
from konfigurasi import DAFTAR_GENRE

st.set_page_config(page_title="Manajemen Koleksi Buku", layout="wide")
st.title("📚 Aplikasi Manajemen Koleksi Buku")

koleksi = KoleksiBuku()

# ------------------------------
# Fungsi halaman input
# ------------------------------
def halaman_tambah_buku():
    st.subheader("➕ Tambah Buku Baru")
    with st.form("form_tambah", clear_on_submit=True):
        judul = st.text_input("Judul Buku")
        penulis = st.text_input("Penulis")
        tahun = st.number_input("Tahun Terbit", min_value=0, step=1, format="%d")
        genre = st.selectbox("Genre", DAFTAR_GENRE)
        jml_halaman = st.number_input("Jumlah Halaman", min_value=0, step=1)
        tipe = st.selectbox("Tipe Buku", ["Fisik", "Digital"])
        submitted = st.form_submit_button("Simpan")
        
        if submitted:
            if tipe == "Fisik":
                buku = BukuFisik(judul, penulis, tahun, genre, jml_halaman)
            else:
                buku = BukuDigital(judul, penulis, tahun, genre, jml_halaman)
            
            if koleksi.tambah_buku(buku):
                st.success("📘 Buku berhasil disimpan!")
                st.rerun()
            else:
                st.error("❌ Gagal menyimpan buku.")

# ------------------------------
# Fungsi halaman daftar buku
# ------------------------------
def halaman_daftar_buku():
    st.subheader("📖 Daftar Koleksi Buku")
    daftar_buku = koleksi.semua_buku()
    if not daftar_buku:
        st.warning("⚠️ Belum ada data buku.")
    else:
        # Fitur pencarian
        keyword = st.text_input("🔍 Cari Buku (judul atau penulis)").lower()

        data = []
        for b in daftar_buku:
            if keyword in b.judul.lower() or keyword in b.penulis.lower():
                data.append({
                    "ID": b.id,
                    "Info": b.cetak_info(),
                    "Penulis": b.penulis,
                    "Tahun": b.tahun,
                    "Genre": b.genre,
                    "Jumlah Halaman": b.halaman,
                    "Tipe": type(b).__name__
                })

        if data:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("❕ Tidak ditemukan buku yang cocok dengan pencarian.")

        with st.expander("🗑️ Hapus Buku"):
            id_hapus = st.number_input("Masukkan ID Buku yang ingin dihapus", min_value=1, step=1)
            if st.button("Hapus Buku"):
                berhasil = koleksi.hapus_buku(id_hapus)
                if berhasil:
                    st.success("✅ Buku berhasil dihapus.")
                    st.rerun()
                else:
                    st.warning("⚠️ ID tidak ditemukan, tapi data mungkin sudah dihapus sebelumnya. Silakan refresh.")

# ------------------------------
# Fungsi halaman ringkasan
# ------------------------------
def halaman_ringkasan():
    st.subheader("📊 Ringkasan Koleksi Buku")
    daftar_buku = koleksi.semua_buku()
    if not daftar_buku:
        st.info("ℹ️ Tidak ada data buku.")
        return

    df = pd.DataFrame([b.__dict__ for b in daftar_buku])

    col1, col2 = st.columns(2)
    col1.metric("Total Buku", len(df))
    col2.metric("Total Halaman", df['halaman'].sum())

    st.divider()
    st.markdown("#### 📚 Grafik Jumlah Buku per Genre")
    df_genre = df['genre'].value_counts().reset_index()
    df_genre.columns = ['Genre', 'Jumlah']
    st.bar_chart(df_genre.set_index('Genre'))

# ------------------------------
# Sidebar navigasi
# ------------------------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/29/29302.png", width=100)
st.sidebar.title("Navigasi Menu")
menu = st.sidebar.radio("Pilih Halaman:", ["Tambah Buku", "Daftar Buku", "Ringkasan"])

if menu == "Tambah Buku":
    halaman_tambah_buku()
elif menu == "Daftar Buku":
    halaman_daftar_buku()
elif menu == "Ringkasan":
    halaman_ringkasan()
