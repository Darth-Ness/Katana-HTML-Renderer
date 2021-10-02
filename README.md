# Katana-HTML-Renderer-Dev

Katana is very, very limited at the moment.
When using the dev version you get the lastest features, but it is not as stable as the main branch.

Only the following tags can be rendered: `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, and `p`, `img`
## Note about Img
Support for this tag is limited. As you can only render one image at a time.

## Install
If you would like to test this on your computer run the following commands:
```bash
git clone https://github.com/Darth-Ness/Katana-HTML-Renderer.git
cd Katana-HTML-Renderer
chmod u+x parser.py
python3 importer.py
```
  
## Features
- Due to the way code is rendered, you do not have to close your tags.
- It is very fast, on my system it was able to render (a very basic webpage) in 140 ms! And most of that was probably interpreting.
  
## Limitations
- It can only render text.
- No CSS parsing.
- No JavaScript at all.
  
Have something you would like to add? Please make a pull request with your changes!

Font Used: SF Pro
