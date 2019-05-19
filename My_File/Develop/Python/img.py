syntax on
set nu!
 15 set nocompatible
 16 set guifont=Luxi/ Mono/9
 17 set filetype on
 18 "set history=100 "记录历史行数"
 19 "set background=dark"背景用黑色"
 20 set autoindent
 21 set cindent
 22 set tabstop=8
 23 set shifwidth=4
 24 set ai!
 25 set showmatch "设置匹配模式，类似当输入一个左括号时会匹配相应的右括号 "
 26 set guioptions-=F "去除vim的GUI版本中得toolbar"
 27 set vb t_vb= "当vim进行编辑时，如果命令错误，会发出警报，该设置去掉警报"
 28 set ruler "在编辑过程中，在右下角显示光标位置的状态行"
 29 set nohls "默认情况下，寻找匹配是高亮度显示，该设置关闭高亮显示"
 30 set incsearch "在程序中查询一单词，自动匹配单词的位置；如查询desk单词，当输>    到/d时，会自动找到第一个d开头的单词，当输入到/de时，会自动找到第一个以ds开头
    的单词，以此类推，进行查找；当找到要匹配的单词时，别忘记回车"
 31 set backspace=2 " 设置退格键可用"
