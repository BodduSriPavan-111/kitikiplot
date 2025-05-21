![plot](https://drive.google.com/uc?id=1kzO8VZC38-ktIezrnFvH1b7K84zGBrsL)

<div align="center">

[![PyPI Downloads](https://static.pepy.tech/badge/kitikiplot)](https://pepy.tech/projects/kitikiplot)
![PyPI](https://img.shields.io/pypi/v/kitikiplot?color=gold)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14632005.svg)](https://doi.org/10.5281/zenodo.14632005)
![License](https://img.shields.io/github/license/BodduSriPavan-111/kitikiplot?color=green)

</div>

# KitikiPlot
KitikiPlot is a Python library for visualizing sequential and time-series categorical "Sliding Window" data. <br>
(The term 'kitiki' means 'window' in Telugu)

Our preprint is published in **TechRxiv**. Find it <a href="https://www.techrxiv.org/users/877016/articles/1256589-kitikiplot-a-python-library-to-visualize-categorical-sliding-window-data"> here <a/>

Research paper is published in **GIS Science Journal** Volume 12 Issue 1, 186-193, 2025 (Scopus indexed with Impact factor **6.1**). </br>
Read it here: <a href="https://zenodo.org/records/14632005">https://zenodo.org/records/14632005</a>
<!--
## Table of Contents</h2>
- [Why Kitkiplot?](#What-and-why)
- [Getting Started](#getting-started)
- [Contribute](#contribute)
- [Maintainer(s)](#maintainer(s))
- [Citation](#citation)

## Why Kitikiplot?
-->

### Examples 
Genome Visualization can be found in [Genome.ipynb](https://github.com/BodduSriPavan-111/kitikiplot/blob/add-comments/examples/Genome.ipynb)
![plot](https://drive.google.com/uc?id=1vpRcqUsalg64ILluCgcXfoaUfcqQfHVN)
<br><br>
Weather Pattern in [Weather Pattern.ipynb](https://github.com/BodduSriPavan-111/kitikiplot/blob/add-comments/examples/Weather_Pattern.ipynb)
![plot](https://drive.google.com/uc?id=1tl5XefYfBqQTap1X0iDNoY3upk0FHFni)
<br><br>
CO Trend in Air in [Air_Quality.ipynb](https://github.com/BodduSriPavan-111/kitikiplot/blob/add-comments/examples/Air_Quality.ipynb)
![plot](https://drive.google.com/uc?id=1LTFgNDX-OlTwkSQjsWA3x6xHRLyu_a6O)
<br>

### Getting Started
Install the package via pip:
```
pip install kitikiplot
```
#### Usage
```py
from kitikiplot import KitikiPlot

data = [] # DataFrame or list of sliding window data

ktk= KitikiPlot( data= data )

ktk.plot( display_legend= True ) # Display the legend
```
Check out the complete <b>guide of customization</b> [here](https://github.com/BodduSriPavan-111/kitikiplot/blob/main/examples/Usage_Guide.ipynb).

## To-do
🟢 Domain-specific modules (In Progress) </br>
🟢 Streamlit Demo Interface (In Progress) </br>
🟢 Website for documentation (In Progress)
- [ ] Tooltip
- [ ] Interactive Plot

Please refer <a href="https://github.com/BodduSriPavan-111/kitikiplot/blob/main/CONTRIBUTING.md">CONTRIBUTING.md</a> for <b>contributions</b> to kitikiplot.

To join the Discord server for more discussion, click <a href="https://discord.gg/PQKtqm5p">here</a>

### Key Author
<a href="https://www.linkedin.com/in/boddusripavan/"> Boddu Sri Pavan </a>

## Citation
APA <br>
> Boddu Sri Pavan, Chandrasheker Thummanagoti, & Boddu Swathi Sree. (2025). KitikiPlot A Python library to visualize categorical sliding window data. https://doi.org/10.5281/zenodo.14632005.

IEEE <br>
> Boddu Sri Pavan, Chandrasheker Thummanagotiand Boddu Swathi Sree, “KitikiPlot A Python library to visualize categorical sliding window data”, 2025, doi: 10.5281/zenodo.14632005.

BibTeX <br>
> @misc{boddu_sri_pavan_2025_14632005,       <br>
>  author       = {Boddu Sri Pavan and       <br>
>                  Chandrasheker Thummanagoti and       <br>
>                  Boddu Swathi Sree},       <br>
>  title        = {KitikiPlot A Python library to visualize       <br>
>                   categorical sliding window data       <br>
>                  },       <br>
>  month        = jan,       <br>
>  year         = 2025,       <br>
>  publisher    = {Zenodo},       <br>
>  doi          = {10.5281/zenodo.14632005},       <br>
>  url          = {https://doi.org/10.5281/zenodo.14632005},       <br>
>}

## Execute Tests when contributing to KitikiPlot

Please refer <a href="https://github.com/BodduSriPavan-111/kitikiplot/blob/main/tests/unit_test/Readme.md">Readme.md</a> to run the tests

## Thank You !
