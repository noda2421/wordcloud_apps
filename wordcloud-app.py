import streamlit as st
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud


def nouns_maker(text):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    noun_list = []

    for token in tokens:
        if token.part_of_speech.split(",")[0] == "名詞":
            if not token.part_of_speech.split(",")[0] == omit_list:
                noun_list.append(token.surface)

    return " ".join(noun_list)


st.sidebar.text("config")
width = st.sidebar.slider("width", 0, 1200, 800, 10)
height = st.sidebar.slider("height", 0, 1200, 500, 10)
st.sidebar.selectbox("テーマ", ["gist_heat", "PuBuGn"])
omit_words = st.sidebar.text_input("除外したいワードをスペース区切りで入れてください")
omit_list = omit_words.split(" ")
st.title("Wordcloud Maker")
text = st.text_area("入力らん", placeholder="ワードクラウドにしたい文章を入れてください")

if st.button("作成"):
    nouns = nouns_maker(text)
    wc = WordCloud(width=500, height=500, font_path="ipaexg.ttf", collocations=False, colormap="PuBuGn")
    # collocationを設定すると単語かぶりを無くすかどうか設定できる
    wc.generate(nouns)
    wc.to_file("text.png")
    st.image("text.png")
