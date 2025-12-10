[app]

title = Test App
package.name = kivy
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3==3.9,kivy

orientation = portrait
fullscreen = 0
android.archs = armeabi-v7a

android.accept_sdk_license = True
#p4a.branch = develop

[buildozer]
log_level = 2
