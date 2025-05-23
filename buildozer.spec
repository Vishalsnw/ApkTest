[app]

# (str) Title of your application
title = PDF Viewer

# (str) Package name
package.name = pdfviewer

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) Application requirements
requirements = python3,kivy,PyMuPDF,Pillow

# (str) Icon of the app
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (list) Permissions needed
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (str) Supported Android API version
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Target API for the APK
android.target = 33

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK API to use
android.ndk_api = 21

# (bool) Whether to enable android logcat output
android.logcat = True

# (str) Presplash screen
# presplash.filename = %(source.dir)s/data/presplash.png

# (list) List of Java classes to add (optional)
# android.add_jars =

# (list) List of Java .jar files to add
# android.add_libs_armeabi_v7a =

# (str) Gradle settings
# android.gradle_dependencies =

# (list) Android Java sources to include
# android.add_src =

# (bool) Enable Android X support
# android.enable_androidx = True

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Presplash color
# presplash.color = #FFFFFF

# (str) Android entry point, default is org.kivy.android.PythonActivity
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is '@android:style/Theme.NoTitleBar'
# android.theme = '@android:style/Theme.NoTitleBar'
