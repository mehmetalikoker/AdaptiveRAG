import streamlit as st
from graph.graph import app  # Senin mevcut graph yapın
from dotenv import load_dotenv

load_dotenv()

# --- UI Sayfa Ayarları ---
st.set_page_config(page_title="Adaptive RAG Assistant", page_icon="🤖", layout="centered")

st.title("🤖 Adaptive RAG Asistanı")
st.markdown("Sorunuzu sorun, sistem en uygun stratejiyle (Retrieve/Web Search) cevaplasın.")

# --- Sohbet Geçmişi ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Eski mesajları ekranda göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Kullanıcı Girişi ---
if prompt := st.chat_input("Nasıl yardımcı olabilirim?"):
    # Kullanıcı mesajını göster ve kaydet
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Graph Çalıştırma ---
    with st.chat_message("assistant"):
        with st.spinner("Düşünüyorum ve araştırıyorum..."):
            # Graph'a input veriyoruz
            inputs = {"question": prompt}

            # Graph'ı çalıştır ve sonucu al
            # Not: app.invoke senin main.py'daki mantığınla aynıdır
            final_state = app.invoke(inputs)

            # GraphState içindeki 'generation' anahtarını alıyoruz
            answer = final_state.get("generation", "Üzgünüm, bir cevap üretilemedi.")

            st.markdown(answer)

            # Kaynakları veya izlenen yolu göstermek istersen (Opsiyonel):
            if final_state.get("web_search"):
                st.caption("🌐 Bu cevap için web araması kullanıldı.")
            else:
                st.caption("📚 Bu cevap yerel dökümanlar kullanılarak oluşturuldu.")

    # Asistan cevabını kaydet
    st.session_state.messages.append({"role": "assistant", "content": answer})