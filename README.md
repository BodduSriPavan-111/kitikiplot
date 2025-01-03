![plot](https://drive.google.com/uc?id=1kzO8VZC38-ktIezrnFvH1b7K84zGBrsL)

<div align="center">

![PyPI](https://img.shields.io/pypi/v/kitikiplot?color=blueviolet)
![PyPI - Downloads](https://img.shields.io/pypi/dm/kitikiplot?color=gold)
[![DOI](https://zenodo.org/badge/874294211.svg)](https://doi.org/10.5281/zenodo.14292811)
![License](https://img.shields.io/github/license/BodduSriPavan-111/kitikiplot?color=green)

</div>

# KitikiPlot
KitikiPlot is a Python library for visualizing sequential and time-series categorical "Sliding Window" data. <br>
(The term 'kitiki' means 'window' in Telugu)

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

Please refer <a href="https://github.com/BodduSriPavan-111/kitikiplot/blob/main/CONTRIBUTING.md">CONTRIBUTING.md</a> for <b>contributions</b> to kitikiplot.

### Author
<a href="https://www.linkedin.com/in/boddusripavan/"> Boddu Sri Pavan </a> & 
<a href="https://www.linkedin.com/in/boddu-swathi-sree-2a2a58332/"> Boddu Swathi Sree </a>

## Citation

> @software{ KitikiPlot_2024 <br/>
> author = {Boddu Sri Pavan and Boddu Swathi Sree}, <br/>
> title = {{KitikiPlot: A Python library to visualize categorical sliding window data}}, <br/>
> year = {2024}, <br/>
> version = {0.1.2}, <br/>
> url = {\url{https://github.com/BodduSriPavan-111/kitikiplot}, <br/>
> doi = {10.5281/zenodo.14293030} <br/>
> howpublished = {\url{https://github.com/BodduSriPavan-111/kitikiplot}} <br/>
> }

## Thank You !
