from flask import Flask,Blueprint, render_template
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib
matplotlib.use('agg')
import os
import io

data = pd.read_excel("pybo/static/others/코로나19 발병 사례 최종.xlsx", sheet_name=None, skiprows=4)
mpl.rc('font', family='Apple SD Gothic Neo')

bp = Blueprint("covid19", __name__, url_prefix="/covid19")


@bp.route("/information")
def covid19_inform():
    global data
    data_dict= data.items()
    sheet_name, df1 = next(iter(data_dict))

    df1 = df1.set_index("일자")
    df1 = df1.iloc[:,:4]
    df1.drop(df1.index[0], axis="index", inplace=True)
    df1.index=pd.to_datetime(df1.index)
    df1.replace("-", 0, inplace=True)

    covid_stats= pd.pivot_table(data=df1, index=df1.index, values=["국내발생(명)", "해외유입(명)", "사망"])
    covid_stats.plot(kind="line", y=['국내발생(명)','해외유입(명)','사망'], figsize=(20,10), ax=plt.gca())

    img_path = "pybo/static/others/covid19_stats.png"
    plt.savefig(img_path)
    img_path = img_path[11:]
    plt.close()

    return render_template("covid19/covid19_stats.html", sheet_name=sheet_name, img_path=img_path)
