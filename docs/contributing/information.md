# Contributing

# Branches

## pages (not actually a branch, it just a public subtree repository)
- Public repository, subtree of the main project repository
- for editing and storing:
    - client side documentations
- release and tag

## main
- for editing and storing:
    - developer side documentations
    - non-coding only
    - small hotfixes
- tag only
    
## InDev
- coding only
- coding documentation
- start of x version

## alpha
- coding only
- coding documentation
- start of y version

## beta
- coding only
- coding documentation
- start of z version

# Folders and Files

## /assets

Folder to store creative works. Other materials intended for use as visuals and sounds are kept here first, then picked the best to be placed in src/assets/. But mostly will be used for raw file of artwork that cannot contain privacy information.

All expected creative works should be made by designer/developers of this software and should be licensed with CC BY SA

## /build

pyinstaller.py script

## /docs

folder ```/docs``` that located in this repository contains  developer-side documentation, which things that dedicated for developers

```/docs``` that located inside ```/pages``` are for clients

## /pages

where public subtree repository located.

all things here are dedicated for clients and some files that be used by the exe.

## /src

where are all be build :)

### /instruments

folders that acts as module/ packages, contains file that replicate/simulate the operation of certain instruments



# Changelogs

# CHANGELOGS

- Notices
    - Will try to follow semantic versioning templates

- Formatting
    - InDev  
        ```v0.Y.Z+<commit number>```  
    unstable, not yet open for public (public in this case is announced for students)
    - Alpha  
        ```vX.Y.Z-alpha.xyz```
    - Beta  
        ```vX.Y.Z-beta.xyz```
    - Full/Stable release  
        ```vX.Y.Z```
    - Hotfix  
        ```<latest version>+<problem>Fix/<commit number>```

- Update Formatting  
```
# <version> - <yyyy/mm/dd>
"<title update if major>"

##


```

# Workflows

- check virus
- merging
- tag and release
