# Turtle Language Server

[![PyPI version](https://badge.fury.io/py/turtle_language_server.svg)](https://badge.fury.io/py/turtle_language_server)

This is a [LSP server](https://langserver.org/) implementation for RDF graphs serialized as Turtle.

Install with: `pip install turtle_language_server`.

If you wish to modify the code instead of just running it, see the "Development" section
below.

## Commands and Features

- Use the `loadGraphs` command to pull in the graph definitions listed as prefixes in your Turtle file:
    ```
    # caches graphs in-memory for NeoVim session
    :CocCommand loadGraphs
    ```
    
    ```
    # overrides cache and pulls graphs anyway
    :CocCommand loadGraphs force
    ```
- syntax checking your Turtle file (including undefined namespaces)
- auto-complete when adding statements to the file (relies on `loadGraphs`)

## TODOs:

- [ ] verify shapes and add validation information to UI


## Setup With NeoVim and CoC

If you are using [`coc.nvim`](https://github.com/neoclide/coc.nvim), you can configure the language server as follows:

1. Make sure Vim correctly detects turtle files and sets the filetype. One way to achieve this
   is by adding the following line to your `.vimrc` or `init.nvim`:

   ```vimrc
   au BufRead,BufNewFile *.ttl set filetype=turtle
   ```
2. Modify your CoC settings to use the `turtle_language_server` when you open a Turtle file.
    1. First, run `:CocConfig` or edit `coc-settings.json`
    2. Add the following (merge with existing keys in `"languageserver"` if needed):
        ```json
        {
          "languageserver": {
            "turtle": {
              "command": "turtle_langserver",
              "filetypes": ["ttl", "turtle"]
            }
          }
        }
        ```

## Development

First, clone the git repository:

```
git clone https://github.com/Spyderisk/langserver
cd langserver
```

You need the `poetry` python package management tool, which you need to install using your
operating systenm's native package manager. For example, `apt install python3-poetry` or
`pacman -S poetry`.

Then, in the new `langserver` directory:

```
poetry install
```

This should install all of the python dependencies listed in the `pyproject.toml` file.
Poetry installs to a standard Python venv virtual environment.

Next decide on a port you wish the LSP server to listen on. Since this is an experimental
service it should never be exposed on the internet, so the only interface to use with it
is `localhost`. You will need to choose an unnused port, which you can verify using 
`nmap localhost`. In the following we have chosen port 7213 for no particular reason.
You should now be able to start the LSP server like this:

```
$ python turtle_language_server/entry.py --tcp localhost:7213
DEBUG:asyncio:Using selector: EpollSelector
INFO:pygls.feature_manager:Registered builtin feature exit
INFO:pygls.feature_manager:Registered builtin feature initialize
INFO:pygls.feature_manager:Registered builtin feature initialized
INFO:pygls.feature_manager:Registered builtin feature shutdown
INFO:pygls.feature_manager:Registered builtin feature textDocument/didChange
INFO:pygls.feature_manager:Registered builtin feature textDocument/didClose
INFO:pygls.feature_manager:Registered builtin feature textDocument/didOpen
INFO:pygls.feature_manager:Registered builtin feature workspace/didChangeWorkspaceFolders
INFO:pygls.feature_manager:Registered builtin feature workspace/executeCommand
INFO:pygls.feature_manager:Command loadGraphs is successfully registered.
INFO:pygls.feature_manager:Registered textDocument/completion with options {'trigger_characters': [':']}
INFO:pygls.feature_manager:Command countDownBlocking is successfully registered.
INFO:pygls.feature_manager:Command countDownNonBlocking is successfully registered.
INFO:pygls.feature_manager:Registered textDocument/didChange with options {}
INFO:pygls.feature_manager:Registered textDocument/didClose with options {}
INFO:pygls.feature_manager:Registered textDocument/didOpen with options {}
INFO:pygls.feature_manager:Registered textDocument/didSave with options {}
INFO:pygls.feature_manager:Command registerCompletions is successfully registered.
INFO:pygls.server:Starting server on localhost:1113
```

Now you can start testing, and modifying server.py.
