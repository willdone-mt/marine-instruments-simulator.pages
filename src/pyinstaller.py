import PyInstaller.__main__

PyInstaller.__main__.run([
    '--onefile',
    '--paths=src',
    'src/main/master.py',
    # '--add-data=src/instruments/hand_refractometer:hand_refractometer',
    '--workpath=build/build_temp',
    '--distpath=build/dist',
    # '--hide-console=hide-early',
    '--name=SIRENIA'
])