let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

if !has("python3")
    echo "vim has to be compiled with +python3 to run this"
    finish
endif

if exists('g:dox_align_plugin_loaded')
    finish
endif

let g:sample_plugin_loaded = 1

function! DoxAlign(arg)
python3 << EOF
# Resolve argument.
import vim
arg = vim.eval("a:arg")

# Resolve function.
import sys
from os.path import normpath, join
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)

from doxygen_align import doxygen_align
doxygen_align(arg)
EOF
endfunction

let g:dox_align_plugin_loaded = 1
