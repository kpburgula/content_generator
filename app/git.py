import htmlgenerator as hg
import pandas as pd

df = pd.read_csv('app/git.csv')

unique_types = set(df['type'].tolist())
unique_topics = set(df['topic'].tolist())
unique_sub_topics = set(df['sub_topic'].tolist())

master_html = []

for unique_type in unique_types:
    for unique_topic in unique_topics:
        for unique_sub_topic in unique_sub_topics:
            temp_df = df[(df['type'] == unique_type) & (df['topic'] == unique_topic) & (df['sub_topic'] == unique_sub_topic)]
            if len(temp_df):
                if unique_sub_topic == 'None':
                    temp_html = [hg.H1(unique_topic), hg.HR()]
                else:
                    temp_html = [hg.H1(unique_topic), hg.H2(unique_sub_topic)]
                for ix,val in temp_df.iterrows():
                    temp_html.append(hg.H3(val['description']))
                    if unique_type == 'command':
                        temp_html.append(hg.CODE(val[unique_type]))
                    else:
                        temp_html.append(hg.P(val[unique_type]))
                
                master_html = master_html + temp_html



my_page = hg.HTML(hg.HEAD(), hg.BODY(hg.DIV(*master_html)))
my_page = hg.render(my_page, {})
with open("git.html", "w") as f:
    f.write(f'{my_page}')
