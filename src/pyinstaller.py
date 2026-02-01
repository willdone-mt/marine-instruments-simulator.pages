import PyInstaller.__main__

PyInstaller.__main__.run([
    '--onefile',
    '--paths=src',
    'src/main_ui.py',
    '--add-data=src/instruments/handrefractometer:handrefractometer',
    '--workpath=build/build_temp',
    '--distpath=build/dist',
    # '--noconsole',
    # '--hide-console=hide-early',
    '--name=SIRENIA'
])