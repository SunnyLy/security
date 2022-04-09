1、BlackDex：
      a)、选择对应架构的apk安装到手机上，手机无需Root,也无需Xposed
      b)、github:https://github.com/CodingGay/BlackDex

2、FDex2:
       a)、不需要Root手机，需要装Xposed

3、PKID:
       一个APK壳检测工具，检测APK是否加壳，以及采用哪家的壳

4、drizzleDumper:
      一个在linux下的脱壳工具，需要手机Root,使用步骤：
     a)、将drizzleDumper push到手机某一目录下，比如：
           adb push drizzleDumper64 /data/local/tmp
           adb shell "chmod 777 /data/local/tmp/drizzleDumper64"
           接下来开始执行命令进行脱壳
           adb shell
           ./data/local/tmp/drizzleDumper64 <应用包名>
           这时窗口会进入等待状态，此里需要用户在手机上打开对应应用。drizzleDumper工具才会Hook到对应进程。

5、xapkdetector:
        一个apk/dex等壳检测工具
        a)、github:https://github.com/horsicq/XAPKDetector
        b)、知乎：https://zhuanlan.zhihu.com/p/310665648
