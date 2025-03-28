import datetime
import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 50px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        text_align="center",
        height="auto",
        opacity=1,
    )

    body = p()
    foot = div(
        style=style_div
    )(
        # hr(
        #     style=style_hr
        # ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        
        "Esteban Basili",
         " - ",
        str(datetime.datetime.today()).split("-")[0],
        " ",
        "Ironhack Data Analytics Bootcamp",
        # "Made in ",
        # image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
        #       width=px(25), height=px(25)),
        # " with ❤️ by ",
        # link("https://twitter.com/ChristianKlose3", "@ChristianKlose3"),

        # br(),
        # link("https://buymeacoffee.com/chrischross", image('https://i.imgur.com/thJhzOO.png')),
    ]
    layout(*myargs)
