import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


st.set_page_config(page_title="Galaxy Translator", layout="centered")

st.markdown("""
<style>

.stApp {
    background-image: url("image.png");
    background-size: 220% 220%;
    background-position: center;
    animation: lavenderFlow 20s ease-in-out infinite;
}

@keyframes lavenderFlow {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: linear-gradient(
        120deg,
        rgba(220, 200, 255, 0.25),
        rgba(255, 255, 255, 0.12)
    );
    animation: softGlow 10s ease-in-out infinite alternate;
    pointer-events: none;
}

@keyframes softGlow {
    0%   { opacity: 0.4; }
    100% { opacity: 0.75; }
}
            
@keyframes galaxyMove {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}

body {
  background: linear-gradient(-45deg, #030014, #0a043c, #1b0033, #06001a);
  background-size: 400% 400%;
  animation: galaxyMove 12s ease infinite;
}

.sparkle {
  position: fixed;
  width: 6px;
  height: 6px;
  background: white;
  border-radius: 50%;
  animation: sparkle 4s infinite ease-in-out;
  opacity: 0.7;
}

@keyframes sparkle {
  0% {transform: scale(0.5); opacity: 0.3;}
  50% {transform: scale(1.2); opacity: 1;}
  100% {transform: scale(0.5); opacity: 0.3;}
}

.title {
  font-size: 42px;
  font-weight: bold;
  text-align: center;
  color: #A41EBB;
  
}

textarea {
  font-size: 18px !important;
  border: 2px solid #c77dff ;
  border-radius: 12px !important;
  background-color: white !important;
  color: #8943BC  !important;
}

.stButton>button {
  background: linear-gradient(135deg, #9b5de5, #f15bb5);
  color: white;
  font-size: 18px;
  border-radius: 12px;
  padding: 10px 25px;
  border: none;
  display:center;
}
.popup-card {
  background: linear-gradient(135deg, #ffffff, #f5d9ff, #ffffff);
  color: #3c096c;
  padding: 36px;
  margin-top: 38px;
  border-radius: 28px;
  text-align: center;
  font-size: 22px;
  font-weight: 800;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 55px rgba(255,255,255,0.95);
  animation: cardPop 0.7s ease;
  border: 2px solid #f5c2ff;
}

@keyframes cardPop {
  from {transform: scale(0.3); opacity: 0;}
  to {transform: scale(1); opacity: 1;}
}

.popup-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: -120%;
  width: 120%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.9), transparent);
  animation: shimmer 2.8s infinite;
}

@keyframes shimmer {
  0% {left: -120%;}
  100% {left: 120%;}
}
</style>

<div class="sparkle" style="top:10%; left:15%"></div>
<div class="sparkle" style="top:40%; left:85%"></div>
<div class="sparkle" style="top:70%; left:10%"></div>
<div class="sparkle" style="top:85%; left:60%"></div>
""", unsafe_allow_html=True)


# LOAD MODEL

@st.cache_resource(show_spinner=False)
def load_model():

    model_name = "facebook/nllb-200-distilled-600M"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True
    )

    return tokenizer, model


with st.spinner("Loading Galaxy Translator AI model..."):
    tokenizer, model = load_model()


# NLLB LANGUAGE MAP
# Human-friendly language name -> NLLB language code

