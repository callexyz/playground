return {
    "nvim-telescope/telescope.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
        require("telescope").setup({
            defaults = {
                mappings = {
                    i = {

                    },
                    n = {

                    },
                },
            },
            pickers = {

            },
            extensions = {

            },
        })
    end
}
