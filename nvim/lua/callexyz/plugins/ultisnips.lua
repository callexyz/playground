return {
    "SirVer/UltiSnips",
    config = function()
        vim.g.UltiSnipsSnippetDirectories = { "/home/lcallegari/.config/nvim/plugins/UltiSnips" }
        vim.g.UltiSnipsExpandTrigger = "<tab>"
        vim.g.UltiSnipsJumpForwardTrigger = "<tab>"
        vim.g.UltiSnipsJumpBackwardTrigger = "<s-tab>"
        vim.g.UltiSnipsEditSplit = "vertical"
    end,
}
