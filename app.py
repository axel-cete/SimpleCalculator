import streamlit as st
from function.calculation import *


st.set_page_config(page_title="Import Calculator", layout="centered")

PASSWORD = "123456"  # simple on purpose

# -----------------------
# AUTH STATE INIT
# -----------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# -----------------------
# LOGIN GATE
# -----------------------
if not st.session_state.authenticated:
    st.title("Login")

    pwd = st.text_input("Password", type="password")

    if pwd == PASSWORD:
        st.session_state.authenticated = True
        st.rerun()
    elif pwd != "":
        st.error("Wrong password")

    st.stop()  # STOP here if not authenticated

# -----------------------
# MAIN APP
# -----------------------
st.title("Import Cost Calculator")
st.success("Access granted")


# === FORM ===
with st.form("calculator_form"):
    LCDPrice = st.number_input("Harga LCD (Yuan)", min_value=0.0)
    Kurs = st.number_input("Yuan Converter", min_value=0.0)
    Ship = st.selectbox("Ukuran Kapal", [20, 40])
    Piece = st.number_input("Jumlah barang (pcs)", min_value=1)
    submitted = st.form_submit_button("Hitung")

# === LOGIC & OUTPUT ===
if submitted:
    result = calculate_import_cost(
      lcd_price=LCDPrice, 
      kurs=Kurs, 
      ship=Ship, 
      piece=Piece
    )

    st.subheader("Hasil Perhitungan")
    st.write(f"Modal: Rp {result['modal']:,.0f}")
    st.write(f"Shipping per pcs (Freight): Rp {result['shipping_per_piece']:,.0f}")
    st.write(f"PPJK per pcs: Rp {result['ppjk_per_piece']:,.0f}")
    st.write(f"PIB: Rp {result['pib']:,.0f}")
    st.success(f"Final Modal per pcs: Rp {result['final_modal']:,.0f}")