language_map = {
    "Afrikaans": "afr_Latn",
    "Albanian": "als_Latn",
    "Amharic": "amh_Ethi",
    "Arabic": "arb_Arab",
    "Assamese": "asm_Beng",
    "Asturian": "ast_Latn",
    "Awadhi": "awa_Deva",
    "Azerbaijani": "azj_Latn",
    "Bashkir": "bak_Cyrl",
    "Bengali": "ben_Beng",
    "Bhojpuri": "bho_Deva",
    "Bosnian": "bos_Latn",
    "Bulgarian": "bul_Cyrl",
    "Burmese": "mya_Mymr",
    "Catalan": "cat_Latn",
    "Cebuano": "ceb_Latn",
    "Chinese (Simplified)": "zho_Hans",
    "Chinese (Traditional)": "zho_Hant",
    "Croatian": "hrv_Latn",
    "Czech": "ces_Latn",
    "Danish": "dan_Latn",
    "Dutch": "nld_Latn",
    "English": "eng_Latn",
    "Estonian": "est_Latn",
    "Filipino": "tgl_Latn",
    "Finnish": "fin_Latn",
    "French": "fra_Latn",
    "Galician": "glg_Latn",
    "Georgian": "kat_Geor",
    "German": "deu_Latn",
    "Greek": "ell_Grek",
    "Gujarati": "guj_Gujr",
    "Haitian Creole": "hat_Latn",
    "Hausa": "hau_Latn",
    "Hebrew": "heb_Hebr",
    "Hindi": "hin_Deva",
    "Hungarian": "hun_Latn",
    "Icelandic": "isl_Latn",
    "Igbo": "ibo_Latn",
    "Indonesian": "ind_Latn",
    "Irish": "gle_Latn",
    "Italian": "ita_Latn",
    "Japanese": "jpn_Jpan",
    "Javanese": "jav_Latn",
    "Kannada": "kan_Knda",
    "Kazakh": "kaz_Cyrl",
    "Khmer": "khm_Khmr",
    "Korean": "kor_Hang",
    "Kyrgyz": "kir_Cyrl",
    "Lao": "lao_Laoo",
    "Latin": "lat_Latn",
    "Latvian": "lvs_Latn",
    "Lithuanian": "lit_Latn",
    "Malay": "zsm_Latn",
    "Malayalam": "mal_Mlym",
    "Marathi": "mar_Deva",
    "Mongolian": "khk_Cyrl",
    "Nepali": "npi_Deva",
    "Norwegian": "nob_Latn",
    "Odia": "ory_Orya",
    "Persian": "pes_Arab",
    "Polish": "pol_Latn",
    "Portuguese": "por_Latn",
    "Punjabi": "pan_Guru",
    "Romanian": "ron_Latn",
    "Russian": "rus_Cyrl",
    "Sanskrit": "san_Deva",
    "Serbian": "srp_Cyrl",
    "Sinhala": "sin_Sinh",
    "Slovak": "slk_Latn",
    "Slovenian": "slv_Latn",
    "Somali": "som_Latn",
    "Spanish": "spa_Latn",
    "Swahili": "swh_Latn",
    "Swedish": "swe_Latn",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Thai": "tha_Thai",
    "Turkish": "tur_Latn",
    "Ukrainian": "ukr_Cyrl",
    "Urdu": "urd_Arab",
    "Uzbek": "uzn_Latn",
    "Vietnamese": "vie_Latn",
    "Welsh": "cym_Latn",
    "Yoruba": "yor_Latn",
    "Zulu": "zul_Latn"
}


st.markdown("<div class='title'>🌌 Language Translator</div>", unsafe_allow_html=True)
st.write("✨ Translate with cosmic ambience")

text = st.text_area("💫 Enter Your Text")


lang_list = list(language_map.keys())

col1, col2 = st.columns(2)

with col1:
    src_lang_name = st.selectbox(
        "🌍 Source Language",
        lang_list,
        index=lang_list.index("English"),
        placeholder="🔍 Search language..."
    )

with col2:
    tgt_lang_name = st.selectbox(
        "🌏 Target Language",
        lang_list,
        index=lang_list.index("Telugu"),
        placeholder="🔍 Search language..."
    )

src_lang = language_map[src_lang_name]
tgt_lang = language_map[tgt_lang_name]


if st.button("🚀 Translate"):

    if text.strip() == "":
        st.warning("Please enter text.")
    else:
        with st.spinner("🌠 Translating through the galaxy..."):

            # Tell NLLB which language the input text is written in
            tokenizer.src_lang = src_lang

            # Convert input text into tokens
            inputs = tokenizer(
                text,
                return_tensors="pt"
            ).to(model.device)

            # Generate translation
            with torch.no_grad():
                generated_tokens = model.generate(
                    **inputs,
                    forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_lang),
                    max_length=100
                )

            # Convert generated tokens back into normal text
            translated_text = tokenizer.batch_decode(
                generated_tokens,
                skip_special_tokens=True
            )[0].strip()

            translated_text = " ".join(translated_text.split())

        st.markdown(
            f"<div class='popup-card'>{translated_text}</div>",
            unsafe_allow_html=True
        )
