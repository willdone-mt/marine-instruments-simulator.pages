import PyInstaller.__main__

PyInstaller.__main__.run([
    '--onefile',
    '--paths=src',
    'src/main_ui.py',
    '--add-data=src:src',
    '--workpath=build/build_temp',
    '--distpath=pages',
    # '--noconsole',
    # '--hide-console=hide-early',
    '--name=SIRENIA'
])