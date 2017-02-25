##VIM Setup
This repository hosts my personal vim setup.

```bash
git clone git@github.com:alghanmi/dotvim.git ~/.vim
mkdir -p ~/.vim/.swap ~/.vim/.undo
ln -s ~/.vim/vimrc ~/.vimrc
```

###Updating Plugins
In order to pull the latest plugin code from their upstream repositories, we need to maintain a list of origins:

```bash
git remote add conky-syntax git@github.com:smancill/conky-syntax.vim.git
git remote add ctrlp git@github.com:kien/ctrlp.vim.git
git remote add dirdiff git@github.com:will133/vim-dirdiff.git
git remote add nerdcommenter git@github.com:scrooloose/nerdcommenter.git
git remote add nerdtree git@github.com:scrooloose/nerdtree.git
git remote add nginx-syntax git@github.com:evanmiller/nginx-vim-syntax.git
git remote add pathogen git@github.com:tpope/vim-pathogen.git
git remote add python-mode git@github.com:klen/python-mode.git
git remote add repeat git@github.com:tpope/vim-repeat.git
git remote add solarized git@github.com:altercation/vim-colors-solarized.git
git remote add surround git@github.com:tpope/vim-surround.git
git remote add vim-fugitive git@github.com:tpope/vim-fugitive.git
git remote add vim-hclfmt git@github.com:fatih/vim-hclfmt.git
git remote add vim-tmux git@github.com:tmux-plugins/vim-tmux.git
git remote add vim-tmux-focus-events git@github.com:tmux-plugins/vim-tmux-focus-events.git
```

Once the remotes are set, we can pull the latest code from the master branch of each upstream repository independenty:
```bash
git subtree pull --squash --prefix=bundle/conky-syntax conky-syntax master
git subtree pull --squash --prefix=bundle/ctrlp ctrlp master
git subtree pull --squash --prefix=bundle/fugitive vim-fugitive master
git subtree pull --squash --prefix=bundle/nerdcommenter nerdcommenter master
git subtree pull --squash --prefix=bundle/nerdtree nerdtree master
git subtree pull --squash --prefix=bundle/nginx-syntax nginx-syntax master
git subtree pull --squash --prefix=bundle/python-mode python-mode master
git subtree pull --squash --prefix=bundle/repeat repeat master
git subtree pull --squash --prefix=bundle/solarized solarized master
git subtree pull --squash --prefix=bundle/surround surround master
git subtree pull --squash --prefix=bundle/vim-dirdiff dirdiff master
git subtree pull --squash --prefix=bundle/vim-hclfmt vim-hclfmt master
git subtree pull --squash --prefix=bundle/vim-pathogen pathogen master
git subtree pull --squash --prefix=bundle/vim-tmux vim-tmux master
git subtree pull --squash --prefix=bundle/vim-tmux-focus-events vim-tmux-focus-events master
```

###Adding a New Plugin

```bash
# Add a remote for the submodule (use https to avoid auth errors with ssh)
git remote add solarized git@github.com:altercation/vim-colors-solarized.git

# Add the subtree
git subtree add --squash --prefix=bundle/solarized solarized master
```
