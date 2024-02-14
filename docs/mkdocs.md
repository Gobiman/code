#### Requirements
* Python
* editor (vscode)
* github account
* [mkdocs material](https://squidfunk.github.io/mkdocs-material/)

##### Create a repo on Github
 - give a name
- public
- Create README.md file
-  ignore python
-  general licence

##### On computer
```bash
#If python envvironment not installed
sudo apt install python3.10-venv 
# clone the github repo created above
git clone git@github.com:Gobiman/mkdocs-material.git  
cd <folder>
#create python environment
python3 -m venv venv  
# activate the environment
source venv/bin/activate 
pip --version
#upgrade pip if required
pip install --upgrade pip  
pip3 install mkdocs
#Open in VScode or any editor
code .   
#will create mkdocs (mkdocs.yaml & docs\index.md)
mkdocs new .  
#build and test the site on your machine
mkdocs serve 
# deploys to gh-pages branch, e.g. site "https://gobiman.github.io/door/"
mkdocs gh-deploy --force 
```

```bash
git add .
git commit -m "some informations"
git push origin main
```

```bash 
# deactivate the enviornment once development is done
deactivate  
```
