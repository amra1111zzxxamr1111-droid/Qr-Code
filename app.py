import streamlit as st
import qrcode
from PIL import Image
import io

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Amr Group Tools", page_icon="📶")

# --- الهيدر (اسم الشركة والبراند) ---
st.title("📶 Amr Group - Smart QR Tool")
st.markdown("أهلاً بك في الأدوات الذكية من **Amr Group**. صُمم هذا التطبيق لخدمتك بسرعة وأمان.")
st.markdown("---")

# --- التبويبات (تنظيم احترافي) ---
tab1, tab2 = st.tabs(["📶 توليد QR للواي فاي", "🔗 توليد QR للروابط والنصوص"])

with tab1:
    st.subheader("اتصال سريع بالواي فاي")
    st.write("أدخل بيانات الشبكة وسنحولها لـ QR يسهل الاتصال به.")
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
            st.warning("يرجى إدخال اسم الشبكة والباسورد أولاً!")

with tab2:
    st.subheader("مُولد الباركود العام")
    st.write("حول أي رابط أو نص لـ QR خاص بك.")
    data = st.text_area("أدخل النص أو الرابط هنا:")
    if st.button("إنشاء الباركود"):
        if data:
            img = qrcode.make(data)
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            st.image(buf, caption="الباركود الخاص بك")
            st.download_button("تحميل الباركود", data=buf.getvalue(), file_name="my_qr.png")
        else:
            st.warning("يرجى إدخال الرابط أو النص.")

# --- الفوتر (معلومات الشركة - التواصل المباشر) ---
st.markdown("---")
st.markdown(f"""
### 📞 تواصل مع Amr Group
نحن هنا لدعمك في أي وقت. لا تتردد في مراسلتنا:

* **واتساب:** [اضغط للمراسلة 01107545181](https://wa.me/201107545181)
* **موقعنا الرسمي:** [https://amr-group.vercel.app/](https://amr-group.vercel.app/)
* **صمم هذا الموقع ليكون أداة مساعدة سريعة لعملاء Amr Group.**
""")
