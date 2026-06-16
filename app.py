import gradio as gr
import pandas as pd
import joblib

# Load model dan kolom training
model = joblib.load("scrollsense_model.pkl")
columns = joblib.load("model_columns.pkl")


def predict_risk(
    age,
    gender,
    academic_level,
    country,
    usage_hours,
    platform,
    academic_effect,
    sleep_hours,
    mental_health,
    relationship_status,
    conflicts
):

    data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Academic_Level": academic_level,
        "Country": country,
        "Avg_Daily_Usage_Hours": usage_hours,
        "Most_Used_Platform": platform,
        "Affects_Academic_Performance": academic_effect,
        "Sleep_Hours_Per_Night": sleep_hours,
        "Mental_Health_Score": mental_health,
        "Relationship_Status": relationship_status,
        "Conflicts_Over_Social_Media": conflicts
    }])

    # One Hot Encoding
    data = pd.get_dummies(data)

    # Menyesuaikan kolom dengan data training
    data = data.reindex(
        columns=columns,
        fill_value=0
    )

    prediction = model.predict(data)[0]

    if prediction == "Rendah":
        return """
🟢 RISIKO RENDAH

Penggunaan media sosial masih dalam batas yang wajar.

Saran:
• Pertahankan pola penggunaan saat ini
• Tetap menjaga keseimbangan aktivitas akademik dan sosial
• Pertahankan kualitas tidur yang baik
"""

    elif prediction == "Sedang":
        return """
🟡 RISIKO SEDANG

Pengguna menunjukkan beberapa indikator ketergantungan media sosial.

Saran:
• Kurangi durasi penggunaan media sosial
• Buat jadwal penggunaan harian
• Prioritaskan aktivitas akademik dan produktif
"""

    else:
        return """
🔴 RISIKO TINGGI

Pengguna menunjukkan tingkat ketergantungan media sosial yang tinggi.

Saran:
• Batasi penggunaan media sosial secara bertahap
• Tingkatkan aktivitas offline
• Perhatikan kualitas tidur dan kesehatan mental
• Kurangi konflik yang dipicu oleh media sosial
"""


with gr.Blocks(title="ScrollSense") as demo:

    gr.Markdown("""
# 📱 ScrollSense

### Prediksi Risiko Ketergantungan Media Sosial Mahasiswa

Aplikasi ini menggunakan model **Random Forest Machine Learning**
untuk memprediksi tingkat risiko ketergantungan media sosial berdasarkan pola aktivitas digital pengguna.

Silakan isi data berikut untuk mendapatkan hasil prediksi.
""")

    with gr.Row():

        with gr.Column():

            age = gr.Slider(
                minimum=15,
                maximum=35,
                value=20,
                step=1,
                label="🎂 Usia"
            )

            gender = gr.Dropdown(
                choices=["Female", "Male"],
                value="Female",
                label="👤 Gender"
            )

            academic_level = gr.Dropdown(
                choices=[
                    "Undergraduate",
                    "Graduate",
                    "High School"
                ],
                value="Undergraduate",
                label="🎓 Academic Level"
            )

            country = gr.Textbox(
                value="Indonesia",
                label="🌍 Country"
            )

            usage_hours = gr.Slider(
                minimum=0,
                maximum=24,
                value=5,
                step=0.5,
                label="⏰ Average Daily Usage Hours"
            )

            platform = gr.Dropdown(
                choices=[
                    "Instagram",
                    "Twitter",
                    "TikTok",
                    "YouTube",
                    "Facebook",
                    "LinkedIn",
                    "Snapchat",
                    "LINE",
                    "KakaoTalk",
                    "VKontakte",
                    "WhatsApp",
                    "WeChat"
                ],
                value="Instagram",
                label="📱 Most Used Platform"
            )

        with gr.Column():

            academic_effect = gr.Radio(
                choices=["Yes", "No"],
                value="No",
                label="📚 Affects Academic Performance"
            )

            sleep_hours = gr.Slider(
                minimum=1,
                maximum=12,
                value=7,
                step=1,
                label="😴 Sleep Hours Per Night"
            )

            mental_health = gr.Slider(
                minimum=0,
                maximum=10,
                value=5,
                step=1,
                label="🧠 Mental Health Score"
            )

            relationship_status = gr.Dropdown(
                choices=[
                    "In Relationship",
                    "Single",
                    "Complicated"
                ],
                value="Single",
                label="❤️ Relationship Status"
            )

            conflicts = gr.Slider(
                minimum=0,
                maximum=5,
                value=0,
                step=1,
                label="⚠️ Conflicts Over Social Media"
            )

            output = gr.Textbox(
                label="🎯 Hasil Prediksi",
                lines=10
            )

    predict_btn = gr.Button(
        "🚀 Predict Risk",
        variant="primary"
    )

    predict_btn.click(
        fn=predict_risk,
        inputs=[
            age,
            gender,
            academic_level,
            country,
            usage_hours,
            platform,
            academic_effect,
            sleep_hours,
            mental_health,
            relationship_status,
            conflicts
        ],
        outputs=output
    )

demo.launch()