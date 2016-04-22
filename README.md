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

  + To add a new bundle or plugin
```bash
export PLUGIN_GIT_REPO=git@github.com:tpope/vim-sensible.git
cd ~/.vim/bundle && git submodule add $PLUGIN_GIT_REPO && cd -
```
