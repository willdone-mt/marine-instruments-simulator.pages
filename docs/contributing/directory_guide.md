# Contributing Guidelines - Directory Information

# Branches

## pages (not actually a branch, it just a public subtree repository)
- Public repository, subtree of the main project repository
- for editing and storing:
    - client side documentations
- release and tag

## main
- for editing:
    - developer side documentations
    - non-coding only
    - small hotfixes
- merge and store other branches
- tag only

Allowed folders and files to be edited are only:

- pages/
- assets/
    
## InDev
- coding only
- coding documentation
- start of x version

Allowed folders and files to be edited are only:

- src/
- build/

## alpha
- coding only
- coding documentation
- start of y version

## beta
- coding only
- coding documentation
- start of z version

# Folders and Files

## assets/

Folder to store creative works. Other materials intended for use as visuals and sounds are kept here first, then picked the best to be placed in src/assets/. But mostly will be used for raw file of artwork that cannot contain privacy information.

All expected creative works should be made by designer/developers of this software and should be licensed with CC BY NC SA

## build/

pyinstaller.py scripts, and temporary builds

## docs/

folder `docs` that located in this repository contains  developer-side documentation, which things that dedicated for developers

`docs/` that located inside `pages/` are for clients

## pages/ (will be changed to dist/)

where public subtree repository located. and also place for final executable file and dependencies.

all things here are dedicated for clients and some files that be used by the exe.

## src/

where are all be build :)

### instruments/

folders that acts as module/ packages, contains file that replicate/simulate the operation of certain instruments

### ui/

folders that acts as module/packages, contains file that be used for UI

# Naming Directories

In documenting and developing SIRENIA exe, imagine all files even in the deepest subfolders are in the same root directory. The only things that make each file distinguishable is the name.

Folders are used to group files based on their purpose.

- A file is named with at least its entity and its role which separated by an underscore `_` and ends with it's extension. 

    - **Entity** = the subject, tool, or concept (e.g., `handrefractometer`, `changelog`, `workflow`).  
    - **Role** = the function or purpose (`ui`, `action`, `guide`).  
    - **Extension** = file type (`.py`, `.md`, etc.). 

    Entity and role name with multiple words are distinguished by the capital letter of the second word of the sentence.

    `<entityName>_<roleName>.<extension>` or `<roleName>_<entityName>.<extension>`

    Examples:

    - `handrefractometer_ui.py`
    - `handrefractometer_action.py`
    - `changelog_guide.md`
    - `workflow_guide.md`

    However, this naming convention is purely encouraged aestethic.

