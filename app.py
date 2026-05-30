import streamlit as st
import qrcode
from PIL import Image
import io

st.title("Amr Group - QR Generator")

data = st.text_input("أدخل الرابط أو نص الواي فاي هنا:")

if st.button("إنشاء الباركود"):
    if data:
        # إنشاء الباركود
        qr = qrcode.QRCode(box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # حفظ الصورة في الذاكرة
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        
        # عرض الصورة
        st.image(buf, caption="الباركود الخاص بك")
        st.download_button("تحميل الباركود", data=buf.getvalue(), file_name="qrcode.png")