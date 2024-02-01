
# Git

###### Basic Git commands

- [Rubygarage](https://rubygarage.org/blog/most-basic-git-commands-with-examples)
- [rogerdudler](https://rogerdudler.github.io/git-guide/)

###### Work flow

Local repository consists of three "trees" maintained by git. 
- The first one is **Working Directory** which holds the actual files. 
- The second one is the **Index** which acts as a staging area.
-  Finally the **HEAD** which points to the last commit you've made.

###### GIt installation with choco on Windows

Use chocolatey to install GIT & poshgit to give you colour & tab completion

```powershell
choco install git -y
choco install poshgit -y
```

###### Git configuration

```ruby
git config --global user.name "Your name"
git config --global user.email "your_email@SomeDomain.com"
git config --global color.ui.true
git config --global --list
```

### GIT Setup on new machine
 
> From the new machine create new public key using **ssh-keygen** or other tools & paste it on git **user settings** 


### Create new repository

```ruby
git init
git status
```

### Add & Commit

```ruby
git add <file-name>
git add <file-name> <yet-another-file-name>
git add .
git add --all
git add -A
git commit -m "Your message"
```

### Untrack file\folder

> To untrack file\folder that was tracked before, 

```ruby
git rm --cached <file-name>
git reset <file-name>
```

> then add the **file-Name** to .gitignore file

### Commiting to repository

```ruby
git commit -m "Your message"
git reset --soft HEAD
git commit --amend m "Your message"
```

### Git pull\push from & reporository

```ruby
git remote add arigin <link>
git push -u origin master
git clone <clone>
git pull
```

### Branching
> Branches are used to develop features isolated from each other. 
 
> The master branch is the **default** branch when you create a repository. 

> Use other branches for development and merge them back to the master branch upon completion.

>create a new branch named "feature_x" and switch to it using

```ruby
git checkout -b feature_x
```

> switch back to master

```ruby
git checkout master
```

> and delete the branch again

```ruby
git branch -d feature_x
```

> a branch is not available to others unless you push the branch to your remote repository

```ruby
git push origin <branch>
```

### Update & Merge

> To update your local repository to the newest commit, execute

```ruby
git pull
```

> in your working directory to fetch and merge remote changes.
> to merge another branch into your active branch (e.g. master), use

```ruby
git merge <branch>
```

> in both cases git tries to auto-merge changes. Unfortunately, this is not always possible and results in conflicts. You are responsible to merge those conflicts manually by editing the files shown by git. After changing, you need to mark them as merged with

```ruby
git add <filename>
```

> before merging changes, you can also preview them by using

```ruby
git diff <source_branch> <target_branch>
```

### Tagging

> it's recommended to create tags for software releases. this is a known concept, which also exists in SVN. You can create a new tag named 1.0.0 by executing

```ruby
git tag 1.0.0 1b2e1d63ff
```

> the 1b2e1d63ff stands for the first 10 characters of the commit id you want to reference with your tag. You can get the commit id by looking at the log

### log

> in its simplest form, you can study repository history using.. git log
You can add a lot of parameters to make the log look like what you want. To see only the commits of a certain author:

```ruby
git log --author=bob
```

> To see a very compressed log where each commit is one line:

```ruby
git log --pretty=oneline
git log --oneline
```

> Or maybe you want to see an ASCII art tree of all the branches, decorated with the names of tags and branches:

```ruby
git log --graph --oneline --decorate --all
```

>See only which files have changed:

```ruby
git log --name-status
```

>These are just a few of the possible parameters you can use, see

```ruby
git log --help
```

### Setup alias

>global configuration file located at home ~\.gitconfig.  This can help with long commands, see below for some examples.  The file can be edited manullay or using commands

```ruby
git config --global alias.st "status"
```

```ruby
[alias]
  st = status
  co = checkout
  ci = commit
  br = branch
  df = diff
  dfs = diff -staged
  logg = log --graph --decorate --oneline --all
```

###### troubleshooting

could not push cloned repo, asking for username & passwd. because originally I clone it using HTTPS.
used these commands, set to use ssh

```bash
# add ssh public key to your settings--> 'SSH and GPG keys'
git remote set-url origin git@github.com:username/repo.git

# check if you have added the remote HTTPS or SSH settings
git remote -v
```