# denite-rails

denite-rails is a Denite.nvim source for Rails.

```
Denite rails:dwim
```

to list correspoinding files to the current buffer's file in Denite buffer.

denite-rails also provide the below command to list specific files.


```
Denite rails:model
Denite rails:controller
Denite rails:view
Denite rails:helper
Denite rails:test
Denite rails:spec
Denite rails:ability
Denite rails:validator
Denite rails:decorator
Denite rails:mailer
Denite rails:asset
Denite rails:service
Denite rails:form
Denite rails:serializer
Denite rails:config
Denite rails:attribute
Denite rails:policy
Denite rails:loyalty
Denite rails:domain
```

## Keymap examples

```vim
nnoremap [rails] <Nop>
nmap     <Leader>r [rails]
nnoremap [rails]r :Denite<Space>rails:
nnoremap <silent> [rails]r :<C-u>Denite<Space>rails:dwim<Return>
nnoremap <silent> [rails]m :<C-u>Denite<Space>rails:model<Return>
nnoremap <silent> [rails]c :<C-u>Denite<Space>rails:controller<Return>
nnoremap <silent> [rails]v :<C-u>Denite<Space>rails:view<Return>
nnoremap <silent> [rails]h :<C-u>Denite<Space>rails:helper<Return>
nnoremap <silent> [rails]r :<C-u>Denite<Space>rails:test<Return>
nnoremap <silent> [rails]s :<C-u>Denite<Space>rails:spec<Return>
```

## TODO

- Support decorators/fixtures/etc.
- Support RSpec/Cucumber/etc.
- Smarter namespace handling
- Refactoring
- Write tests
