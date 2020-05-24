let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

" Check that python is available.
if !has("python3")
    echo "vim has to be compiled with +python3 to run this"
    finish
endif

" Import Script.
python3 << EOF
# Resolve argument.
import vim

# Resolve function.
import sys
from os.path import normpath, join
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
from doxygen_align import doxygen_align
EOF

" Define alignment function.
function! DoxAlign(arg)
python3 << EOF
import vim
arg = vim.eval("a:arg")
out = doxygen_align(arg)
EOF

return py3eval('out')
endfunction

" #pragma once
if exists('g:dox_align_plugin_loaded')
    finish
endif
let g:dox_align_plugin_loaded = 1
