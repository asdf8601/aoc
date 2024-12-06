-- create autogroup
local aoc = vim.api.nvim_create_augroup('AoC', { clear = true })

vim.api.nvim_create_autocmd('BufWritePost', {
  command = ':!go run %',
  group = aoc,
  pattern = '*.go',
})

vim.api.nvim_create_autocmd('BufWritePost', {
  command = ':!uv run %',
  group = aoc,
  pattern = '*.py',
})

-- vim: set ts=2 sw=2 tw=80 et :
