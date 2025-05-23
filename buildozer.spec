[app]
title = PDFViewer
package.name = pdfviewer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyjnius,pillow,PyMuPDF
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = armeabi-v7a
# If needed, enable this
# android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
# Force accept licenses (important for CI)
android.accept_sdk_license = true
android.accept_android_sdk_license = true
