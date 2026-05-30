import streamlit as st
import qrcode
from PIL import Image
import io

# --- تصميم الصفحة ---
st.set_page_config(page_title="Amr Group Tools", page_icon="📶")

# --- الهيدر (اسم الشركة والبراند) ---
st.title("📶 Amr Group - Smart QR Tool")
st.markdown("---")

# --- التبويبات (تنظيم احترافي) ---
tab1, tab2 = st.tabs(["Wi-Fi QR", "Link/Text QR"])

with tab1:
    st.subheader("توليد باركود الواي فاي")
    ssid = st.text_input("اسم الشبكة (SSID):")
    password = st.text_input("كلمة السر:", type="password")
    if st.button("إنشاء باركود الواي فاي"):
        if ssid and password:
            wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
            img = qrcode.make(wifi_data)
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            st.image(buf, caption="امسح الباركود للاتصال مباشرة")
            st.download_button("تحميل الباركود", data=buf.getvalue(), file_name="wifi_qr.png")
        else:
            st.warning("يرجى إدخال اسم الشبكة والباسورد")

with tab2:
    st.subheader("توليد باركود للروابط أو النصوص")
    data = st.text_area("أدخل النص أو الرابط هنا:")
    if st.button("إنشاء الباركود"):
        if data:
            img = qrcode.make(data)
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            st.image(buf, caption="الباركود الخاص بك")
            st.download_button("تحميل الباركود", data=buf.getvalue(), file_name="my_qr.png")

# --- الفوتر (معلومات الشركة) ---
st.markdown("---")
st.markdown("""
### تواصل معنا - Amr Group
📞 **للدعم الفني:** 010xxxxxxxx  
🌐 **موقعنا:** [www.amrgroup.com](http://www.amrgroup.com)  
*صمم ليكون الأسرع والأكثر أماناً.*
""")
