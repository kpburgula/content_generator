import htmlgenerator as hg
import pandas as pd
from config import Columns, FileConfig

df = pd.read_csv(FileConfig.CSV_FILE_PATH)

unique_types = set(df[Columns.TYPE].tolist())
unique_topics = set(df[Columns.TOPIC].tolist())
unique_sub_topics = set(df[Columns.SUB_TOPIC].tolist())

master_html = []

for unique_type in unique_types:
    for unique_topic in unique_topics:
        for unique_sub_topic in unique_sub_topics:
            temp_df = df[(df[Columns.TYPE] == unique_type) & (df[Columns.TOPIC] == unique_topic) & (df[Columns.SUB_TOPIC] == unique_sub_topic)]
            if len(temp_df):
                if unique_sub_topic == 'None':
                    temp_html = [hg.H1(unique_topic), hg.HR()]
                else:
                    temp_html = [hg.H1(unique_topic), hg.H2(unique_sub_topic)]
                for ix,val in temp_df.iterrows():
                    temp_html.append(hg.H3(val[Columns.DESCRIPTION]))
                    if unique_type == Columns.COMMAND:
                        temp_html.append(hg.CODE(val[unique_type]))
                    else:
                        temp_html.append(hg.P(val[unique_type]))
                
                master_html = master_html + temp_html



my_page = hg.HTML(hg.HEAD(), hg.BODY(hg.DIV(*master_html)))
my_page = hg.render(my_page, {})
with open(FileConfig.OUTPUT_HTML_FILE_PATH, "w") as f:
    f.write(f'{my_page}')
