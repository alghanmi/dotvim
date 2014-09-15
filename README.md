##VIM Setup
This repository hosts my personal vim setup.

```bash
git clone --recursive  git@github.com:alghanmi/dotvim.git ~/.vim
mkdir -p ~/.vim/.swap ~/.vim/.undo
ln -s ~/.vim/vimrc ~/.vimrc
```

###Notes
  + To update all submodules
```bash
git submodule foreach git pull origin master
```
