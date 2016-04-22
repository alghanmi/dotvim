##VIM Setup
This repository hosts my personal vim setup.

```bash
git clone --recursive  git@github.com:alghanmi/dotvim.git ~/.vim
mkdir -p ~/.vim/.swap ~/.vim/.undo
ln -s ~/.vim/vimrc ~/.vimrc
```

###Notes
  + To update all dependencies
```bash
git submodule update --init --recursive
curl --silent --show-error --location --output ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
```
