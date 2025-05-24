[app]
title = PDFViewer
package.name = pdfviewer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyjnius,pillow,pymupdf,android
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
android.arch = armeabi-v7a,arm64-v8a
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.accept_sdk_license = true
android.accept_android_sdk_license = true
android.enable_androidx = true
android.gradle_dependencies = androidx.activity:activity:1.7.2

# Optional: for better PDF/image compatibility
android.allow_backup = true
android.hardwareAccelerated = true
