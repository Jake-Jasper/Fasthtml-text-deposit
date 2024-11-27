"""
Want similar functionality to upload text file - https://gallery.fastht.ml/split/start_simple/csv_editor
Probably this one as well for data spot checks - https://github.com/AnswerDotAI/fasthtml-example/blob/main/data_spot_check/main.py
And embed a pdf - https://gallery.fastht.ml/split/widgets/pdf

Next, put the text spitter in,

After that have input to chagne text splitter
"""
from fasthtml.common import *

app, router = fast_app(live=True)

TMP_FILE : str = r"E:\Python stuff\Web apps\Fasthtml-retriever\01 - The Fellowship Of The Ring.txt"

def load_text(path):
    file = open(path, "r")
    doc = file.read()
    file.close()
    return doc


"""Should make one text area take from the other, therefore
if one is altered it cahnges the other??"""


@router
def index():
    # Here type is "internet media type"
    return Div(H1("View Text Chunking"),
               P("Introductory Text Goes here"),
                Div(
                Pre(load_text(TMP_FILE),contenteditable="readonly"),
                Textarea(load_text(TMP_FILE)),
                style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 10px; width: 100%; height: 800px;"
            )
    )

serve()

