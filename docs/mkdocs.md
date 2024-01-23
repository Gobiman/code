#### Requirements
* Python
* editor (vscode)
* github account

##### Create a repo on Github
 - give a name
- public
- Create README.md file
-  ignore python
-  general licence

##### On computer
```bash
sudo apt install python3.10-venv #If python envvironment not installed
git clone git@github.com:Gobiman/mkdocs-material.git  # clone the github repo created above
git clone git@github.com:Gobiman/mkdocs-material.git  # clone the github repo created above
cd <folder>
python3 -m venv venv  #create python environment
source venv/bin/activate # activate the environment
pip --version
pip install --upgrade pip  #upgrade pip if required
pip3 install mkdocs
code .  #Open in VScode or any editor 
mkdocs new .  #will create mkdocs (mkdocs.yaml & docs\index.md)
mkdocs serve  #build and test the site on your machine
mkdocs gh-deploy --force # deploys to gh-pages branch, e.g. site "https://gobiman.github.io/door/"
```
```bash title="git commands to sync to github repo"
git add .
git commit -m "some informations"
git push origin main
```
```bash 
deactivate  # deactivate the enviornment once development is done
```
