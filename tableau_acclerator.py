import streamlit as st
import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components




if __name__ =="__main__":
    st.set_page_config(layout="wide")
    st.title("Welcom to Viz CoP: July Specials")
    st.subheader("Attribution Dashboard")
    tableau_dashboard_html = "<div class='tableauPlaceholder' id='viz1658381601538' style='position: relative'><noscript><a href='#'><img alt='viz ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;HR&#47;HRAttritionDashboardRWFD_16570446563570&#47;viz&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='HRAttritionDashboardRWFD_16570446563570&#47;viz' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;HR&#47;HRAttritionDashboardRWFD_16570446563570&#47;viz&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1658381601538');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1450px';vizElement.style.height='977px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    components.html(tableau_dashboard_html, height=1000)
    st.subheader("HR Data Profile/Summary")
    hr_data = pd.read_csv("hr_sample_data_viz_CoP_July.csv", sep = "|")
    data_profile = ProfileReport(hr_data, explorative = True)
    st_profile_report(data_profile)

