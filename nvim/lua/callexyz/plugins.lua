require("lazy").setup(
    {
        require "callexyz/plugins/colorscheme",
        require "callexyz/plugins/ultisnips",
        require "callexyz/plugins/lualine",
        require "callexyz/plugins/vimtex",
        require "callexyz/plugins/telescope",
        require "callexyz/plugins/treesitter",
        require "callexyz/plugins/autopairs",
    },
    {
        ui = {
            icons = {},
        },
    }
)
