return {
    "lervag/vimtex",
    config = function()
        vim.g.vimtex_quickfix_mode = 0
        vim.g.vimtex_syntax_enabled = 1
        vim.g.vimtex_completion_enabled = 1
        vim.g.vimtex_indent_enabled = 0
        vim.g.vimtex_mappings_enabled = 0
        -- vim.g.vimtex_syntax_enabled = 0

        vim.keymap.set('n', 'lr', '<Plug>(vimtex-delim-toggle-modifier)', { remap = true, silent = true })
        vim.keymap.set('n', 'cse', '<Plug>(vimtex-env-change)', { remap = true, silent = true })
        vim.keymap.set('n', 'csd', '<Plug>(vimtex-env-change-math)', { remap = true, silent = true })
        vim.keymap.set('i', '<c-l>', '<Esc><Plug>(vimtex-delim-toggle-modifier)a', { remap = true, silent = true })
        vim.keymap.set('n', '<leader>ll', '<Plug>(vimtex-compile)', { remap = true, silent = true })
        vim.keymap.set('n', '<leader>lc', '<Plug>(vimtex-clean)', { remap = true, silent = true })
        vim.keymap.set('n', '<leader>lC', '<Plug>(vimtex-clean-full)', { remap = true, silent = true })
        vim.keymap.set('n', '<leader>le', '<Plug>(vimtex-errors)', { remap = true, silent = true })
    end
}
