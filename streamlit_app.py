import streamlit as st

st.set_page_config(
    page_title="Project",
  
)

st.write("FINAL PROJECT")
st.write("Name: Tianxin Yin (Stark)")
st.write("Student ID: 1330365249")

def main():
    # Embedding CSS styles
    st.markdown("""
        <style>
            .title-row {
                color: white;
                text-align: center;
                background-color: #666362;
            }
            .page {
                color: white;
                background-color: #666362;
            }
            .site-footer {
                background-color: #26272b;
                padding: 45px 0 20px;
                font-size: 15px;
                line-height: 24px;
                color: #737373;
                box-shadow: 0 10px 20px rgba(0,0,0,0.5);
            }
            .site-footer hr {
                border-top-color: #bbb;
                opacity: 0.5;
            }
            .site-footer hr.small {
                margin: 20px 0;
            }
            .site-footer h6 {
                color: #fff;
                font-size: 16px;
                text-transform: uppercase;
                margin-top: 5px;
                letter-spacing: 2px;
            }
            .site-footer a {
                color: #737373;
            }
            .site-footer a:hover {
                color: #fff;
                text-decoration: none;
            }
            .footer-author {
                padding-left: 0;
                list-style: none;
            }
            .footer-author li {
                display: block;
            }
            .footer-author a {
                color: #737373;
            }
            .footer-author a:active,
            .footer-author a:focus,
            .footer-author a:hover {
                color: #fff;
                text-decoration: none;
            }
            .copyright-text {
                margin: 0;
            }
            @media (max-width: 991px) {
                .site-footer [class^="col-"] {
                    margin-bottom: 30px;
                }
            }
            @media (max-width: 767px) {
                .site-footer {
                    padding-bottom: 0;
                }
                .site-footer .copyright-text,
                .site-footer .social-icons {
                    text-align: center;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    # Embedding HTML content
    st.markdown("""
        <html lang="en">
        <head>
            <meta charset="utf-8"/>
            <meta content="width=device-width, initial-scale=1.0" name="viewport">
            <title>Project</title>
            <link crossorigin="anonymous" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
                  integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" rel="stylesheet">
            <link crossorigin="anonymous" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css"
                  integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA=="
                  rel="stylesheet"/>
            <link href="style.css" rel="stylesheet">
            <link rel="stylesheet" type="text/css" href="home.css">
        </head>
        <body>
        <div style="background-color: #666362;">


   

</div>
<div id="map"></div>
<iframe style="background: #F1F5F4;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);width: 100vh;height: 100vh;"  src="https://charts.mongodb.com/charts-mongoheroku-fippb/embed/dashboards?id=bda286af-9e3b-4db5-aeb8-5b199d18c824&theme=light&autoRefresh=true&maxDataAge=3600&showTitleAndDesc=false&scalingWidth=fixed&scalingHeight=fixed"></iframe>
<h3 style= "color: rgb(9, 127, 236);">Population</h3>
<p class="text-justify">The Population data provides information about the distribution and 
    density of human settlements in a geographic area. It typically includes demographic details 
    such as population count. In this project, population data from the Global Human Settlement 
    Layer (GHSL) was used. This dataset is valuable for understanding population density, 
    urbanization patterns, and areas of high human activity, which are essential for analyzing 
    the impact of weather on human settlements and vulnerability assessment.
</p>
<h3 style= "color: rgb(9, 127, 236);">Temperature</h3>
<p class="text-justify">Temperature data represents historical weather observations related to 
    temperature, collected from various weather stations worldwide. In this project, 
    temperature data was obtained from NOAA's Climate Data Online Tool (CDOT). The dataset 
    includes information on daily temperature readings, such as average temperature. 
    Analyzing temperature data allows us to understand long-term weather patterns, trends, 
    and variability, which are crucial for assessing the influence of weather conditions on 
    human settlements and land cover dynamics.
</p>
<h3 style= "color: rgb(9, 127, 236);">Land Use</h3>
<p class="text-justify">The land use data provides information on how land is utilized 
    within different regions. The description suggests that land use patterns vary, with urban 
    areas characterized by dense development and vegetated areas containing forest cover. 
    This distinction in land use contributes to the observed temperature differences, 
    with urban areas experiencing higher temperatures due to the prevalence of impervious 
    surfaces and reduced vegetation cover. Understanding land use patterns helps in assessing the 
    environmental impact of human activities and informing urban planning decisions aimed at
     promoting sustainability and resilience.
</p>
<div id="map"></div>
<div style="display: flex; justify-content: space-between;">
    <iframe style="background: #F1F5F4; border: none; border-radius: 2px; box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2); width: calc(50% - 10px); height: 700px;" src="https://nu.maps.arcgis.com/apps/instant/basic/index.html?appid=ca725242c91d4d7d84c380c308f3c6fc"></iframe>
    <iframe style="background: #F1F5F4; border: none; border-radius: 2px; box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2); width: calc(50% - 10px); height: 700px;" src="https://nu.maps.arcgis.com/apps/instant/basic/index.html?appid=a2ca9d6f7936493ea06ce7db0d49f944"></iframe>
</div>

<embed id="6381c86c-938e-4aa5-8256-909609c3d21f">

       
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
