import streamlit as st
import streamlit.components.v1 as components

# Title of the app
st.title("Embedded Tableau Dashboard")

# Embed Tableau dashboard using the provided HTML code
html_code = """
<div class='tableauPlaceholder' id='viz1732312919874' style='position: relative'><noscript><a href='#'><img alt='Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1_17258251624400&#47;Dashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book1_17258251624400&#47;Dashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1_17258251624400&#47;Dashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                
<script type='text/javascript'>                    
    var divElement = document.getElementById('viz1732312919874');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (divElement.offsetWidth > 800) { 
        vizElement.style.width='1280px';
        vizElement.style.height='956px';
    } else if (divElement.offsetWidth > 500) { 
        vizElement.style.width='1280px';
        vizElement.style.height='956px';
    } else { 
        vizElement.style.width='100%';
        vizElement.style.height='1427px';
    } 
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

# Render the HTML code in Streamlit
components.html(html_code, height=1000)