# -*- mode: python -*-

block_cipher = None


a = Analysis(['CopybookGeneratorApp.py'],
             pathex=['/Users/zhongxiaoxi/copybook_generator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='CopybookGeneratorApp',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='CopybookGeneratorApp')
app = BUNDLE(coll,
             name='CopybookGeneratorApp.app',
             icon=None,
             bundle_identifier=None)
